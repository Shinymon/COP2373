"""
This program defines a BankAcct class that simulates a basic bank account
and allows a user to interactively:
- Create an account
- Deposit and withdraw money
- Adjust the interest rate
- View current balance
- Calculate interest based on number of days

Account info is displayed using the __str__ method.
"""

class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate  # annual interest rate in %

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            print(f"Deposited ${amount:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= amount
            print(f"Withdrew ${amount:.2f}.")

    def adjust_interest_rate(self, new_rate):
        if new_rate >= 0:
            self.interest_rate = new_rate
            print(f"Interest rate updated to {new_rate}%.")
        else:
            print("Interest rate cannot be negative.")

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        daily_rate = self.interest_rate / 100 / 365
        interest = self.amount * daily_rate * days
        return interest

    def __str__(self):
        return (f"\n--- Account Summary ---\n"
                f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2f}%\n")

def test_bank_acct():
    print("Welcome to ChatGPT Bank!")
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")
    while True:
        try:
            initial_amount = float(input("Enter initial deposit amount: "))
            if initial_amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative number.")
    while True:
        try:
            interest_rate = float(input("Enter annual interest rate: "))
            if interest_rate < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative number.")

    acct = BankAcct(name, account_number, initial_amount, interest_rate)
    print(acct)

    while True:
        print("\nChoose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Adjust Interest Rate")
        print("4. Show Balance")
        print("5. Calculate Interest")
        print("6. Show Account Info")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                amount = float(input("Enter deposit amount: "))
                acct.deposit(amount)
            except ValueError:
                print("Invalid input.")
        elif choice == '2':
            try:
                amount = float(input("Enter withdrawal amount: "))
                acct.withdraw(amount)
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            try:
                new_rate = float(input("Enter new interest rate: "))
                acct.adjust_interest_rate(new_rate)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            print(f"Current balance: ${acct.get_balance():.2f}")
        elif choice == '5':
            try:
                days = int(input("Enter number of days: "))
                interest = acct.calculate_interest(days)
                print(f"Interest for {days} day(s): ${interest:.2f}")
            except ValueError:
                print("Invalid number of days.")
        elif choice == '6':
            print(acct)
        elif choice == '0':
            print("Thank you for banking with us! Goodbye.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    test_bank_acct()