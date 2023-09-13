import os
import Accounts, Users


def build(page_data={}):
    page_type = page_data.get("page_type")
    new_page_data = retrieve_page(page_type)

    if page_type == "fatal_error":
        new_page_data["page_message"]["text"] = page_data.get("page_message")
    elif page_type == "login":
        if page_data.get("page_message"):
            new_page_data["page_message"]["text"] = page_data.get("page_message")
    elif page_type == "customer-sign-up":
        if page_data.get("page_message"):
            new_page_data["page_message"]["text"] = page_data.get("page_message")
    elif page_type == "staff-sign-up":
        if page_data.get("page_message"):
            new_page_data["page_message"]["text"] = page_data.get("page_message")
    elif page_type == "home":
        new_page_data["username"] = page_data.get("username")
        new_page_data["username_text"]["text"] = page_data.get("username")
    elif page_type == "staff-home":
        new_page_data["username"] = page_data.get("username")
        new_page_data["username_text"]["text"] = page_data.get("username")
    elif page_type == "customize_profile":
        new_page_data["username"] = page_data.get("username")
        get_customize_profile_changes(new_page_data, page_data.get("username"), "customer")
        if page_data.get("page_message"):
            new_page_data["page_message"]["text"] = page_data.get("page_message")
    elif page_type == "customize_staff_profile":
        new_page_data["username"] = page_data.get("username")
        get_customize_profile_changes(new_page_data, page_data.get("username"), "staff")
        if page_data.get("page_message"):
            new_page_data["page_message"]["text"] = page_data.get("page_message")
    elif page_type == "staff_controls":
        new_page_data["username"] = page_data.get("username")
        new_page_data["page_message"]["text"] = page_data.get("page_message")
        new_page_data = modify_for_staff_controls(new_page_data)
    elif page_type == "view_balance":
        new_page_data["username"] = page_data.get("username")
        new_page_data["checking_account_balance_text"]["text"] = \
            f"${Accounts.get_user_checking(page_data.get('username')).get_balance():.2f}"
        new_page_data["savings_account_balance_text"]["text"] = \
            f"${Accounts.get_user_savings(page_data.get('username')).get_balance():.2f}"
    elif page_type == "checking_history":
        new_page_data["username"] = page_data.get("username")
        new_page_data["page_number"] = page_data.get("page_number")
        new_page_data = add_transactions(new_page_data, page_data.get("username"),
                                         page_data.get("page_number"), "checking")
    elif page_type == "savings_history":
        new_page_data["username"] = page_data.get("username")
        new_page_data["page_number"] = page_data.get("page_number")
        new_page_data = add_transactions(new_page_data, page_data.get("username"),
                                         page_data.get("page_number"), "savings")
    elif page_type == "transfer_funds":
        new_page_data["username"] = page_data.get("username")
        new_page_data = add_transfer_options(new_page_data, page_data.get("username"))
        if page_data.get("page_message"):
            new_page_data["page_message"]["text"] = page_data.get("page_message")

    print(f"returning page: {page_type} = {new_page_data}")
    return new_page_data


