import csv
import argparse
import os
from dotenv import load_dotenv

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-u', '--user', help='Filter specific user(s) by UID', required=False, nargs='+')
arg_parser.add_argument('-d', '--delimiter', help='Define custom delimiter',required=False, default=',')
arg_parser.add_argument('-w', '--withdraw', help='Filter only withdrawing transactions', action='store_true' ,required=False)
arg_parser.add_argument('-dp', '--deposit', help='Filter only deposit transactions', action='store_true' ,required=False)
arg_parser.add_argument('-i', '--input', help="Provide an input CSV-file", required=True)
arg_parser.add_argument('-o', '--output', help="Provide an output filename", required=False, default='summary.csv')
arg_parser.add_argument('-v', '--verbose', help='Verbose output', required=False)
arg_parser.add_argument('-c', '--currency', help='Filter transactions by currency', required=False, default='USD')


args = arg_parser.parse_args()

load_dotenv()
api_key = os.getenv('API_KEY')


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
                summary[uid_val] = {'total_amount_withdraw': 0.0, 'total_amount_deposit': 0.0, 'transaction_count': 0}

            if transaction_type == 'd':
                summary[uid_val]['total_amount_deposit'] += amount_val
            elif transaction_type == 'w':
                summary[uid_val]['total_amount_withdraw'] += amount_val
            else:
                print(f"Invalid transaction type '{transaction_type}'")
                print("Should be 'd' for 'deposit' or 'w' for 'withdraw'")

            summary[uid_val]['transaction_count'] += 1

    except FileNotFoundError:
        print("Error: The file does not exist")

    if not summary:
        print(f"No data found for user '{uid_val}'")

    with open(args.output, mode='w', newline='',encoding='utf-8') as result:
        fieldnames = ['uid', 'total_amount_withdraw', 'total_amount_deposit', 'transaction_count']

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
                    'total_amount_withdraw': summary[uid]['total_amount_withdraw'],
                    'total_amount_deposit': summary[uid]['total_amount_deposit'],
                    'transaction_count': summary[uid]['transaction_count']
                }
            )

        if args.verbose:
            print(f"Done! Results saved in {args.output}")