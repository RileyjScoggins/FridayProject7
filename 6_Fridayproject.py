class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Account number for the bank account
        self.balance = balance  # Initial balance, defaults to 0

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Please enter a positive amount to deposit.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        elif amount <= 0:
            print("Please enter a positive amount to withdraw.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        """Check the current balance of the account."""
        print(f"Your current balance is: ${self.balance:.2f}")

# Create an account with a sample account number and initial balance
account = BankAccount(account_number="12345678")

# Main program loop
print("Welcome to the Bank Account Manager!")

while True:
    # Ask for the account number each time to simulate verification
    entered_account = input("\nPlease enter your account number: ").strip()
    
    if entered_account == account.account_number:
        print("\nWhat would you like to do?")
        print("a) Deposit Money")
        print("b) Withdraw Money")
        print("c) Check Balance")
        print("d) Exit")

        # Get user choice
        choice = input("Choose an option (a/b/c/d): ").strip().lower()

        if choice == "a":
            try:
                amount = float(input("Enter the amount to deposit: $"))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        elif choice == "b":
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        elif choice == "c":
            account.check_balance()
        
        elif choice == "d":
            print("Thank you for using the Bank Account Manager. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")
    
    else:
        print("Account number not recognized. Please try again.")