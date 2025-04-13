import json

class User:
    def __init__(self, user_id, name, password, phone, email, gender, age, city, balance=0):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.phone = phone
        self.email = email
        self.gender = gender
        self.age = age
        self.city = city
        self.balance = balance

    def to_dict(self):
        return {
            "ID": self.user_id,
            "Name": self.name,
            "Password": self.password,
            "Phone number": self.phone,
            "Mail": self.email,
            "Gender": self.gender,
            "Age": self.age,
            "City": self.city,
            "Balance": self.balance
        }

class BankAccount:
    def __init__(self, user):
        self.user = user

    def deposit(self, amount, currency, currency_rates):
        if currency in currency_rates:
            amount *= currency_rates[currency]
            self.user.balance += amount
            return True, amount
        return False, 0

    def withdraw(self, amount, currency, currency_rates):
        if currency in currency_rates:
            amount *= currency_rates[currency]
            if amount <= self.user.balance:
                self.user.balance -= amount
                return True, amount
        return False, 0

    def transfer(self, amount, recipient):
        if amount <= self.user.balance:
            self.user.balance -= amount
            recipient.balance += amount
            return True
        return False

class Transaction:
    @staticmethod
    def log_transaction(user_id, transaction_type, amount, currency, from_user=None, to_user=None):
        transaction = {
            "UserID": user_id,
            "Type": transaction_type,
            "Amount": amount,
            "Currency": currency
        }

        if to_user is not None:
            transaction["To ID"] = to_user
        with open("transactions_log.json", "a") as log_file:
            json.dump(transaction, log_file)
            log_file.write("\n")

# Function to load data from JSON file
def load_data():
    with open("Project_1_json.json", "r") as file:
        return [User(user_id=user['ID'], name=user['Name'], password=user['Password'], phone=user['Phone number'],
                    email=user['Mail'], gender=user['Gender'], age=user['Age'], city=user['City'], balance=user['Balance'])
                for user in json.load(file)]

# Function to save data to JSON file
def save_data(users):
    with open("Project_1_json.json", "w") as file:
        json.dump([user.to_dict() for user in users], file, indent=2)

# Load users
database = load_data()

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

# Function to validate name
def is_valid_name(name):
    return name.isalpha()

# Function to validate password
def is_valid_password(password):
    return len(password) >= 8

# Function to validate phone number
def is_valid_phone_number(phone):
    return len(str(phone)) >= 11

repeat = True
while repeat:
    print('\n', '*'*5, "Welcome to SIC Bank Management System", '*'*5, '\n')
    print("To create a new account, please type [register]")
    print("To access your existing account, please type [login]")
    print("To access admin panel, please type [admin]", '\n')

    user_sign = input('Enter : ').lower().strip()

    # login
    if user_sign == 'login':
        print('*'*20, "Login Page", '*'*20)

        user_logined_id = get_int_input('Please enter your User ID: ')
        user_logined_ps = input('Please enter your Password: ').strip()

        user = next((u for u in database if u.user_id == user_logined_id and u.password == user_logined_ps), None)

        if user:
            repeat = False
            print(f'Welcome back, {user.name}!')
            account = BankAccount(user)
        else:
            print("Incorrect User ID or Password. Please try again.")

    # register
    elif user_sign == 'register':
        print('*' * 20, "Registration Page", '*' * 20)

        while True:
            user_signed_name = input('Enter your full name: ').strip().capitalize()
            if not is_valid_name(user_signed_name):
                print("Invalid name. Please enter alphabetic characters only.")
                continue

            user_signed_ps = input('Create a password: ').strip()
            if not is_valid_password(user_signed_ps):
                print("Password must be at least 8 characters long.")
                continue

            user_signed_num = get_int_input('Enter your phone number: ')
            if not is_valid_phone_number(user_signed_num):
                print("Phone number must be at least 11 digits long.")
                continue

            user_signed_mail = input('Enter your email address: ').strip()
            user_signed_gender = input('Enter your gender: ').strip().capitalize()
            user_signed_age = get_int_input('Enter your age: ')
            user_signed_city = input('Enter your city of residence: ').strip().capitalize()

            new_ID = database[-1].user_id + 1 if database else 1
            new_user = User(new_ID, user_signed_name, user_signed_ps, user_signed_num, user_signed_mail, user_signed_gender, user_signed_age, user_signed_city)

            database.append(new_user)
            save_data(database)

            print(f'Registration successful! Your User ID is {new_ID}. You are now logged in.')
            account = BankAccount(new_user)
            repeat = False
            break

    # admin
    elif user_sign == 'admin':
        print('*' * 20, "Admin Panel", '*' * 20)
        try:
            with open("transactions_log.json", "r") as log_file:
                transactions = log_file.readlines()
                if transactions:
                    print("Transaction Log:")
                    for transaction in transactions:
                        print(transaction.strip())
                else:
                    print("No transactions found.")
        except FileNotFoundError:
            print("Transaction log file not found.")

    else:
        print("Invalid option. Please type [register], [login], or [admin].")

