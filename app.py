import csv


summary = {}

with open('transactions.csv', mode='w') as transactions_file:
    reader = csv.DictReader(transactions_file)

    for row in reader:
        uid_val = row['uid']
        amount_val = float(row['amount'])

        if id_val not in summary:
            summary[uid_val] = {'total_amount': 0.0, 'transaction_count': 0}

        summary[uid_val]['total_amount'] += amount_val
        summary[uid_val]['transaction_count'] += 1

    with open('summary.csv', mode='w') as summary:
        fieldnames = ['uid', 'total_amount', 'transaction_count']
        writer = csv.DictWriter(summary, fieldnames=fieldnames)
        writer.writeheader()

        for uid_val in summary.keys():
            writer.write(summary[uid_val])
