# Smart Expense Tracker

expenses = {}

def add_expense():
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))
    
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
        
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
    else:
        print("Expense Summary:")
        for category, amount in expenses.items():
            print(f"{category}: ₹{amount}")
        print()

def total_spending():
    total = sum(expenses.values())
    print(f"Total Spending: ₹{total}\n")

def highest_spending():
    if not expenses:
        print("No expenses recorded.\n")
    else:
        highest = max(expenses, key=expenses.get)
        print(f"Highest Spending Category: {highest} (₹{expenses[highest]})\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Highest Spending Category")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spending()
    elif choice == "4":
        highest_spending()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
