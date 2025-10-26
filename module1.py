
from datetime import datetime 
import csv 
 
class Transaction: 
    def __init__(self, user, amount, category, date): 
        self.user = user 
        self.amount = amount 
        self.category = category 
        self.date = date 
 
def enter_transaction(categories): 
    user, amount = input("Enter your Name: "), float(input("Enter 
the amount: ")) 
    print("Available categories:") 
    for i, category in enumerate(categories, 1): 
        print(f"{i}. {category}") 
    category = categories[int(input("Enter the category number: ")) - 1] 
    return Transaction(user, amount, category, 
datetime.now().strftime("%Y-%m-%d")) 
 
def view_transactions(transactions): 
    if transactions: 
        for i, transaction in enumerate(transactions, 1): 
            print(f"{i}. Name: {transaction.user}, amount: 
{transaction.amount}, Category: {transaction.category}, Date: 
{transaction.date}") 
    else: 
        print("No transactions yet.") 
 
def sort_transactions(transactions, key): 
    if key in ['user', 'category']: 
        return sorted(transactions, key=lambda x: getattr(x, key)) 
    print("Invalid sorting key.") 
    return transactions 
 
def update_transaction(transactions): 
    view_transactions(transactions) 
    index = int(input("Enter the index of the transaction to update: 
")) - 1 
    transaction = transactions[index] 
    transaction.amount, transaction.category, transaction.date = 
float(input("Enter the new amount: ")), input("Enter the new 
category: "), datetime.now().strftime("%Y-%m-%d") 
    print("Transaction updated successfully!") 
 
def delete_transaction(transactions): 
    view_transactions(transactions) 
    del transactions[int(input("Enter the index of the transaction 
to delete: ")) - 1] 
    print("Transaction deleted successfully!") 
 
def export_transactions_to_csv(transactions): 
    with open ('my_file.csv','w', newline='') as f: 
        csv.writer(f).writerows([["Name", "amount", "Category", 
"Date"]] + [[t.user, t.amount, t.category, t.date] for t in 
transactions]) 
    print("Transactions exported to project.csv") 
 
def report(transactions): 
    print(f"Total Expenses: {sum(transaction.amount for transaction 
in transactions if transaction.amount < 0)}") 
    print(f"Total Income: {sum(transaction.amount for transaction in 
transactions if transaction.amount > 0)}") 
    category_spending = {} 
    category_counts = {} 
    for transaction in transactions: 
        category_spending[transaction.category] = 
category_spending.get(transaction.category, 0) + transaction.amount 
        category_counts[transaction.category] = 
category_counts.get(transaction.category, 0) + 1 
    print("\nSpending by Category:") 
    for category, spending in category_spending.items(): 
        print(f"{category}: {spending}") 
    print("\nAverage Transaction Value by Category:") 
    for category, total in category_spending.items(): 
        print(f"{category}: {total / category_counts[category]}") 
 
def main(): 
    categories = ["Food", "Transportation", "Entertainment", 
"Salary", "Medical service"] 
    transactions = [] 
 
    while True: 
        print("\n1. Enter a transaction") 
        print("2. View all transactions") 
        print("3. Sort transactions") 
        print("4. Update a transaction") 
        print("5. Delete a transaction") 
        print("6. Generate Basic Reports")