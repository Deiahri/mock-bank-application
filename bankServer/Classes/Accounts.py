import json, os, datetime
import time

from params import bank_data_route


# routing number will always be equal to 985847372
class Account:
    def __init__(self, balance=0, routing_number=985847372, open_date="", enabled=True, user="", transaction_history={}):
        self.balance = balance
        self.routing_number = 985847372
        self.open_date = open_date
        self.enabled = enabled
        self.user = user
        self.transaction_history = transaction_history

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def submit_transaction(self, amount, reason):
        amount = float(amount)
        self.balance = self.balance + amount
        current_time = datetime.datetime.now()
        transaction_time = f"{current_time.year}-{current_time.month}-{current_time.day} " \
                           f"{current_time.hour}:{current_time.minute:02}.{current_time.second}"
        self.transaction_history[transaction_time] = f"${amount:.2f} | {reason}"

    def get_routing_number(self):
        return self.routing_number

    def get_open_date(self):
        return self.open_date

    def get_enabled(self):
        return self.enabled

    def get_user(self):
        return self.user

    def get_transaction_history(self):
        return self.transaction_history

    def toggle_enabled(self):
        self.enabled = not self.enabled
        return self.enabled


class CheckingAccount(Account):
    def __init__(self, balance=0, routing_number=985847372, open_date="", enabled=True, user="", transaction_history={},
                 checking_number=""):
        super(CheckingAccount, self).__init__(balance, routing_number, open_date, enabled, user, transaction_history)
        self.checking_number = checking_number

    def get_checking_number(self):
        return self.checking_number


class SavingsAccount(Account):
    def __init__(self, balance=0, routing_number=985847372, open_date="",
                 enabled=True, user="", transaction_history={}, savings_number="", interest_rate=0.0):
        super(SavingsAccount, self).__init__(balance, routing_number, open_date, enabled, user, transaction_history)
        self.savings_number = savings_number
        self.interest_rate = interest_rate

    def get_savings_number(self):
        return self.savings_number

    def get_interest_rate(self):
        return self.interest_rate


def update(account):
    if type(account) == Account:
        print("cannot update Account. Can only update CheckingAccount and SavingsAccount")
    elif type(account) == CheckingAccount:
        update_checking_account(account)
    elif type(account) == SavingsAccount:
        update_savings_account(account)
    else:
        print(f"information passed is of type {type(account)} and is not a valid account type")


def update_checking_account(checking_account):
    checking_account_json = {
        "balance": checking_account.get_balance(),
        "routing_number": checking_account.get_routing_number(),
        "open_date": checking_account.get_open_date(),
        "enabled": checking_account.get_enabled(),
        "user": checking_account.get_user(),
        "transaction_history": checking_account.get_transaction_history(),
        "checking_number": checking_account.get_checking_number()
    }
    with open(f"{bank_data_route}/Accounts/CheckingAccounts/{checking_account.get_checking_number()}.txt", "w") as file:
        json.dump(checking_account_json, file, indent=4)


def update_savings_account(savings_account):
    savings_account_json = {
        "balance": savings_account.get_balance(),
        "routing_number": savings_account.get_routing_number(),
        "open_date": savings_account.get_open_date(),
        "enabled": savings_account.get_enabled(),
        "user": savings_account.get_user(),
        "transaction_history": savings_account.get_transaction_history(),
        "savings_number": savings_account.get_savings_number(),
        "interest_rate": savings_account.get_interest_rate()
    }
    with open(f"{bank_data_route}/Accounts/SavingsAccounts/{savings_account.get_savings_number()}.txt", "w") \
            as savings_account_file:
        json.dump(savings_account_json, savings_account_file, indent=4)


def get_account(account_number):
    first_number = int(account_number[0])
    if first_number == 1 or first_number == 2 or first_number == 3 or first_number == 4:
        return get_checking_account(account_number)
    elif first_number == 5 or first_number == 6 or first_number == 7 or first_number == 8:
        return get_savings_account()


def get_checking_account(account_number):
    try:
        with open(f"{bank_data_route}/Accounts/CheckingAccounts/{account_number}.txt", "r") as account_file:
            account_json = json.load(account_file)
            balance = account_json.get("balance")
            open_date = account_json.get("open_date")
            enabled = bool(account_json.get("enabled"))
            user = account_json.get("user")
            transaction_history = account_json.get("transaction_history")
            return CheckingAccount(balance, 0, open_date, enabled, user, transaction_history, account_number)
    except Exception:
        return None


def get_savings_account(account_number):
    try:
        with open(f"{bank_data_route}/Accounts/SavingsAccounts/{account_number}.txt", "r") as account_file:
            account_json = json.load(account_file)
            balance = account_json.get("balance")
            open_date = account_json.get("open_date")
            enabled = bool(account_json.get("enabled"))
            user = account_json.get("user")
            transaction_history = account_json.get("transaction_history")
            interest_rate = float(account_json.get("interest_rate"))
            return SavingsAccount(balance, 0, open_date, enabled, user, transaction_history,
                                  account_number, interest_rate)
    except Exception:
        return None


