from expense import ExpenseTracker as eT

system = 'Expense Tracker'


def identify_command(parts):
    command = parts[0]
    try:
        match command:
            case "add":
                if parts[1] == '--description' and len(parts) > 4:
                    description = parts[2]
                    amount = int(parts[4]) if parts[3] == '--amount' else None
                    if description and amount:
                        eT.add_expense(description, amount)
                    else:
                        print("[Error]: Invalid description or amount.")
                    return True
                print("[Error]: Proper arguments for 'add' are missing.")
                return True

            case 'update':
                if parts[1] == '--id' and len(parts) > 4:
                    _id = int(parts[2])
                    amount = int(parts[4]) if parts[3] == '--amount' else None
                    if amount:
                        eT.update_expense(_id, amount)
                    else:
                        print("[Error]: New amount not specified.")
                    return True
                print("[Error]: Proper arguments for 'update' are missing.")
                return True

            case 'delete':
                if parts[1] == "--id" and len(parts) > 2:
                    _id = int(parts[2])
                    eT.delete_expense(_id)
                else:
                    print("[Error]: No id provided for deletion.")
                return True

            case 'list':
                month = int(parts[2]) if len(parts) > 2 and parts[1] == '--month' else 0
                eT.list_expenses(month)
                return True

            case 'summary':
                month = int(parts[2]) if len(parts) > 2 and parts[1] == '--month' else 0
                eT.summary(month)
                return True

            case 'quit':
                _quit = input("Are you sure you want to quit? (Y/N): ").strip().lower()
                if _quit == "y":
                    print(f"[{system}]: Exiting Expense Tracker...")
                    return False
                print(f"[{system}]: Continuing...")
                return True

            case 'export':
                eT.export_expenses()
                return True
            case _:
                print('Command not recognized!')
                return True
    except (IndexError, ValueError) as e:
        print(f"[Error]: Invalid command syntax - {e}")
        return True


def main():
    print("Expense Tracker")
    while True:
        print("--------------------")
        user_input = input("Enter command: ")
        if user_input.startswith("expense-tracker"):
            parts = user_input.split()
            command = parts[1:]
            running = identify_command(command)
            if running:
                continue
            else:
                break
        else:
            print(f'[Error]: Command "{user_input}" is not recognized! ')


if __name__ == "__main__":
    main()
