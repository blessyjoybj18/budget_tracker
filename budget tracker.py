# Budget Tracker App

import datetime

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description):
        self.transactions.append({
            'type': 'Income',
            'amount': amount,
            'description': description,
            'date': datetime.datetime.now()
        })

    def add_expense(self, amount, description):
        self.transactions.append({
            'type': 'Expense',
            'amount': amount,
            'description': description,
            'date': datetime.datetime.now()
        })

    def view_summary(self):
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'Income')
        expense = sum(t['amount'] for t in self.transactions if t['type'] == 'Expense')
        balance = income - expense
        print("\n=== Budget Summary ===")
        print(f"Total Income: ₹{income:.2f}")
        print(f"Total Expense: ₹{expense:.2f}")
        print(f"Balance: ₹{balance:.2f}\n")

    def view_transactions(self):
        print("\n=== All Transactions ===")
        for t in self.transactions:
            print(f"[{t['date'].strftime('%Y-%m-%d %H:%M')}] {t['type']}: ₹{t['amount']} - {t['description']}")


def main():
    tracker = BudgetTracker()

    while True:
        print("\n--- Budget Tracker Menu ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View All Transactions")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter income amount: ₹"))
            description = input("Enter income description: ")
            tracker.add_income(amount, description)
        elif choice == '2':
            amount = float(input("Enter expense amount: ₹"))
            description = input("Enter expense description: ")
            tracker.add_expense(amount, description)
        elif choice == '3':
            tracker.view_summary()
        elif choice == '4':
            tracker.view_transactions()
        elif choice == '5':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
