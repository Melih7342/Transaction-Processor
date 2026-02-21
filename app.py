import csv


summary = {}

with open('transactions.csv', mode='r', encoding='utf-8') as transactions_file:
    reader = csv.DictReader(transactions_file)

    for row in reader:
        uid_val = row['uid']
        amount_val = float(row['amount'])

        if uid_val not in summary:
            summary[uid_val] = {'total_amount': 0.0, 'transaction_count': 0}

        summary[uid_val]['total_amount'] += amount_val
        summary[uid_val]['transaction_count'] += 1

    with open('summary.csv', mode='w', newline='',encoding='utf-8') as result:
        fieldnames = ['uid', 'total_amount', 'transaction_count']
        writer = csv.DictWriter(result, fieldnames=fieldnames)
        writer.writeheader()

        for uid, stats in summary.items():
            writer.writerow(
                {
                    'uid': uid,
                    'total_amount': summary[uid]['total_amount'],
                    'transaction_count': summary[uid]['transaction_count']
                }
            )
