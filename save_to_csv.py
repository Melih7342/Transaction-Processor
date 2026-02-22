import argparse, csv

def write_summary(args: argparse.Namespace, summary: dict):

    with open(args.output, mode='w', newline='', encoding='utf-8') as result:
        fieldnames = ['uid', 'total_amount_withdraw', 'total_amount_deposit', 'transaction_count', 'currency']

        if args.verbose:
            print("Setting up the writer...")
        writer = csv.DictWriter(result, fieldnames=fieldnames, delimiter=args.delimiter)

        if args.verbose:
            print(f"Writing the header for the file '{args.output}'...")

        writer.writeheader()

        if args.verbose:
            print(f"Writing summary into '{args.output}'...")

        for uid, stats in summary.items():
            if args.withdraw:
                writer.writerow(
                    {
                        'uid': uid,
                        'total_amount_withdraw': f"{summary[uid]['total_amount_withdraw']:.2f}",
                        'transaction_count': summary[uid]['transaction_count'],
                        'currency': summary[uid]['currency']
                    }
                )
            elif args.deposit:
                writer.writerow(
                    {
                        'uid': uid,
                        'total_amount_deposit': f"{summary[uid]['total_amount_deposit']:.2f}",
                        'transaction_count': summary[uid]['transaction_count'],
                        'currency': summary[uid]['currency']
                    }
                )
            else:
                writer.writerow(
                    {
                        'uid': uid,
                        'total_amount_withdraw': f"{summary[uid]['total_amount_withdraw']:.2f}",
                        'total_amount_deposit': f"{summary[uid]['total_amount_deposit']:.2f}",
                        'transaction_count': summary[uid]['transaction_count'],
                        'currency': summary[uid]['currency']
                    }
                )


        if args.verbose:
            print(f"Done! Results saved in {args.output}")