# Expense Tracker CLI Application

A simple command-line-based **Expense Tracker** application to manage your finances. This application allows users to **add**, **update**, **delete**, and **view** expenses while also providing monthly and overall expense summaries. Additionally, users can **export expenses to a CSV file** for easy reporting.

---

## 📋 **Features**
- ✅ **Add an expense:** Record expenses with a description and amount.
- ✅ **Update an expense:** Modify the amount of an existing expense.
- ✅ **Delete an expense:** Remove an expense by its ID.
- ✅ **View all expenses:** List all recorded expenses.
- ✅ **View expense summary:** Display total expenses.
- ✅ **Monthly summary:** View total expenses for a specific month.
- ✅ **Export to CSV:** Export all expenses to a CSV file.
- ✅ **Error handling:** Prevent invalid inputs and edge cases.

---

## ⚙️ **Installation**

Make sure you have **Python 3.x** installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/EMMD474/expense-tracker.git
   cd expense-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## 🚀 **Usage**

### Add an Expense
```bash
expense-tracker add --description "Lunch" --amount 20
```
**Output:**
```
[Expense Tracker]: New expense with id: 1 has been added!
```

### Update an Expense
```bash
expense-tracker update --id 1 --amount 25
```
**Output:**
```
[Expense Tracker]: Expense with id: 1 has been updated!
```

### Delete an Expense
```bash
expense-tracker delete --id 1
```
**Output:**
```
[Expense Tracker]: Expense with id: 1 has been deleted!
```

### List All Expenses
```bash
expense-tracker list
```
**Output:**
```
ID   Date        Description   Amount
1    2024-08-06  Lunch         K20
```

### Summary of All Expenses
```bash
expense-tracker summary
```
**Output:**
```
[Expense Tracker]: Total expenses: K20
```

### Monthly Summary
```bash
expense-tracker summary --month 8
```
**Output:**
```
[Expense Tracker]: Total expenses for August: K20
```

### Export Expenses to CSV
```bash
expense-tracker export
```
**Output:**
```
[Expense Tracker]: Expenses have been exported to 'expenses.csv' successfully!
```

---

## 🛠️ **Technologies Used**
- **Python 3.x**
- **JSON** for data storage
- **Pandas** for CSV export
- **Tabulate** for clean table displays

---

## 📂 **Project Structure**
```
📦 expense-tracker
├── main.py          # Entry point for the CLI
├── expense.py       # Core logic for expense management
├── expenses.json    # Data storage file
├── requirements.txt # Python dependencies
└── README.md        # Documentation
```

---

## 🛡️ **Error Handling**
- Invalid inputs (e.g., negative amounts or missing descriptions) are handled gracefully.
- User confirmations are required for destructive actions like deleting expenses.
- Proper validation for commands and their parameters.

---

## 📖 **Future Enhancements**
- Add expense categories.
- Implement budget tracking and alerts.
- Support for exporting monthly reports.

---

## 🤝 **Contributing**
Feel free to fork the repository, create a new branch, and submit a pull request.

1. Fork the repo.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push your branch:
   ```bash
   git push origin feature-branch
   ```
5. Submit a pull request.

---

## 📝 **License**
This project is licensed under the **MIT License**.

---

## **Projec Challenge URL**
https://roadmap.sh/projects/expense-tracker

---

## 📬 **Contact**
- **Author:** Emmanuel Banda
- **Email:** emmanueldaliso3@gmail.com

Happy Tracking! 🎯