# menu
while True:
    print("Please select an option from the menu below:")
    print('[0] Deposit Funds')
    print('[1] Withdraw Funds')
    print('[2] Transfer Funds')
    print('[3] View Account Details')
    print('[4] Exit')

    user_op_num = get_int_input('Enter the number corresponding to your choice: ')

    # deposit
    if user_op_num == 0:
        print(f"Your current balance is {account.user.balance} EGP.")
        user_deposite = get_float_input('Enter the amount you wish to deposit: ')
        currency = input('Enter the currency type (e.g., EGP): ').strip().upper()

        currency_rates = {"USD": 30, "SAR": 9, "EGP": 1}

        success, amount = account.deposit(user_deposite, currency, currency_rates)
        if success:
            save_data(database)
            Transaction.log_transaction(account.user.user_id, "Deposit", amount, currency)
            print(f"Deposit successful! Your new balance is {account.user.balance} EGP.")
        else:
            print("Invalid currency entered. Please try again.")

    # withdraw
    elif user_op_num == 1:
        print(f"Your current balance is {account.user.balance} EGP.")
        user_withdraw = get_float_input('Enter the amount you wish to withdraw: ')
        currency = input('Enter the currency type (e.g., EGP): ').strip().upper()

        currency_rates = {"USD": 30, "SAR": 9, "EGP": 1}

        success, amount = account.withdraw(user_withdraw, currency, currency_rates)
        if success:
            save_data(database)
            Transaction.log_transaction(account.user.user_id, "Withdraw", amount, currency)
            print(f"Withdrawal successful! Your new balance is {account.user.balance} EGP.")
        else:
            print("Invalid currency entered or insufficient funds. Please try again.")

    # transfer
    elif user_op_num == 2:
        print(f"Your current balance is {account.user.balance} EGP.")
        user_amount = get_float_input("Enter the amount you wish to transfer in EGP: ")
        user_id = get_int_input("Enter the User ID of the recipient: ")

        recipient = next((u for u in database if u.user_id == user_id), None)

        if recipient:
            success = account.transfer(user_amount, recipient)
            if success:
                save_data(database)
                Transaction.log_transaction(account.user.user_id, "Transfer", user_amount, "EGP", from_user=account.user.user_id, to_user=recipient.user_id)
                print(f"Transfer successful! Your new balance is {account.user.balance} EGP.")
            else:
                print("Insufficient funds for this transfer. Please try again.")
        else:
            print("Recipient not found. Please check the User ID and try again.")

    # info
    elif user_op_num == 3:
        print("Here are your account details:")
        for key, value in account.user.to_dict().items():
            print(f"{key}: {value}")

    # exit
    elif user_op_num == 4:
        print("Thank you for using the Bank Management System. Goodbye!")
        break

    else:
        print("Invalid selection. Please choose a valid option from the menu.")
        