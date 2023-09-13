import json

from params import bank_data_route


class Loan:
    """**Contains loan information**\n
    loan_id: loan's id\n
    period: length of time until interest is charged again (seven days, weekly, monthly, yearly, etc.)\n
    length: length of time until all of the loan should be paid off\n
    principle: amount of money loaned\n
    interest_rate: rate of interest on loan\n
    amount_repaid: amount of money repaid\n
    amount_remaining: amount of money left to be repaid\n
    defaulted: True if loan is defaulted, False otherwise\n
    enabled: True if loan is active
    """
    def __init__(self, user, loan_id, period, length, principle, interest_rate, amount_repaid, amount_remaining,
                 defaulted, enabled):
        self.user = user
        self.loan_id = loan_id
        self.period = period
        self.length = length
        self.principle = float(principle)
        self.interest_rate = float(interest_rate)
        self.amount_repaid = float(amount_repaid)
        self.amount_remaining = float(amount_remaining)
        self.defaulted = defaulted
        self.enabled = enabled

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_loan_id(self):
        return self.loan_id

    def get_period(self):
        return self.period

    def set_period(self, period):
        self.period = period

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_principle(self):
        return self.principle

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def get_amount_repaid(self):
        return self.amount_repaid

    def set_amount_repaid(self, amount_repaid):
        self.amount_repaid = amount_repaid

    def get_amount_remaining(self):
        return self.amount_remaining

    def set_amount_remaining(self, amount_remaining):
        self.amount_remaining = amount_remaining

    def get_defaulted(self):
        return self.defaulted

    def toggle_defaulted(self):
        self.defaulted = not self.defaulted

    def get_enabled(self):
        return self.enabled

    def toggle_enabled(self):
        self.enabled = not self.enabled

    def apply_interest(self):
        self.amount_remaining *= self.interest_rate/100


def update(loan):
    if not (type(loan) is Loan):
        print(f"error: object passed is of type {type(loan)}, not Loan")
    else:
        loan_json = {
            "user": loan.get_user(),
            "loan_id": loan.get_loan_id(),
            "period": loan.get_period(),
            "length": loan.get_length(),
            "principle": loan.get_principle(),
            "interest_rate": loan.get_interest_rate(),
            "amount_repaid": loan.get_amount_repaid(),
            "amount_remaining": loan.get_amount_remaining(),
            "defaulted": loan.get_defaulted(),
            "enabled": loan.get_enabled(),
        }
        with open(f"{bank_data_route}/Loan/{loan.get_loan_id()}.txt", "w") as loan_file:
            json.dump(loan_json, loan_file, indent=4)

