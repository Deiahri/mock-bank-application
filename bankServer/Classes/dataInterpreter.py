import pageBuilder, json
import Users
from Accounts import process_transfer


def interpret(sent_data={}):
    sent_page_type = sent_data.get("page_type")
    page_data = {}
    if not sent_page_type:
        page_data["page_type"] = "fatal_error"
        page_data["page_message"] = "Fatal Error: Page type was not sent"
    if sent_page_type == "login":
        if sent_data.get("page_requested") == "login":
            page_data["page_type"] = "login"
        elif sent_data.get("page_requested") == "customer-sign-up":
            page_data["page_type"] = "customer-sign-up"
        elif sent_data.get("page_requested") == "staff-sign-up":
            page_data["page_type"] = "staff-sign-up"
        # checks if credentials are correct
        else:
            user = Users.get_user(sent_data.get("username_field").lower())
            # if user can be retrieved, checks password
            if user:
                # goes to summary page on success
                if user.get_password() == sent_data.get("password_field"):
                    if type(user) is Users.Customer:
                        page_data["page_type"] = "home"
                        page_data["username"] = sent_data.get("username_field")
                    elif type(user) is Users.Staff:
                        page_data["page_type"] = "staff-home"
                        page_data["username"] = sent_data.get("username_field")
                    else:
                        page_data["page_type"] = "fatal_error"
                        page_data["page_message"] = "Something went wrong on our end. Sorry"
                        print(f"Error: Expected user.get_user() to return either staff or customer, but got {type(user)}")
                # goes to login page on fail
                else:
                    page_data["page_type"] = "login"
                    page_data["page_message"] = "invalid login credentials"
            # goes to login page on fail
            else:
                page_data["page_type"] = "login"
                page_data["page_message"] = "invalid login credentials"
    elif sent_page_type == "home":
        if sent_data.get("page_requested") == "login":
            page_data["page_type"] = "login"
        elif sent_data.get("page_requested") == "view_balance":
            page_data["page_type"] = "view_balance"
            page_data["username"] = sent_data.get("username")
        elif sent_data.get("page_requested") == "customize_profile":
            page_data["page_type"] = "customize_profile"
            page_data["username"] = sent_data.get("username")
    elif sent_page_type == "customize_profile":
        if sent_data.get("page_requested") == "home":
            page_data["page_type"] = "home"
            page_data["username"] = sent_data.get("username")
        else:
            response = Users.validate_and_apply_changes(sent_data.get("username"), sent_data)
            page_data["page_message"] = response
            page_data["page_type"] = "customize_profile"
            page_data["username"] = sent_data.get("username")

    elif sent_page_type == "staff-home":
        if sent_data.get("page_requested") == "login":
            page_data["page_type"] = "login"
        elif sent_data.get("page_requested") == "customize_staff_profile":
            page_data["page_type"] = "customize_staff_profile"
            page_data["username"] = sent_data.get("username")
        elif sent_data.get("page_requested") == "staff_controls":
            page_data["page_type"] = "staff_controls"
            page_data["username"] = sent_data.get("username")
    elif sent_page_type == "customize_staff_profile":
        if sent_data.get("page_requested") == "staff-home":
            page_data["page_type"] = "staff-home"
            page_data["username"] = sent_data.get("username")
        else:
            response = Users.validate_and_apply_changes(sent_data.get("username"), sent_data)
            page_data["page_message"] = response
            page_data["page_type"] = "customize_staff_profile"
            page_data["username"] = sent_data.get("username")
    elif sent_page_type == "staff_controls":
        if sent_data.get("page_requested") == "staff-home":
            page_data["page_type"] = "staff-home"
            page_data["username"] = sent_data.get("username")
        else:
            response = Users.apply_staff_change(sent_data, sent_data.get("username"))
            page_data["page_message"] = response
            page_data["page_type"] = "staff_controls"
            page_data["username"] = sent_data.get("username")
    elif sent_page_type == "view_balance":
        if sent_data.get("page_requested") == "home":
            page_data["page_type"] = "home"
            page_data["username"] = sent_data.get("username")
        elif sent_data.get("page_requested") == "checking_history":
            page_data["page_type"] = "checking_history"
            page_data["username"] = sent_data.get("username")
            page_data["page_number"] = 1
        elif sent_data.get("page_requested") == "savings_history":
            page_data["page_type"] = "savings_history"
            page_data["username"] = sent_data.get("username")
            page_data["page_number"] = 1
        elif sent_data.get("page_requested") == "transfer_funds":
            page_data["page_type"] = "transfer_funds"
            page_data["username"] = sent_data.get("username")
    elif sent_page_type == "transfer_funds":
        if sent_data.get("page_requested") == "view_balance":
            page_data["page_type"] = "view_balance"
            page_data["username"] = sent_data.get("username")
        else:
            response = process_transfer(sent_data)
            if type(response) == str:
                page_data["page_message"] = response
            page_data["page_type"] = "transfer_funds"
            page_data["username"] = sent_data.get("username")
    elif sent_page_type == "checking_history":
        if sent_data.get("page_requested") == "view_balance":
            page_data["page_type"] = "view_balance"
            page_data["username"] = sent_data.get("username")
        elif sent_data.get("page_requested") == "checking_history+":
            page_data["page_type"] = "checking_history"
            page_data["username"] = sent_data.get("username")
            page_data["page_number"] = int(sent_data.get("page_number")) + 1
        elif sent_data.get("page_requested") == "checking_history-":
            page_data["page_type"] = "checking_history"
            page_data["username"] = sent_data.get("username")
            page_data["page_number"] = int(sent_data.get("page_number")) - 1
    elif sent_page_type == "savings_history":
        if sent_data.get("page_requested") == "view_balance":
            page_data["page_type"] = "view_balance"
            page_data["username"] = sent_data.get("username")
        elif sent_data.get("page_requested") == "savings_history+":
            page_data["page_type"] = "savings_history"
            page_data["username"] = sent_data.get("username")
            page_data["page_number"] = int(sent_data.get("page_number")) + 1
        elif sent_data.get("page_requested") == "savings_history-":
            page_data["page_type"] = "savings_history"
            page_data["username"] = sent_data.get("username")
            page_data["page_number"] = int(sent_data.get("page_number")) - 1
    elif sent_page_type == "customer-sign-up":
        if sent_data.get("page_requested") == "login":
            page_data["page_type"] = "login"
        # only other option is to create account
        else:
            user_creation_response = Users.create_user(sent_data, "customer")
            if type(user_creation_response) is Users.Customer:
                page_data["page_type"] = "home"
                page_data["username"] = sent_data.get("username_field")
            else:
                page_data["page_type"] = "customer-sign-up"
                page_data["page_message"] = user_creation_response
    elif sent_page_type == "staff-sign-up":
        if sent_data.get("page_requested") == "login":
            page_data["page_type"] = "login"
        else:
            user_creation_response = Users.create_user(sent_data, "staff")
            if type(user_creation_response) is Users.Staff:
                page_data["page_type"] = "staff-home"
                page_data["username"] = sent_data.get("username_field")
            else:
                page_data["page_type"] = "staff-sign-up"
                page_data["page_message"] = user_creation_response
    else:
        page_data["page_type"] = "fatal_error"
        page_data["page_message"] = "Fatal Error: Page type does not exist"

    new_page_data = pageBuilder.build(page_data)
    return new_page_data


# d = {
#     "page_type": "login",
#     "username_field": "Drett",
#     "password_field": "pass",
# }
# returned = interpret(d)
# with open("output.txt", "w") as output_file:
#     json.dump(returned, output_file, indent=4)
