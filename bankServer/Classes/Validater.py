import os
from params import bank_data_route


def validate_ssn(ssn):
    ssn_split = ssn.split("-")
    if len(ssn_split) == 1:
        if len(ssn) == 9:
            try:
                int(ssn)
            except Exception:
                return False
        else:
            return False
    else:
        if len(ssn_split) == 3:
            total_len = 0
            for ssn_chunk in ssn_split:
                total_len += len(ssn_chunk)
                try:
                    int(ssn_split[0])
                except Exception:
                    return False
            if not total_len == 9:
                return False
        else:
            return False
    return True


def validate_email(email_address):
    state = 0
    valid = True
    invalid_reason = "email"
    for email_char in email_address:
        if state == 0:
            if email_char.isalpha() or email_char == '.':
                state = 1
            elif email_char.isnumeric():
                state = 1
            else:
                valid = False
                invalid_reason += f" cannot contain {email_char} "
                break
        elif state == 1:
            if email_char.isalpha() or email_char == '.':
                pass
            elif email_char == '@':
                state = 2
            else:
                valid = False
                invalid_reason += f" cannot contain {email_char} "
                break
        elif state == 2:
            if email_char.isalpha():
                pass
            elif email_char == '.':
                state = 3
            else:
                valid = False
                invalid_reason += f" domain cannot contain {email_char} "
                break
        elif state == 3:
            if email_char.isalpha():
                state = 4
            else:
                valid = False
                invalid_reason += f" domain cannot contain {email_char} "
                break
        elif state == 4:
            if email_char.isalpha():
                state = 5
            else:
                valid = False
                invalid_reason += f" domain cannot contain {email_char} "
                break
        elif state == 5:
            if email_char.isalpha():
                pass
            elif email_char == ".":
                state = 3
            else:
                valid = False
                invalid_reason += f" domain cannot contain {email_char} "
                break

    if not valid or state != 5:
        print(invalid_reason)
        return False
    else:
        return True


def validate_password(password):
    if password == "":
        return "Password cannot be blank"
    elif len(password) < 5:
        return "Password is too short"
    return True


def validate_name(name):
    if name == "":
        return "name cannot be blank "
    elif name.__contains__("."):
        return "name cannot contain ."
    return True


def validate_username(username):
    if username.__contains__(" "):
        return "username cannot contain spaces"

    user_files = os.listdir(f"{bank_data_route}/Users/Customers")
    for user_file in user_files:
        if user_file.__contains__("."):
            user_file_username = user_file[0:user_file.index(".")]
        else:
            print("Customer file with no extension: "+user_file)
            continue

        if username == user_file_username:
            return False
    return True


def validate_address(address):
    if not address:
        return "address cannot be blank "
    elif len(address) < 3:
        return "address is too short "
    return True
