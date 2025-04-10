import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = {
            '1': 'Food',
            '2': 'Transport',
            '3': 'Entertainment',
            '4': 'Bills',
            '5': 'Shopping',
            '6': 'Other'
        }
        self.load_data()

    def add_expense(self):
        print("\nAdd New Expense")
        amount = float(input("Enter amount spent: $"))
        
        print("\nCategories:")
        for num, name in self.categories.items():
            print(f"{num}. {name}")
        
        while True:
            cat_choice = input("Select category (1-6): ")
            if cat_choice in self.categories:
                category = self.categories[cat_choice]
                break
            print("Invalid choice. Try again.")
        
        note = input("Add a note (optional): ").strip()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.expenses.append({
            'amount': amount,
            'category': category,
            'note': note,
            'date': date
        })
        
        self.save_data()
        print("Expense added successfully!")

    def view_summary(self):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return
        
        total = sum(exp['amount'] for exp in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")
        
        print("\nLast 5 Expenses:")
        for exp in self.expenses[-5:][::-1]:
            print(f"{exp['date']} - {exp['category']}: ${exp['amount']:.2f} - {exp['note']}")

    def show_charts(self):
        if not self.expenses:
            print("\nNo expenses to visualize!")
            return
        
        # Pie Chart by Category
        category_totals = defaultdict(float)
        for exp in self.expenses:
            category_totals[exp['category']] += exp['amount']
        
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.pie(
            category_totals.values(),
            labels=category_totals.keys(),
            autopct='%1.1f%%',
            startangle=90
        )
        plt.title("Spending by Category")
        
        # Bar Chart (Last 7 Days)
        daily_totals = defaultdict(float)
        for exp in self.expenses[-30:]:  # Last 30 expenses
            date = exp['date'].split()[0]
            daily_totals[date] += exp['amount']
        
        dates = sorted(daily_totals.keys())[-7:]  # Last 7 days
        amounts = [daily_totals[d] for d in dates]
        
        plt.subplot(1, 2, 2)
        plt.bar(dates, amounts)
        plt.title("Last 7 Days Spending")
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.show()

    def save_data(self):
        with open('expenses.json', 'w') as f:
            json.dump(self.expenses, f)

    def load_data(self):
        if os.path.exists('expenses.json'):
            with open('expenses.json', 'r') as f:
                self.expenses = json.load(f)

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Show Charts")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_summary()
        elif choice == '3':
            tracker.show_charts()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
