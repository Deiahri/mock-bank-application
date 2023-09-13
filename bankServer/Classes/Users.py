import json, os, datetime, Accounts, Validater
from Accounts import CheckingAccount, SavingsAccount
from CreditCards import CreditCard
from params import bank_data_route


staff_auth_code = "454432"


class User:
    def __init__(self, name="", username="", password="", dob="", address="", email="", ssn=""):
        self.name = name
        self.username = username
        self.password = password
        self.dob = dob
        self.address = address
        self.email = email
        self.ssn = ssn

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        self.dob = dob

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_ssn(self):
        return self.ssn


class Customer(User):
    def __init__(self, name="", username="", password="", dob="", address="", email="", ssn="", accounts=[],
                 loans=[], credit_cards=[]):
        super(Customer, self).__init__(name, username, password, dob, address, email, ssn)
        self.accounts = accounts
        self.loans = loans
        self.credit_cards = credit_cards

    def get_accounts(self):
        return self.accounts

    def add_account(self, account):
        if type(account) is CheckingAccount or type(account) is SavingsAccount:
            if type(account) is CheckingAccount:
                self.accounts.append(account.get_checking_number())
            elif type(account) is SavingsAccount:
                self.accounts.append(account.get_savings_number())
        else:
            print(f"error: an object of type {type(account)} is neither a checking or savings account.")

    def get_loans(self):
        return self.loans

    def add_loan(self, loan):
        if not (type(loan) is loan):
            print(f"Cannot add {type(loan)} to Customer's loans")
        else:
            self.loans.append(loan.get_loan_id())

    def get_credit_cards(self):
        return self.credit_cards

    def add_credit_card(self, credit_card):
        if type(credit_card) is CreditCard:
            self.credit_cards.append(credit_card.get_card_number())
        else:
            print(f"error: object of type {type(credit_card)} is not a credit card.")


class Staff(User):
    def __init__(self, name="", username="", password="", dob="", address="", email="", ssn=""
                 , eid="", access_level=0):
        super(Staff, self).__init__(name, username, password, dob, address, email, ssn)
        self.eid = eid
        self.access_level = access_level

    def get_eid(self):
        return self.eid

    def get_access_level(self):
        return self.access_level

    def set_access_level(self, access_level):
        self.access_level = access_level


def update(user):
    if type(user) == User:
        print("You cannot save type user. You can only save type staff or customer")
    elif type(user) == Customer:
        write_customer(user)
    elif type(user) == Staff:
        write_staff(user)
    else:
        print(f"error: object not of type customer or staff, but of type {type(user)}")


def write_customer(customer):
    customer_json = {
        "name": customer.get_name(),
        "username": customer.get_username(),
        "password": customer.get_password(),
        "dob": customer.get_dob(),
        "address": customer.get_address(),
        "email": customer.get_email(),
        "ssn": customer.get_ssn(),
        "accounts": customer.get_accounts(),
        "loans": customer.get_loans(),
        "credit_cards": customer.get_credit_cards()
    }
    with open(f"{bank_data_route}/Users/Customers/{customer.get_username()}.txt", "w") as customerFile:
        json.dump(customer_json, customerFile, indent=4)


def write_staff(staff):
    staff_json = {
        "name": staff.get_name(),
        "username": staff.get_username(),
        "password": staff.get_password(),
        "dob": staff.get_dob(),
        "address": staff.get_address(),
        "email": staff.get_email(),
        "ssn": staff.get_ssn(),
        "eid": staff.get_eid(),
        "access_level": staff.get_access_level()
    }
    with open(f"{bank_data_route}/Users/Staff/{staff.get_username()}.txt", "w") as staffFile:
        json.dump(staff_json, staffFile, indent=4)


def get_user(username):
    """Returns the customer or staff object of the username passed.\n
        Returns False if customer of staff cannot be located."""
    username = username.lower()
    customers = os.listdir(f"{bank_data_route}/Users/Customers")
    for customer in customers:
        if customer[0:customer.index(".")] == username:
            with open(f"{bank_data_route}/Users/Customers/{customer}") as customer_file:
                customer_json = json.load(customer_file)
                return Customer(customer_json.get("name"), customer_json.get("username"),
                        customer_json.get("password"), customer_json.get("dob"), customer_json.get("address"),
                        customer_json.get("email"), customer_json.get("ssn"), customer_json.get("accounts"),
                        customer_json.get("loans"), customer_json.get('credit_cards'))

    staff = os.listdir(f"{bank_data_route}/Users/Staff")
    for staff_member in staff:
        if staff_member[0:staff_member.index(".txt")] == username:
            with open(f"{bank_data_route}/Users/Staff/{staff_member}") as staff_file:
                staff_json = json.load(staff_file)
                return Staff(staff_json.get("name"), staff_json.get("username"),
                             staff_json.get("password"), staff_json.get("dob"), staff_json.get("address"),
                             staff_json.get("email"), staff_json.get("ssn"), staff_json.get("eid"),
                             staff_json.get("access_level"))
    return False


