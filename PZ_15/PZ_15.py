import sqlite3
from datetime import datetime
import os

def create_sample_database(db_name='expenses.db'):
    """Creates a database with sample records"""
    if os.path.exists(db_name):
        return  # Database already exists
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            product_code TEXT NOT NULL,
            product_name TEXT NOT NULL,
            expense_type TEXT NOT NULL,
            amount REAL NOT NULL
        )
    ''')
    
    # Add sample data
    sample_data = [
        ('2023-01-10', 'P001', 'Smartphone X', 'Materials', 150000),
        ('2023-01-12', 'P001', 'Smartphone X', 'Salary', 50000),
        ('2023-01-15', 'P002', 'Laptop Pro', 'Components', 220000),
        ('2023-01-18', 'P002', 'Laptop Pro', 'Logistics', 15000),
        ('2023-02-05', 'P003', 'Tablet Mini', 'Materials', 80000),
        ('2023-02-10', 'P001', 'Smartphone X', 'Marketing', 30000),
        ('2023-02-15', 'P003', 'Tablet Mini', 'Salary', 35000),
        ('2023-02-20', 'P004', 'Headphones Pro', 'Components', 45000),
        ('2023-03-01', 'P002', 'Laptop Pro', 'Marketing', 40000),
        ('2023-03-05', 'P004', 'Headphones Pro', 'Logistics', 8000)
    ]
    
    cursor.executemany('''
        INSERT INTO expenses (date, product_code, product_name, expense_type, amount)
        VALUES (?, ?, ?, ?, ?)
    ''', sample_data)
    
    conn.commit()
    conn.close()

class ExpenseTracker:
    def __init__(self, db_name='expenses.db'):
        """Initializes the expense tracker"""
        create_sample_database(db_name)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def add_expense(self, date, product_code, product_name, expense_type, amount):
        """Adds a new expense record"""
        try:
            # Date format validation
            datetime.strptime(date, '%Y-%m-%d')
            
            # Amount validation
            if amount <= 0:
                raise ValueError("Amount must be positive")
                
            self.cursor.execute('''
                INSERT INTO expenses (date, product_code, product_name, expense_type, amount)
                VALUES (?, ?, ?, ?, ?)
            ''', (date, product_code, product_name, expense_type, amount))
            self.conn.commit()
            return True, "Expense record added successfully!"
        except ValueError as e:
            return False, f"Validation error: {e}"
        except sqlite3.Error as e:
            return False, f"Database error: {e}"
    
    def get_all_expenses(self):
        """Gets all expense records"""
        try:
            self.cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    
    def get_expenses_by_product(self, product_code):
        """Gets expenses by product code"""
        try:
            self.cursor.execute('''
                SELECT * FROM expenses 
                WHERE product_code = ? 
                ORDER BY date DESC
            ''', (product_code,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    
    def get_total_expenses_for_period(self, start_date, end_date):
        """Gets total expenses for a period"""
        try:
            # Date validation and normalization
            start_date = self._validate_date(start_date)
            end_date = self._validate_date(end_date)
            
            if not start_date or not end_date:
                return 0, "Invalid date format. Use YYYY-MM-DD"
            
            if start_date > end_date:
                start_date, end_date = end_date, start_date
            
            self.cursor.execute('''
                SELECT SUM(amount) FROM expenses 
                WHERE date BETWEEN ? AND ?
            ''', (start_date, end_date))
            
            result = self.cursor.fetchone()
            total_amount = result[0] if result[0] is not None else 0
            return total_amount, f"Total expenses from {start_date} to {end_date}"
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return 0, "Error calculating total expenses"
    
    def _validate_date(self, date_string):
        """Validates and normalizes date"""
        try:
            date_string = date_string.strip().replace(' ', '-')
            date_obj = datetime.strptime(date_string, '%Y-%m-%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            return None
    
    def close(self):
        """Closes the database connection"""
        try:
            self.conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Connection closing error: {e}")
            return False

def display_expenses(expenses_list, title=None):
    """Displays a list of expenses"""
    if not expenses_list:
        print("No expenses found")
        return
        
    if title:
        print(f"\n{title}:")
    
    headers = ["ID", "Date", "Code", "Product", "Expense Type", "Amount"]
    print("{:<4} {:<12} {:<8} {:<15} {:<15} {:<10}".format(*headers))
    print("-" * 70)
    
    for expense in expenses_list:
        print("{:<4} {:<12} {:<8} {:<15} {:<15} {:<10.2f}".format(
            expense[0], expense[1], expense[2], expense[3], expense[4], expense[5]))

def main_menu():
    """Displays the main menu"""
    print("\nPRODUCT EXPENSE TRACKER")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. View expenses by product")
    print("4. View total expenses for period")
    print("5. Exit")
    
    while True:
        user_choice = input("Select action (1-5): ").strip()
        if user_choice in ('1', '2', '3', '4', '5'):
            return user_choice
        print("Invalid input. Please enter a number between 1 and 5.")

def get_valid_input(prompt, validator=None):
    """Gets and validates user input"""
    while True:
        try:
            user_input = input(prompt).strip()
            if validator:
                validated = validator(user_input)
                if validated is not None:
                    return validated
            else:
                return user_input
        except (ValueError, Exception) as e:
            print(f"Error: {e}")

def validate_date(date_input):
    """Validates date"""
    try:
        date_input = date_input.replace(' ', '-')
        datetime.strptime(date_input, '%Y-%m-%d')
        return date_input
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

def validate_amount(amount_input):
    """Validates amount"""
    try:
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return amount
    except ValueError:
        raise ValueError("Invalid amount. Must be a positive number")

def main():
    """Main program function"""
    tracker = ExpenseTracker()
    
    try:
        while True:
            choice = main_menu()
            
            if choice == '1':
                print("\nADD NEW EXPENSE")
                date = get_valid_input("Enter date (YYYY-MM-DD): ", validate_date)
                code = get_valid_input("Enter product code: ")
                name = get_valid_input("Enter product name: ")
                expense_type = get_valid_input("Enter expense type: ")
                amount = get_valid_input("Enter amount: ", validate_amount)
                
                success, message = tracker.add_expense(date, code, name, expense_type, amount)
                print(message)
            
            elif choice == '2':
                expenses = tracker.get_all_expenses()
                display_expenses(expenses, "ALL EXPENSES")
            
            elif choice == '3':
                code = input("Enter product code: ").strip()
                expenses = tracker.get_expenses_by_product(code)
                display_expenses(expenses, f"EXPENSES FOR PRODUCT {code}")
            
            elif choice == '4':
                print("\nTOTAL EXPENSES FOR PERIOD")
                start = get_valid_input("Enter start date (YYYY-MM-DD): ", validate_date)
                end = get_valid_input("Enter end date (YYYY-MM-DD): ", validate_date)
                
                total, message = tracker.get_total_expenses_for_period(start, end)
                print(f"\n{message}: {total:.2f}")
            
            elif choice == '5':
                tracker.close()
                print("Goodbye!")
                break
            
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        tracker.close()

if __name__ == "__main__":
    main()