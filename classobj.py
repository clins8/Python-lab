class Bank_Account:
    def __init__(self):
        self.balance = 0
        self.acno = ""
        self.name = ""
        print("Deposit & Withdrawal Operations of a Bank")

    def accinfo(self):
        self.acno = int(input("Enter account number: "))
        self.name = input("Enter Name: ")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        if amount > 0:
            self.balance += amount
            print("\nAmount Deposited:", amount)
            return True  # Return True to indicate successful deposit
        else:
            print("\nInvalid input! Please enter a positive number or an amount greater than 0.")
            return False

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdraw:", amount)
        else:
            print("\nInsufficient balance!")

    def display(self):
        print("\n")
        print(f"\nAccount number: {self.acno}")
        print(f"Account Holder: {self.name}")
        print(f"Net Available Balance: {self.balance}")
        print("\n")

    def menu(self):
        while True:
            print("\nChoose an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Display Account Information")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                if self.deposit():  # Deposit only if successful
                    print("Deposit completed successfully.")
            elif choice == 2:
                self.withdraw()
            elif choice == 3:
                self.display()
            elif choice == 4:
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice! Please enter a valid option.")

# Driver code
account = Bank_Account()
account.accinfo()
account.menu()