def create_user(customer_json={}, user_type=""):
    name = customer_json.get("name_field").strip()
    username = customer_json.get("username_field").strip().lower()
    password = customer_json.get("password_field").strip()
    user_email = customer_json.get("email_field").strip()
    address = customer_json.get("address_field").strip()
    ssn = customer_json.get("ssn_field").replace(" ", "")

    if type(Validater.validate_name(name)) == str:
        return Validater.validate_password(password)

    if not Validater.validate_username(username):
        return "username is invalid"

    if type(Validater.validate_password(password)) == str:
        return Validater.validate_password(password)

    if not Validater.validate_email(user_email):
        return "email is invalid"

    if type(Validater.validate_address(password)) == str:
        return Validater.validate_address(password)

    if not ssn:
        return "ssn cannot be blank"
    else:
        if not Validater.validate_ssn(ssn):
            return "ssn is invalid"

    current_time = datetime.datetime.now()
    now = f"{current_time.year}/{current_time.month:02}/{current_time.day:02}"

    if user_type == "customer":
        new_user = Customer(name, username, password, "", address, user_email, ssn)

        new_checking = CheckingAccount(0, 0, now, True, username, {}, Accounts.get_available_checking_number())
        new_savings = SavingsAccount(0, 0, now, True, username, {}, Accounts.get_available_savings_number(), 3.5)

        Accounts.update(new_checking)
        Accounts.update(new_savings)
        new_user.add_account(new_checking)
        new_user.add_account(new_savings)
        update(new_user)

    elif user_type == "staff":
        authorization = customer_json.get("authorization_field")
        if not authorization == staff_auth_code:
            return "authorization code is invalid"
        new_user = Staff(name, username, password, "", address, user_email, ssn, 123456, 2)
        update(new_user)
    else:
        print("Expected a user type of either staff or customer but recieved "+user_type)
        return "Something went wrong on the server's end..."

    return new_user


def validate_and_apply_changes(username="", change_data={}):
    new_password = change_data.get("new_password_field").strip()
    new_email = change_data.get("email_field").strip()
    new_name = change_data.get("name_field").strip()
    new_address = change_data.get("address_field").strip()
    old_password = change_data.get("old_password_field").strip()

    user = get_user(username)

    made_changes = False

    if user.get_password() != old_password:
        return "Old password is not correct"

    if new_password:
        if type(Validater.validate_password(new_password)) == str:
            return Validater.validate_password(new_password)
        else:
            user.set_password(new_password)
            made_changes = True

    if new_email:
        if not Validater.validate_email(new_email):
            return "email is invalid"
        else:
            user.set_email(new_email)
            made_changes = True

    if new_name:
        if type(Validater.validate_name(new_name)) == str:
            return Validater.validate_name(new_name)
        else:
            user.set_name(new_name)
            made_changes = True

    if new_address:
        if type(Validater.validate_address(new_address)) == str:
            return Validater.validate_address(new_address)
        else:
            user.set_address(new_address)
            made_changes = True

    update(user)
    if made_changes:
        return "Successfully applied changes"
    else:
        return "No changes applied"


def apply_staff_change(sent_data={}, staff_user=""):
    account_type = sent_data.get("account_field")
    to_user = sent_data.get("to_field")
    reason = sent_data.get("reason_field")
    amount = sent_data.get("amount_field")

    try:
        float(amount)
    except Exception:
        return "Amount is invalid"

    amount = float(amount)

    if account_type == "Checking":
        account = Accounts.get_user_checking(to_user)
    elif account_type == "Savings":
        account = Accounts.get_user_savings(to_user)

    if not reason:
        reason = f"Gift from staff user {staff_user}"

    account.submit_transaction(amount, reason)
    Accounts.update(account)
    return "Successfully applied transaction"


def list_customers():
    customer_files = os.listdir(f"{bank_data_route}/Users/Customers")
    customer_list = []
    for current_file in customer_files:
        if current_file.__contains__("."):
            customer_list.append(current_file[0:current_file.index(".")])
        else:
            pass
    return customer_list