def get_available_checking_number():
    checking_account_files = os.listdir(f"{bank_data_route}/Accounts/CheckingAccounts")
    last_valid = ""
    for file_name in checking_account_files:
        file_name_no_extension = ""
        if file_name.__contains__("."):
            file_name_no_extension = file_name[0:file_name.index(".")]
        else:
            print(f"{file_name} does not have a file extension")
            pass
        first_digit = int(file_name[0])
        if first_digit == 1 or first_digit == 2 or first_digit == 3 or first_digit == 4:
            if len(file_name_no_extension) == 16:
                last_valid = file_name_no_extension

    if not last_valid:
        name = "1000000000000000"
    else:
        name = f"{int(last_valid) + 1}"

    return name


def get_available_savings_number():
    savings_account_files = os.listdir(f"{bank_data_route}/Accounts/SavingsAccounts")
    last_valid = ""
    for file_name in savings_account_files:
        file_name_no_extension = ""
        if file_name.__contains__("."):
            file_name_no_extension = file_name[0:file_name.index(".")]
        else:
            print(f"{file_name} does not have a file extension")
        first_digit = int(file_name[0])

        # savings accounts are 16 digits, and begin with either 5, 6, 7, or 8.
        if first_digit == 5 or first_digit == 6 or first_digit == 7 or first_digit == 8:
            if len(file_name_no_extension) == 16:
                last_valid = file_name_no_extension

    if not last_valid:
        name = "5000000000000000"
    else:
        name = f"{int(last_valid) + 1}"

    return name


def get_user_checking(username):
    user_json = load_user_json(username.lower())
    if not user_json:
        return "No Checkings"

    if not user_json.__contains__("accounts"):
        return "No Checkings"
    else:
        accounts = user_json.get("accounts")

    for account_number in accounts:
        if len(account_number) == 16:
            first_digit = account_number[0]
            if first_digit == "1" or first_digit == "2" or first_digit == "3" or first_digit == "4":
                return get_checking_account(account_number)
            elif first_digit == "5" or first_digit == "6" or first_digit == "7" or first_digit == "8":
                continue
            else:
                continue
    return "No Savings Account"


def get_user_savings(username):
    user_json = load_user_json(username.lower())
    if not user_json:
        return "No Savings"

    if not user_json.__contains__("accounts"):
        return "No Savings"
    else:
        accounts = user_json.get("accounts")

    for account_number in accounts:
        if len(account_number) == 16:
            first_digit = account_number[0]
            if first_digit == "1" or first_digit == "2" or first_digit == "3" or first_digit == "4":
                continue
            elif first_digit == "5" or first_digit == "6" or first_digit == "7" or first_digit == "8":
                return get_savings_account(account_number)
            else:
                continue
    return "No Savings Account"


def process_transfer(sent_data={}):
    username = sent_data.get("username")
    from_account_field = sent_data.get("from_field")
    to_account_field = sent_data.get("to_field")
    to_user_field = sent_data.get("username_field")
    amount_field = sent_data.get("amount_field").strip()
    reason_field = sent_data.get("reason_field").strip()

    if from_account_field == to_account_field:
        return "Error: Cannot send from and to the same account"
    elif not amount_field:
        return "Amount cannot be empty"

    from_account_type = ""
    to_account_type = ""

    from_account = ""
    to_account = ""
    if from_account_field.__contains__("Checking account"):
        from_account = get_user_checking(username)
        from_account_type = "checking"
    else:
        from_account = get_user_savings(username)
        from_account_type = "savings"

    if to_account_field.__contains__("Checking account"):
        to_account = get_user_checking(username)
        to_account_type = "checking"
    elif to_account_field.__contains__("Savings account"):
        to_account = get_user_savings(username)
        to_account_type = "savings"

    if not to_account:
        if not to_user_field:
            return "Username field cannot be blank if sending to a user."
        else:
            if to_account_field == "User checking":
                to_account = get_user_checking(to_user_field)
                to_account_type = "checking"
            elif to_account_field == "User savings":
                to_account = get_user_savings(to_user_field)
                to_account_type = "savings"

    if type(from_account) == str:
        return f"You do not have a {from_account_type} account"
    if type(to_account) == str:
        return f"{to_user_field} does not have a {from_account_type} account"

    amount = float(amount_field).__round__(2)
    from_account.submit_transaction(-amount, f"paid to {to_user_field}'s {to_account_type}")
    if not reason_field:
        reason_field = "No reason specified"
    to_account.submit_transaction(amount, reason_field)
    update(from_account)
    update(to_account)
    return True


def load_user_json(username):
    username = username.lower()
    try:
        with open(f"{bank_data_route}/Users/Customers/{username}.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None


