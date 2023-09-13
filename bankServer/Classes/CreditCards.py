import json
from params import bank_data_route


class CreditCard:
    def __init__(self, card_number, security_code, credit_limit, credit_used, enabled,
                 interest_rate, bonus_category, bonus_category_category_cash_back_rate,
                 regular_cash_back_rate, cash_back):
        self.card_number = card_number
        self.security_code = security_code
        self.credit_limit = credit_limit
        self.credit_used = credit_used
        self.enabled = enabled
        self.interest_rate = interest_rate
        self.bonus_category = bonus_category
        self.bonus_category_cash_back_rate = bonus_category_category_cash_back_rate
        self.regular_cash_back_rate = regular_cash_back_rate
        self.cash_back = cash_back

    def get_card_number(self):
        return self.card_number

    def get_security_code(self):
        return self.security_code

    def get_credit_limit(self):
        return self.credit_limit

    def set_credit_limit(self, credit_limit):
        self.credit_limit = credit_limit

    def get_credit_used(self):
        return self.credit_used

    def set_credit_used(self, credit_used):
        self.credit_used = credit_used

    def get_enabled(self):
        return self.enabled

    def toggle_enabled(self):
        self.enabled = True

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.credit_used = self.credit_used * self.interest_rate

    def get_bonus_category(self):
        return self.bonus_category

    def get_bonus_category_category_cash_back_rate(self):
        return self.bonus_category_cash_back_rate

    def get_regular_cash_back_rate(self):
        return self.regular_cash_back_rate

    def get_cash_back(self):
        return self.cash_back


def update(card):
    if not (type(card) is CreditCard):
        print(f"{type(card)} is not a CreditCard object.")
    else:
        credit_card_json = {
            "card_number": card.get_card_number(),
            "security_code": card.get_security_code(),
            "credit_limit": card.get_credit_limit(),
            "credit_used": card.get_credit_used(),
            "enabled": card.get_enabled(),
            "interest_rate": card.get_interest_rate(),
            "bonus_category": card.get_bonus_category(),
            "bonus_category_category_cash_back_rate": card.get_bonus_category_category_cash_back_rate(),
            "regular_cash_back_rate": card.get_regular_cash_back_rate(),
            "cash_back": card.get_cash_back()
        }
        with open(f"{bank_data_route}/CreditCards/{card.get_card_number()}.txt", "w") as credit_card_file:
            json.dump(credit_card_json, credit_card_file, indent=4)


