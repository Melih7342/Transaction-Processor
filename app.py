import csv
import argparse
import os

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-u', '--user', help='Filter specific user(s) by UID', required=False, nargs='+')
arg_parser.add_argument('-d', '--delimiter', help='Define custom delimiter',required=False, default=',')
arg_parser.add_argument('-w', '--withdraw', help='Filter only withdrawing transactions', action='store_true' ,required=False)
arg_parser.add_argument('-dp', '--deposit', help='Filter only deposit transactions', action='store_true' ,required=False)
arg_parser.add_argument('-i', '--input', help="Provide an input CSV-file", required=True)
arg_parser.add_argument('-o', '--output', help="Provide an output filename", required=False, default='summary.csv')
arg_parser.add_argument('-v', '--verbose', help='Verbose output', required=False)


args = arg_parser.parse_args()

summary = {}

if not os.path.exists(args.input):
    print(f"Error: The file '{args.input}' was not found")
    exit(1)

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

            if args.user and uid_val not in args.user:
                continue

            if args.withdraw and transaction_type != 'w' or args.deposit and transaction_type != 'd' :
                continue

            amount_val = float(row['amount'])

            if uid_val not in summary:
                summary[uid_val] = {'total_amount': 0.0, 'transaction_count': 0}

            summary[uid_val]['total_amount'] += amount_val
            summary[uid_val]['transaction_count'] += 1

    except FileNotFoundError:
        print("Error: The file does not exist")

    if not summary:
        print(f"No data found for user '{uid_val}'")

    with open(args.output, mode='w', newline='',encoding='utf-8') as result:
        fieldnames = ['uid', 'total_amount', 'transaction_count']

        if args.verbose:
            print("Setting up the writer...")
        writer = csv.DictWriter(result, fieldnames=fieldnames, delimiter=args.delimiter)

        if args.verbose:
            print(f"Writing the header for the file '{args.output}'...")

        writer.writeheader()

        if args.verbose:
            print(f"Writing summary into '{args.output}'...")

        for uid, stats in summary.items():
            writer.writerow(
                {
                    'uid': uid,
                    'total_amount': summary[uid]['total_amount'],
                    'transaction_count': summary[uid]['transaction_count']
                }
            )

        if args.verbose:
            print(f"Done! Results saved in {args.output}")