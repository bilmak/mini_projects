import csv

transactions = []

def finance_manager(file):
    total = 0
    
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader) # skip Transaction ID
        for row in csv_reader:
            name = row[4]
            amount = float(row[7])
            date = row[1]
            
            transaction = (date, name, amount)
            total+= amount
            transactions.append(transaction)
            
    print(f"The sum of transactions is: {total}")
    return transactions


finance_manager("monzo_july_sample.csv")
            
        
    