def retrieve_page(page_type=""):
    """Receives a page type, and returns a dictionary containing page_item_names:page_item_details\n
        color: 000000000-255255255 (RGB)"""
    new_page_data = {}
    if page_type == "fatal_error":
        new_page_data["window_size"] = {
            "x": 500,
            "y": 400
        }
        new_page_data["page_message"] = {
            "component_type": "label",
            "x": 150,
            "y": 100,
            "width": 300,
            "height": 20,
            "text": "",
            "color": "200000000",
            "font_size": 12
        }
        new_page_data["page_image"] = {
            "component_type": "label",
            "x": 10,
            "y": 15,
            "width": 200,
            "height": 200,
            "image_name": "FrownyFace.png",
            "image_width": 100,
            "image_height": 100,
        }
    elif page_type == "login":
        new_page_data["page_title"] = "Login"
        new_page_data["window_size"] = {
            "x": 380,
            "y": 400
        }
        new_page_data["logo"] = {
            "component_type": "label",
            "x": 130,
            "y": 10,
            "width": 200,
            "height": 200,
            "image_name": "logo.jpg",
            "image_width": 100,
            "image_height": 100,
        }
        new_page_data["username_text"] = {
            "component_type": "label",
            "x": 25,
            "y": 174,
            "width": 100,
            "height": 10,
            "text": "Username: ",
            "color": "000000000",
            "font_size": 12,
        }
        new_page_data["username_field"] = {
            "component_type": "text_field",
            "x": 90,
            "y": 170,
            "width": 200,
            "height": 20,
            "text": "",
            "color": "000000000",
            "font_size": 12
        }
        new_page_data["password_text"] = {
            "component_type": "label",
            "x": 25,
            "y": 204,
            "width": 100,
            "height": 10,
            "text": "Password: ",
            "color": "000000000",
            "font_size": 12
        }
        new_page_data["password_field"] = {
            "component_type": "text_field",
            "x": 90,
            "y": 200,
            "width": 200,
            "height": 20,
            "text": "",
            "color": "000000000",
            "font_size": 12
        }
        new_page_data["page_message"] = {
            "component_type": "label",
            "x": 10,
            "y": 10,
            "width": 200,
            "height": 20,
            "text": "",
            "color": "200050050",
            "font_size": 12
        }
        new_page_data["login_button"] = {
            "component_type": "button",
            "x": 140,
            "y": 230,
            "width": 80,
            "height": 40,
            "text": "Login",
            "color": "255255255",
            "background_color": "100100255",
            "font_size": 12,
            "on_click_action": "submit_page",
        }
        new_page_data["customer_sign_up_button"] = {
            "component_type": "button",
            "x": 210,
            "y": 320,
            "width": 140,
            "height": 30,
            "text": "Customer Sign-up",
            "font_size": 12,
            "on_click_action": "request_page",
            "page_requested": "customer-sign-up"
        }
        new_page_data["staff_sign_up_button"] = {
            "component_type": "button",
            "x": 15,
            "y": 320,
            "width": 130,
            "height": 30,
            "text": "Staff Sign-up",
            "font_size": 12,
            "on_click_action": "request_page",
            "page_requested": "staff-sign-up"
        }
    elif page_type == "customer-sign-up":
        new_page_data["base_font_name"] = "Tahoma"
        new_page_data["base_font_style"] = "PLAIN"  # Can be PLAIN, BOLD, ITALIC, etc.
        new_page_data["base_font_size"] = 12
        new_page_data["page_title"] = "Sign Up"
        new_page_data["window_size"] = {
            "x": 600,
            "y": 400
        }
        new_page_data["sign_up_text"] = {
            "component_type": "label",
            "x": 20,
            "y": 14,
            "width": 150,
            "height": 35,
            "text": "Sign Up",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 20,
        }
        new_page_data["name_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 56,
            "width": 158,
            "height": 17,
            "text": "Name"
        }
        new_page_data["name_field"] = {
            "component_type": "text_field",
            "x": 70,
            "y": 74,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["username_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 97,
            "width": 158,
            "height": 17,
            "text": "Username"
        }
        new_page_data["username_field"] = {
            "component_type": "text_field",
            "x": 70,
            "y": 115,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["password_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 142,
            "width": 158,
            "height": 17,
            "text": "Password"
        }
        new_page_data["password_field"] = {
            "component_type": "text_field",
            "x": 70,
            "y": 160,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["email_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 97,
            "width": 158,
            "height": 17,
            "text": "Email"
        }
        new_page_data["email_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 115,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["address_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 142,
            "width": 158,
            "height": 17,
            "text": "Address"
        }
        new_page_data["address_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 160,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["ssn_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 56,
            "width": 158,
            "height": 17,
            "text": "SSN"
        }
        new_page_data["ssn_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 74,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["page_message"] = {
            "component_type": "label",
            "x": 40,
            "y": 200,
            "width": 500,
            "height": 100,
            "text": "",
            "color": "200000000",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 11,
        }
        new_page_data["create_account_button"] = {
            "component_type": "button",
            "x": 367,
            "y": 314,
            "width": 130,
            "height": 23,
            "text": "Create Account",
            "on_click_action": "submit_page"
        }
        new_page_data["back_button"] = {
            "component_type": "button",
            "x": 59,
            "y": 314,
            "width": 107,
            "height": 23,
            "text": "Back",
            "on_click_action": "request_page",
            "page_requested": "login"
        }
    elif page_type == "staff-sign-up":
        new_page_data["base_font_name"] = "Tahoma"
        new_page_data["base_font_style"] = "PLAIN"  # Can be PLAIN, BOLD, ITALIC, etc.
        new_page_data["base_font_size"] = 12
        new_page_data["page_title"] = "Sign Up"
        new_page_data["window_size"] = {
            "x": 600,
            "y": 400
        }
        new_page_data["sign_up_text"] = {
            "component_type": "label",
            "x": 20,
            "y": 14,
            "width": 150,
            "height": 35,
            "text": "Sign Up",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 20,
        }
        new_page_data["name_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 56,
            "width": 158,
            "height": 17,
            "text": "Name"
        }
        new_page_data["name_field"] = {
            "component_type": "text_field",
            "x": 70,
            "y": 74,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["username_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 97,
            "width": 158,
            "height": 17,
            "text": "Username"
        }
        new_page_data["username_field"] = {
            "component_type": "text_field",
            "x": 70,
            "y": 115,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["password_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 142,
            "width": 158,
            "height": 17,
            "text": "Password"
        }
        new_page_data["password_field"] = {
            "component_type": "text_field",
            "x": 70,
            "y": 160,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["email_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 97,
            "width": 158,
            "height": 17,
            "text": "Email"
        }
        new_page_data["email_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 115,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["address_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 142,
            "width": 158,
            "height": 17,
            "text": "Address"
        }
        new_page_data["address_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 160,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["ssn_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 56,
            "width": 158,
            "height": 17,
            "text": "SSN"
        }
        new_page_data["ssn_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 74,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["authorization_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 192,
            "width": 158,
            "height": 17,
            "text": "Authorization Code"
        }
        new_page_data["authorization_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 210,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["page_message"] = {
            "component_type": "label",
            "x": 40,
            "y": 200,
            "width": 500,
            "height": 100,
            "text": "",
            "color": "200000000",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 11,
        }
        new_page_data["create_account_button"] = {
            "component_type": "button",
            "x": 367,
            "y": 314,
            "width": 130,
            "height": 23,
            "text": "Create Account",
            "on_click_action": "submit_page"
        }
        new_page_data["back_button"] = {
            "component_type": "button",
            "x": 59,
            "y": 314,
            "width": 107,
            "height": 23,
            "text": "Back",
            "on_click_action": "request_page",
            "page_requested": "login"
        }
    elif page_type == "home":
        new_page_data["base_font_name"] = "Tahoma"
        new_page_data["base_font_style"] = "BOLD"  # Can be PLAIN, BOLD, ITALIC, etc.
        new_page_data["base_font_size"] = 11
        new_page_data["page_title"] = "Home"
        new_page_data["window_size"] = {
            "x": 600,
            "y": 400
        }
        new_page_data["welcome_text"] = {
            "component_type": "label",
            "x": 40,
            "y": 25,
            "width": 300,
            "height": 14,
            "text": "Welcome, ",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 11,
        }
        new_page_data["username_text"] = {
            "component_type": "label",
            "x": 100,
            "y": 25,
            "width": 500,
            "height": 14,
            "text": "",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 11,
        }
        new_page_data["customize_profile_button"] = {
            "component_type": "button",
            "x": 40,
            "y": 107,
            "width": 140,
            "height": 23,
            "text": "Customize Profile",
            "on_click_action": "request_page",
            "page_requested": "customize_profile"
        }
        new_page_data["view_balance_button"] = {
            "component_type": "button",
            "x": 40,
            "y": 157,
            "width": 140,
            "height": 23,
            "text": "View Balance",
            "on_click_action": "request_page",
            "page_requested": "view_balance"
        }
        new_page_data["welcome_sub_text"] = {
            "component_type": "label",
            "x": 40,
            "y": 52,
            "width": 534,
            "height": 23,
            "text": "Here in the welcome center you can edit profile information, "
                    "view balances and transactions, and transfer funds",
            "font_name": "Tahoma",
            "font_style": "PLAIN",
            "font_size": 10,
        }
        new_page_data["customize_profile_description"] = {
            "component_type": "label",
            "x": 205,
            "y": 111,
            "width": 220,
            "height": 14,
            "text": "View and customize your user profile",
        }
        new_page_data["view_balance_description"] = {
            "component_type": "label",
            "x": 205,
            "y": 161,
            "width": 220,
            "height": 14,
            "text": "View Checking and Saving balance",
        }
        new_page_data["sign_out_button"] = {
            "component_type": "button",
            "x": 485,
            "y": 316,
            "width": 89,
            "height": 23,
            "text": "Sign-out",
            "on_click_action": "request_page",
            "page_requested": "login"
        }
    elif page_type == "staff-home":
        new_page_data["base_font_name"] = "Tahoma"
        new_page_data["base_font_style"] = "BOLD"  # Can be PLAIN, BOLD, ITALIC, etc.
        new_page_data["base_font_size"] = 11
        new_page_data["page_title"] = "Staff Home"
        new_page_data["window_size"] = {
            "x": 600,
            "y": 400
        }
        new_page_data["welcome_text"] = {
            "component_type": "label",
            "x": 40,
            "y": 25,
            "width": 300,
            "height": 14,
            "text": "Welcome staff, ",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 11,
        }
        new_page_data["username_text"] = {
            "component_type": "label",
            "x": 130,
            "y": 25,
            "width": 500,
            "height": 14,
            "text": "",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 11,
        }
        new_page_data["customize_profile_button"] = {
            "component_type": "button",
            "x": 40,
            "y": 107,
            "width": 140,
            "height": 23,
            "text": "Customize Profile",
            "on_click_action": "request_page",
            "page_requested": "customize_staff_profile"
        }
        new_page_data["staff_controls_button"] = {
            "component_type": "button",
            "x": 40,
            "y": 157,
            "width": 140,
            "height": 23,
            "text": "Staff Controls",
            "on_click_action": "request_page",
            "page_requested": "staff_controls"
        }
        new_page_data["welcome_sub_text"] = {
            "component_type": "label",
            "x": 40,
            "y": 52,
            "width": 534,
            "height": 23,
            "text": "Here in the welcome center you can edit profile information, "
                    "view balances and transactions, and transfer funds",
            "font_name": "Tahoma",
            "font_style": "PLAIN",
            "font_size": 10,
        }
        new_page_data["customize_profile_description"] = {
            "component_type": "label",
            "x": 205,
            "y": 111,
            "width": 220,
            "height": 14,
            "text": "View and customize your user profile",
        }
        new_page_data["view_balance_description"] = {
            "component_type": "label",
            "x": 205,
            "y": 161,
            "width": 220,
            "height": 14,
            "text": "View Checking and Saving balance",
        }
        new_page_data["sign_out_button"] = {
            "component_type": "button",
            "x": 485,
            "y": 316,
            "width": 89,
            "height": 23,
            "text": "Sign-out",
            "on_click_action": "request_page",
            "page_requested": "login"
        }
    elif page_type == "customize_profile":
        new_page_data["base_font_name"] = "Tahoma"
        new_page_data["base_font_style"] = "PLAIN"  # Can be PLAIN, BOLD, ITALIC, etc.
        new_page_data["base_font_size"] = 12
        new_page_data["page_title"] = "Customize profile"
        new_page_data["window_size"] = {
            "x": 600,
            "y": 400
        }
        new_page_data["customize_profile_text"] = {
            "component_type": "label",
            "x": 20,
            "y": 14,
            "width": 300,
            "height": 35,
            "text": "Customize profile",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 20,
        }
        new_page_data["name_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 56,
            "width": 200,
            "height": 17,
            "text": "Name: "
        }
        new_page_data["name_field"] = {
            "component_type": "text_field",
            "x": 70,
            "y": 74,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["username_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 97,
            "width": 158,
            "height": 17,
            "text": "Username"
        }
        new_page_data["username_value"] = {
            "component_type": "label",
            "x": 70,
            "y": 115,
            "width": 200,
            "height": 20,
            "text": "",
            "font_style": "BOLD",
        }
        new_page_data["password_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 142,
            "width": 158,
            "height": 17,
            "text": "Password"
        }
        new_page_data["new_password_field"] = {
            "component_type": "text_field",
            "x": 70,
            "y": 160,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["email_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 97,
            "width": 200,
            "height": 17,
            "text": "Email: "
        }
        new_page_data["email_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 115,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["address_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 142,
            "width": 200,
            "height": 17,
            "text": "Address: "
        }
        new_page_data["address_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 160,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["ssn_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 56,
            "width": 158,
            "height": 17,
            "text": "SSN"
        }
        new_page_data["ssn_value"] = {
            "component_type": "label",
            "x": 303,
            "y": 74,
            "width": 158,
            "height": 20,
            "text": "",
            "font_style": "BOLD"
        }
        new_page_data["old_password_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 242,
            "width": 158,
            "height": 17,
            "text": "Previous Password"
        }
        new_page_data["old_password_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 260,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["page_message"] = {
            "component_type": "label",
            "x": 40,
            "y": 200,
            "width": 500,
            "height": 100,
            "text": "",
            "color": "200000000",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 11,
        }
        new_page_data["submit_changes_button"] = {
            "component_type": "button",
            "x": 367,
            "y": 314,
            "width": 130,
            "height": 23,
            "text": "Submit changes",
            "on_click_action": "submit_page"
        }
        new_page_data["back_button"] = {
            "component_type": "button",
            "x": 59,
            "y": 314,
            "width": 107,
            "height": 23,
            "text": "Back",
            "on_click_action": "request_page",
            "page_requested": "home"
        }
    elif page_type == "customize_staff_profile":
        new_page_data["base_font_name"] = "Tahoma"
        new_page_data["base_font_style"] = "PLAIN"  # Can be PLAIN, BOLD, ITALIC, etc.
        new_page_data["base_font_size"] = 12
        new_page_data["page_title"] = "Customize profile"
        new_page_data["window_size"] = {
            "x": 600,
            "y": 400
        }
        new_page_data["customize_profile_text"] = {
            "component_type": "label",
            "x": 20,
            "y": 14,
            "width": 300,
            "height": 35,
            "text": "Customize profile",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 20,
        }
        new_page_data["name_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 56,
            "width": 200,
            "height": 17,
            "text": "Name: "
        }
        new_page_data["name_field"] = {
            "component_type": "text_field",
            "x": 70,
            "y": 74,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["username_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 97,
            "width": 158,
            "height": 17,
            "text": "Username"
        }
        new_page_data["username_value"] = {
            "component_type": "label",
            "x": 70,
            "y": 115,
            "width": 200,
            "height": 20,
            "text": "",
            "font_style": "BOLD",
        }
        new_page_data["eid_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 187,
            "width": 158,
            "height": 17,
            "text": "EID"
        }
        new_page_data["eid_value"] = {
            "component_type": "label",
            "x": 70,
            "y": 205,
            "width": 200,
            "height": 20,
            "text": "",
            "font_style": "BOLD",
        }
        new_page_data["password_text"] = {
            "component_type": "label",
            "x": 70,
            "y": 142,
            "width": 158,
            "height": 17,
            "text": "Password"
        }
        new_page_data["new_password_field"] = {
            "component_type": "text_field",
            "x": 70,
            "y": 160,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["email_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 97,
            "width": 200,
            "height": 17,
            "text": "Email: "
        }
        new_page_data["email_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 115,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["address_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 142,
            "width": 200,
            "height": 17,
            "text": "Address: "
        }
        new_page_data["address_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 160,
            "width": 158,
            "height": 20,
            "text": ""
        }
        new_page_data["ssn_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 56,
            "width": 158,
            "height": 17,
            "text": "SSN"
        }
        new_page_data["ssn_value"] = {
            "component_type": "label",
            "x": 303,
            "y": 74,
            "width": 158,
            "height": 20,
            "text": "",
            "font_style": "BOLD"
        }
        new_page_data["old_password_text"] = {
            "component_type": "label",
            "x": 303,
            "y": 242,
            "width": 158,
            "height": 17,
            "text": "Previous Password"
        }
        new_page_data["old_password_field"] = {
            "component_type": "text_field",
            "x": 303,
            "y": 260,
            "width": 158,
            "height": 20,
            "text": "",
        }
        new_page_data["page_message"] = {
            "component_type": "label",
            "x": 40,
            "y": 200,
            "width": 500,
            "height": 100,
            "text": "",
            "color": "200000000",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 11,
        }
        new_page_data["submit_changes_button"] = {
            "component_type": "button",
            "x": 367,
            "y": 314,
            "width": 130,
            "height": 23,
            "text": "Submit changes",
            "on_click_action": "submit_page"
        }
        new_page_data["back_button"] = {
            "component_type": "button",
            "x": 59,
            "y": 314,
            "width": 107,
            "height": 23,
            "text": "Back",
            "on_click_action": "request_page",
            "page_requested": "staff-home"
        }
    elif page_type == "view_balance":
        new_page_data["base_font_name"] = "Tahoma"
        new_page_data["base_font_style"] = "BOLD"  # Can be PLAIN, BOLD, ITALIC, etc.
        new_page_data["base_font_size"] = 11
        new_page_data["page_title"] = "View Balance"
        new_page_data["title_text"] = {
            "component_type": "label",
            "x": 40,
            "y": 25,
            "width": 300,
            "height": 24,
            "text": "Accounts",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 14,
        }
        new_page_data["window_size"] = {
            "x": 600,
            "y": 400
        }
        new_page_data["checking_account_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 100,
            "width": 150,
            "height": 14,
            "text": "Checking Account"
        }
        new_page_data["savings_account_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 193,
            "width": 150,
            "height": 14,
            "text": "Savings Account"
        }
        new_page_data["checking_account_button"] = {
            "component_type": "button",
            "x": 56,
            "y": 130,
            "width": 150,
            "height": 24,
            "text": "View History",
            "on_click_action": "request_page",
            "page_requested": "checking_history"
        }
        new_page_data["savings_account_button"] = {
            "component_type": "button",
            "x": 56,
            "y": 223,
            "width": 150,
            "height": 24,
            "text": "View History",
            "on_click_action": "request_page",
            "page_requested": "savings_history"
        }
        new_page_data["checking_account_balance_text"] = {
            "component_type": "label",
            "x": 150,
            "y": 85,
            "width": 500,
            "height": 40,
            "text": "",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 30,
        }
        new_page_data["savings_account_balance_text"] = {
            "component_type": "label",
            "x": 150,
            "y": 178,
            "width": 500,
            "height": 40,
            "text": "",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 30,
        }
        new_page_data["return_button"] = {
            "component_type": "button",
            "x": 272,
            "y": 313,
            "width": 89,
            "height": 23,
            "text": "Return",
            "on_click_action": "request_page",
            "page_requested": "home",
        }
        new_page_data["transfer_funds_button"] = {
            "component_type": "button",
            "x": 72,
            "y": 313,
            "width": 122,
            "height": 23,
            "text": "Transfer Funds",
            "on_click_action": "request_page",
            "page_requested": "transfer_funds",
        }
    elif page_type == "checking_history":
        new_page_data["page_title"] = "Checking Account History"
        new_page_data["page_number"] = 1
        new_page_data["window_size"] = {
            "x": 600,
            "y": 700
        }
        new_page_data["welcome_text"] = {
            "component_type": "label",
            "x": 40,
            "y": 25,
            "width": 300,
            "height": 24,
            "text": "Checking account",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 14,
        }
        new_page_data["page_number_text"] = {
            "component_type": "label",
            "x": 480,
            "y": 25,
            "width": 300,
            "height": 24,
            "text": "",
            "font_style": "BOLD",
            "font_size": 12,
        }
        new_page_data["return_button"] = {
            "component_type": "button",
            "x": 30,
            "y": 620,
            "width": 89,
            "height": 23,
            "text": "Return",
            "on_click_action": "request_page",
            "page_requested": "view_balance",
        }
    elif page_type == "savings_history":
        new_page_data["page_title"] = "Savings Account History"
        new_page_data["page_number"] = 1
        new_page_data["window_size"] = {
            "x": 600,
            "y": 700
        }
        new_page_data["welcome_text"] = {
            "component_type": "label",
            "x": 40,
            "y": 25,
            "width": 300,
            "height": 24,
            "text": "Savings account",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 14,
        }
        new_page_data["page_number_text"] = {
            "component_type": "label",
            "x": 480,
            "y": 25,
            "width": 300,
            "height": 24,
            "text": "",
            "font_style": "BOLD",
            "font_size": 12,
        }
        new_page_data["return_button"] = {
            "component_type": "button",
            "x": 30,
            "y": 620,
            "width": 89,
            "height": 23,
            "text": "Return",
            "on_click_action": "request_page",
            "page_requested": "view_balance",
        }
    elif page_type == "transfer_funds":
        new_page_data["base_font_name"] = "Tahoma"
        new_page_data["base_font_size"] = 14
        new_page_data["page_title"] = "Transfer Funds"
        new_page_data["title_text"] = {
            "component_type": "label",
            "x": 40,
            "y": 25,
            "width": 300,
            "height": 24,
            "text": "Transfer",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 18,
        }
        new_page_data["window_size"] = {
            "x": 600,
            "y": 420
        }
        new_page_data["from_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 85,
            "width": 150,
            "height": 14,
            "text": "From: ",
            "font_size": 15
        }
        new_page_data["from_field"] = {
            "component_type": "combo_box",
            "x": 146,
            "y": 80,
            "width": 350,
            "height": 25,
            "text": "From: ",
            "options": ["None"],
            "font_size": 15
        }
        new_page_data["to_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 125,
            "width": 150,
            "height": 14,
            "text": "To: ",
            "font_size": 15
        }
        new_page_data["to_field"] = {
            "component_type": "combo_box",
            "x": 146,
            "y": 120,
            "width": 350,
            "height": 25,
            "text": "To: ",
            "options": ["None"],
            "font_size": 15
        }
        new_page_data["username_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 165,
            "width": 150,
            "height": 14,
            "text": "Username: ",
            "font_size": 15
        }
        new_page_data["username_subtext"] = {
            "component_type": "label",
            "x": 146,
            "y": 185,
            "width": 150,
            "height": 14,
            "text": "Required if To: User",
            "font_size": 11
        }
        new_page_data["username_field"] = {
            "component_type": "text_field",
            "x": 146,
            "y": 160,
            "width": 350,
            "height": 25,
            "text": "",
            "font_size": 15
        }
        new_page_data["amount_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 225,
            "width": 150,
            "height": 14,
            "text": "Amount: ",
            "font_size": 15
        }
        new_page_data["amount_field"] = {
            "component_type": "text_field",
            "x": 146,
            "y": 220,
            "width": 350,
            "height": 25,
            "text": "",
            "font_size": 15
        }
        new_page_data["reason_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 265,
            "width": 150,
            "height": 14,
            "text": "Reason: ",
            "font_size": 15
        }
        new_page_data["reason_field"] = {
            "component_type": "text_field",
            "x": 146,
            "y": 260,
            "width": 350,
            "height": 25,
            "text": "",
            "font_size": 15
        }
        new_page_data["page_message"] = {
            "component_type": "label",
            "x": 56,
            "y": 295,
            "width": 400,
            "height": 14,
            "text": "",
            "color": "200000000",
            "font_size": 12
        }
        new_page_data["return_button"] = {
            "component_type": "button",
            "x": 30,
            "y": 340,
            "width": 89,
            "height": 23,
            "text": "Return",
            "on_click_action": "request_page",
            "page_requested": "view_balance",
        }
    elif page_type == "staff_controls":
        new_page_data["base_font_name"] = "Tahoma"
        new_page_data["base_font_size"] = 14
        new_page_data["page_title"] = "Transfer Funds"
        new_page_data["title_text"] = {
            "component_type": "label",
            "x": 40,
            "y": 25,
            "width": 300,
            "height": 24,
            "text": "Staff Controls",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 18,
        }
        new_page_data["window_size"] = {
            "x": 600,
            "y": 420
        }
        new_page_data["to_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 85,
            "width": 150,
            "height": 14,
            "text": "To: ",
            "font_size": 15
        }
        new_page_data["to_field"] = {
            "component_type": "combo_box",
            "x": 146,
            "y": 80,
            "width": 350,
            "height": 25,
            "text": "From: ",
            "options": ["None"],
            "font_size": 15
        }
        new_page_data["account_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 125,
            "width": 150,
            "height": 14,
            "text": "Account: ",
            "font_size": 15
        }
        new_page_data["account_field"] = {
            "component_type": "combo_box",
            "x": 146,
            "y": 120,
            "width": 350,
            "height": 25,
            "text": "To: ",
            "options": ["Checking", "Savings"],
            "font_size": 15
        }
        new_page_data["amount_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 185,
            "width": 150,
            "height": 14,
            "text": "Amount: ",
            "font_size": 15
        }
        new_page_data["amount_field"] = {
            "component_type": "text_field",
            "x": 146,
            "y": 180,
            "width": 350,
            "height": 25,
            "text": "",
            "font_size": 15
        }
        new_page_data["reason_text"] = {
            "component_type": "label",
            "x": 56,
            "y": 225,
            "width": 150,
            "height": 14,
            "text": "Reason: ",
            "font_size": 15
        }
        new_page_data["reason_field"] = {
            "component_type": "text_field",
            "x": 146,
            "y": 220,
            "width": 350,
            "height": 25,
            "text": "",
            "font_size": 15
        }
        new_page_data["page_message"] = {
            "component_type": "label",
            "x": 56,
            "y": 295,
            "width": 400,
            "height": 14,
            "text": "",
            "color": "200000000",
            "font_size": 12
        }
        new_page_data["send_button"] = {
            "component_type": "button",
            "x": 465,
            "y": 340,
            "width": 89,
            "height": 23,
            "text": "Send",
            "on_click_action": "submit_page"
        }
        new_page_data["return_button"] = {
            "component_type": "button",
            "x": 30,
            "y": 340,
            "width": 89,
            "height": 23,
            "text": "Return",
            "on_click_action": "request_page",
            "page_requested": "staff-home",
        }
    elif page_type == "__template__":
        new_page_data["base_font_name"] = "Comic Sans"
        new_page_data["base_font_style"] = "PLAIN"  # Can be PLAIN, BOLD, ITALIC, etc.
        new_page_data["base_font_size"] = 12
        new_page_data["page_title"] = "Template"
        new_page_data["window_size"] = {
            "x": 400,
            "y": 300
        }
        new_page_data["template_text"] = {
            "component_type": "label",
            "x": 25,
            "y": 154,
            "width": 100,
            "height": 10,
            "text": "This is template text"
        }
        new_page_data["template_text_2"] = {
            "component_type": "label",
            "x": 25,
            "y": 194,
            "width": 100,
            "height": 10,
            "text": "This is template text 2!",
            "color": "000000000",
            "font_name": "Calibri",
            "font_style": "BOLD",
            "font_size": 12,
        }
        new_page_data["button"] = {
            "component_type": "button",
            "x": 140,
            "y": 200,
            "width": 80,
            "height": 40,
            "text": "KABOOM!",
            "color": "255255255",
            "background_color": "100100255",
            "font_size": 12,
            "on_click_action": "submit_form",
        }
        new_page_data["button_2"] = {
            "component_type": "button",
            "x": 140,
            "y": 200,
            "width": 80,
            "height": 40,
            "text": "Refresh",
            "color": "255255255",
            "background_color": "100100255",
            "font_size": 12,
            "on_click_action": "request_page",
            "page_requested": "login"
        }

    new_page_data["page_type"] = page_type
    return new_page_data


def add_transfer_options(new_page_data={}, username=""):
    user = Users.get_user(username)
    if not user:
        return new_page_data

    accounts = user.get_accounts()
    got_checking, got_savings = False, False

    for account_number in accounts:
        if got_checking and got_savings:
            break
        else:
            first_number = account_number[0]
            if first_number == "1" or first_number == "2" or first_number == "3" or first_number == "4":
                checking_account = Accounts.get_checking_account(account_number)
                got_checking = True
            elif first_number == "5" or first_number == "6" or first_number == "7" or first_number == "8":
                savings_account = Accounts.get_savings_account(account_number)
                got_savings = True

    from_options = []
    if got_checking:
        from_options.append(f"Checking account | ${checking_account.get_balance()}")

    if got_savings:
        from_options.append(f"Savings account | ${savings_account.get_balance()}")

    to_options = from_options.copy()
    to_options.append("User checking")
    to_options.append("User savings")

    new_page_data["to_field"]["options"] = to_options
    new_page_data["from_field"]["options"] = from_options

    new_page_data["send_button"] = {
        "component_type": "button",
        "x": 465,
        "y": 340,
        "width": 89,
        "height": 23,
        "text": "Send",
        "on_click_action": "submit_page"
    }
    return new_page_data


def add_transactions(new_page_data={}, username="", page_number=0, account_type=""):
    user = Users.get_user(username)
    if not user:
        return new_page_data
    new_page_data["page_number_text"]["text"] = f"Page: {page_number}"

    accounts = user.get_accounts()
    transaction_history = {}
    if account_type == "checking":
        for account_number in accounts:
            first_digit = account_number[0]
            if first_digit == "1" or first_digit == "2" or first_digit == "3" or first_digit == "4":
                checking_account = Accounts.get_checking_account(account_number)
                transaction_history = checking_account.get_transaction_history()
    elif account_type == "savings":
        for account_number in accounts:
            first_digit = account_number[0]
            if first_digit == "5" or first_digit == "6" or first_digit == "7" or first_digit == "8":
                savings_account = Accounts.get_savings_account(account_number)
                transaction_history = savings_account.get_transaction_history()

    if not transaction_history:
        return new_page_data
    else:
        history_dates_inverted = []
        for transaction_date in transaction_history:
            history_dates_inverted.insert(0, transaction_date)

        transactions_per_page = 10
        date_x = 40
        value_x = 185
        starting_y = 145
        y_increment = 30

        new_page_data[f"transaction_date_text"] = {
            "component_type": "label",
            "x": date_x,
            "y": starting_y - 30,
            "width": 140,
            "height": 24,
            "text": f"Date",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 16,
        }
        new_page_data[f"transaction_value_text"] = {
            "component_type": "label",
            "x": value_x,
            "y": starting_y - 30,
            "width": 370,
            "height": 24,
            "text": f"Amount | Reason",
            "font_name": "Tahoma",
            "font_style": "BOLD",
            "font_size": 16,
        }

        dots = "..................................."

        count = 1
        count_range_min = ((page_number - 1) * transactions_per_page + 1)
        count_range_max = page_number * transactions_per_page
        current_y = starting_y
        for transaction_date in history_dates_inverted:
            if count_range_min <= count <= count_range_max:
                new_page_data[f"transaction_date_{count}"] = {
                    "component_type": "label",
                    "x": date_x,
                    "y": current_y,
                    "width": 140,
                    "height": 24,
                    "text": f"{transaction_date}{dots}",
                    "font_name": "Tahoma",
                    "font_size": 12,
                }
                new_page_data[f"transaction_value_{count}"] = {
                    "component_type": "label",
                    "x": value_x,
                    "y": current_y,
                    "width": 370,
                    "height": 24,
                    "text": f"{transaction_history.get(transaction_date)}",
                    "font_name": "Tahoma",
                    "font_style": "BOLD",
                    "font_size": 12,
                }
                current_y += y_increment

            count += 1

        if int(page_number)*10 < len(transaction_history):
            new_page_data["next_button"] = {
                "component_type": "button",
                "x": 480,
                "y": 620,
                "width": 89,
                "height": 23,
                "text": "Next",
                "on_click_action": "request_page",
                "page_requested": "checking_history+",
            }
        if int(page_number) > 1:
            new_page_data["previous_button"] = {
                "component_type": "button",
                "x": 380,
                "y": 620,
                "width": 89,
                "height": 23,
                "text": "Prev",
                "on_click_action": "request_page",
                "page_requested": "checking_history-",
            }

        return new_page_data


def get_customize_profile_changes(page_data={}, username="", user_type=""):
    page_data["username_value"]["text"] = username
    user = Users.get_user(username)
    ssn = user.get_ssn()
    page_data["ssn_value"]["text"] = f"*****{ssn[-4:]}"
    page_data["name_text"]["text"] += user.get_name()
    page_data["email_text"]["text"] += user.get_email()
    page_data["address_text"]["text"] += user.get_address()

    if user_type == "staff":
        page_data["eid_value"]["text"] = user.get_eid()

    return page_data


def modify_for_staff_controls(page_data={}):
    users = Users.list_customers()
    page_data["to_field"]["options"] = users
    return page_data

