import json
from datetime import datetime
from tabulate import tabulate
import pandas as pd

system = 'Expense Tracker'


def write_file(expenses):
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f, indent=4)


def read_file():
    try:
        with open("expenses.json", 'r') as f:
            expenses = json.load(f)
            if not isinstance(expenses, list):
                raise ValueError("JSON file is not an array!")
            else:
                return expenses
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def select_month(month: int):
    match month:
        case 1:
            return 'January'
        case 2:
            return 'February'
        case 3:
            return 'March'
        case 4:
            return 'April'
        case 5:
            return 'May'
        case 6:
            return 'June'
        case 7:
            return 'July'
        case 8:
            return 'August'
        case 9:
            return 'September'
        case 10:
            return 'October'
        case 11:
            return 'November'
        case 12:
            return 'December'
        case _:
            return 'Not a month'


class ExpenseTracker:
    @staticmethod
    def add_expense(description, amount):
        expenses = read_file()

        next_id = max(expense['_id'] for expense in expenses) + 1 if expenses else 1

        expense = {
            "_id": next_id,
            "description": description,
            "amount": amount,
            "date": datetime.now().isoformat(),
            "updated_at": None
        }

        expenses.append(expense)
        write_file(expenses)
        print(f'[{system}]: New expense with id: {next_id} has been added!')

    @staticmethod
    def update_expense(_id, new_amount):
        expenses = read_file()
        found_expense = False

        for expense in expenses:
            if expense['_id'] == _id:
                expense["amount"] = new_amount
                expense['updated_at'] = datetime.now().isoformat()
                found_expense = True
                break

        if found_expense:
            write_file(expenses)
            print(f"[{system}]: Expense with id: {id} has been updated")
        else:
            print(f"[Error]: No expense with id: {id}")

    @staticmethod
    def list_expenses(month=0):
        """List all expenses in a tabular format with formatted dates."""
        expenses = read_file()
        if not expenses:
            print(f"[{system}]: No expenses to display.")
            return

        headers = ['ID', 'Date', 'Updated_At', "Description", "Amount"]
        table = []
        for expense in expenses:
            try:
                date = datetime.fromisoformat(expense['date']).strftime('%Y-%m-%d %H:%M:%S')
                updates_at = (
                    datetime.fromisoformat(expense['updated_at']).strftime('%Y-%m-%d %H:%M:%S')
                    if expense['updated_at'] else 'N/A'
                )
                expense_month = datetime.fromisoformat(expense['date']).month
                if month == 0 or month == expense_month:
                    table.append([
                        expense['_id'],
                        date,
                        updates_at,
                        expense['description'],
                        f"K{expense['amount']:.2f}"
                    ])
            except (KeyError, ValueError) as e:
                print(f"[Error]: Issue with an expense entry - {e}")

        if table:
            if month == 0:
                print(f"[{system}]: List Of All Expenses:")
            else:
                print(f"[{system}]: List of Expenses for {select_month(month)}:")
            print(tabulate(table, headers=headers, tablefmt='grid'))
        else:
            print(f"[{system}]: No expenses found for the selected month.")

    @staticmethod
    def delete_expense(_id):
        delete = input(f"Are you sure you want to delete expense with id: {_id}? (Y/N): ").strip().lower()
        if delete == 'n':
            return ''
        else:
            expenses = read_file()
            initial_length = len(expenses)

            expenses = [expense for expense in expenses if expense['_id'] != _id]
            if initial_length > len(expenses):
                write_file(expenses)
                print(f"[{system}]: Expense with id: {_id} has been deleted!")
            else:
                print(f"[Error]: Expense with id: {_id} was not found!")

    @staticmethod
    def summary(month=0):
        expenses = read_file()
        total = 0

        if not expenses:
            print(f'[{system}]: No expenses to display!')
            return

        for expense in expenses:
            try:
                data = datetime.fromisoformat(expense['date'])
                if month == 0 or data.month == month:
                    total += expense['amount']
            except (KeyError, ValueError) as e:
                print(f"[Error]: Issue with an expense entry - {e}")

        if month == 0:
            print(f"[{system}]: Total expenses: K{total:.2f}")
        else:
            print(f"[{system}]: Total expenses for {select_month(month)}: K{total:.2f}")

    @staticmethod
    def export_expenses():
        expenses = read_file()
        if not expenses:
            print(f"[{system}]: No expenses to export")
            return

        df = pd.DataFrame(expenses)
        df['date'] = pd.to_datetime(df['date'])
        df['updated_at'] = pd.to_datetime(df['updated_at'], errors='coerce')

        df.to_csv('expenses.csv', index=False)
        print(f"[{system}]: Expenses have been exported to 'expenses.csv' successfully!")