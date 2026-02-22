import argparse, csv
from currencies import get_currency_rate



def aggregate(args: argparse.Namespace) -> dict:
    summary = {}
    cache = {}

    with open(args.input, mode='r', encoding='utf-8') as transactions_file:
        try:
            if args.verbose:
                print("Setting up the reader...")

            reader = csv.DictReader(transactions_file)

            if args.verbose:
                print(f"Reading the file '{args.input}'...")

            for row in reader:
                uid_val = row['uid']
                transaction_type = row['type']
                base_cur = row['currency']

                if args.user and uid_val not in args.user:
                    continue

                amount_val = float(row['amount'])

                if uid_val not in summary:
                    summary[uid_val] = {'total_amount_withdraw': 0.0, 'total_amount_deposit': 0.0, 'transaction_count': 0, 'currency': args.currency}

                if transaction_type == 'd':
                    if base_cur != args.currency:
                        if base_cur not in cache:
                            cache[base_cur] = {}
                        if args.currency not in cache[base_cur]:
                            if args.verbose:
                                print(f"Fetching rate: {base_cur} -> {args.currency}")
                            cache[base_cur][args.currency] = get_currency_rate(base_cur, args.currency)
                        summary[uid_val]['total_amount_deposit'] += amount_val * cache[base_cur][args.currency]
                    else:
                        summary[uid_val]['total_amount_deposit'] += amount_val
                elif transaction_type == 'w':
                    if base_cur != args.currency:
                        if base_cur not in cache:
                            cache[base_cur] = {}
                        if args.currency not in cache[base_cur]:
                            if args.verbose:
                                print(f"Fetching rate: {base_cur} -> {args.currency}")
                            cache[base_cur][args.currency] = get_currency_rate(base_cur, args.currency)
                        summary[uid_val]['total_amount_withdraw'] += amount_val * cache[base_cur][args.currency]
                    else:
                        summary[uid_val]['total_amount_withdraw'] += amount_val
                else:
                    print(f"Invalid transaction type '{transaction_type}'")
                    print("Should be 'd' for 'deposit' or 'w' for 'withdraw'")

                summary[uid_val]['transaction_count'] += 1

        except FileNotFoundError:
            print("Error: The file does not exist")

        if not summary:
            print("No data matching the filters found.")

    return summary