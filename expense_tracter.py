import csv
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "date": row["date"],
                    "category": row["category"],
                    "amount": float(row["amount"])
                })
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount"])
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")
        date_text = input("Enter date (YYYY-MM-DD): ").strip()
        datetime.strptime(date_text, "%Y-%m-%d")
        expenses.append({
            "amount": amount,
            "category": category,
            "date": date_text
        })
        print("Expense added successfully.")
    except ValueError as error:
        print("Invalid input:", error)

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"{expense['date']} | {expense['category']} | ${expense['amount']:.2f}")

def generate_report(expenses):
    if not expenses:
        print("No data available.")
        return
    total = sum(e["amount"] for e in expenses)
    highest = max(expenses, key=lambda e: e["amount"])
    average = total / len(expenses)
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
    print("Total spent:", total)
    print("Average expense:", average)
    print("Highest expense:", highest)
    print("Category totals:", category_totals)

def visualize_expenses(expenses):
    if not expenses:
        print("No data available to visualize.")
        return
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
    plt.bar(category_totals.keys(), category_totals.values())
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

def main():
    expenses = load_expenses()
    while True:
        print("\nWelcome to Personal Expense Tracker!")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Generate Report")
        print("4. Visualize Expenses")
        print("5. Save and Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            generate_report(expenses)
        elif choice == "4":
            visualize_expenses(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()