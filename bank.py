accounts = {}
account_number = 1001

def authenticate(acc_no):
    """Authenticate user using password."""
    if acc_no not in accounts:
        print("Account does not exist.")
        return False
    password = input("Enter your password: ")
    if password == accounts[acc_no]['password']:
        return True
    else:
        print("Incorrect password.")
        return False

while True:
    print("\n------ WELCOME TO BANK OF MAHARASHTRA ------")
    print("1. Create New Account")
    print("2. Add Amount")
    print("3. Withdraw Amount")
    print("4. Check Balance")
    print("5. View Account Details")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        print("\n--- Create Account ---")
        name = input("Enter your name: ")
        try:
            age = int(input("Enter your age: "))
            password = input("Set a password for your account: ")
            accounts[account_number] = {
                'name': name,
                'age': age,
                'balance': 5000,  # default balance
                'password': password
            }
            print(f"Account created successfully! Your account number is: {account_number}")
            account_number += 1
        except ValueError:
            print("Invalid age entered.")

    elif choice == 2:
        print("\n--- Add Amount ---")
        try:
            acc_no = int(input("Enter your account number: "))
            if authenticate(acc_no):
                amount = int(input("Enter amount to add: "))
                accounts[acc_no]['balance'] += amount
                print(f"₹{amount} added successfully. New balance: ₹{accounts[acc_no]['balance']}")
        except ValueError:
            print("Invalid input.")

    elif choice == 3:
        print("\n--- Withdraw Amount ---")
        try:
            acc_no = int(input("Enter your account number: "))
            if authenticate(acc_no):
                amount = int(input("Enter amount to withdraw: "))
                if amount <= accounts[acc_no]['balance']:
                    accounts[acc_no]['balance'] -= amount
                    print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{accounts[acc_no]['balance']}")
                else:
                    print("Insufficient balance.")
        except ValueError:
            print("Invalid input.")

    elif choice == 4:
        print("\n--- Check Balance ---")
        try:
            acc_no = int(input("Enter your account number: "))
            if authenticate(acc_no):
                print(f"Current balance: ₹{accounts[acc_no]['balance']}")
        except ValueError:
            print("Invalid input.")

    elif choice == 5:
        print("\n--- View Account Details ---")
        try:
            acc_no = int(input("Enter your account number: "))
            if authenticate(acc_no):
                acc = accounts[acc_no]
                print(f"\nACCOUNT NUMBER: {acc_no}")
                print(f"NAME         : {acc['name']}")
                print(f"AGE          : {acc['age']}")
                print(f"BALANCE      : ₹{acc['balance']}")
        except ValueError:
            print("Invalid input.")

    elif choice == 6:
        print("Thank you for using Bank of Maharashtra. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")
