import csv


summary = {}

with open('transactions.csv', mode='w') as transactions_file:
    reader = csv.DictReader(transactions_file)

    for row in reader:
        id_val = row['uid']
        amount_val = float(row['amount'])

        if id_val not in summary:
            summary[id_val] = {'total_amount': 0.0, 'transaction_count': 0}

        summary[id_val]['total_amount'] += amount_val
        summary[id_val]['transaction_count'] += 1


