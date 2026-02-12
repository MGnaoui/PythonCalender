import random
from admin_menu import Admin_menu
import string

file = "urjubnhgar78ur432grthfg47g89trfwsebyidf.txt"


class Check_admin:

    def __init__(self, password):
        self.password = password

    def make_password():
        with open(file, "w", encoding="utf-8") as f:
            f.truncate()
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            f.write(random_string)

    def check_password(password):
        with open(file, "r", encoding="utf-8") as f:
            password_txt = f.readline()
            if password_txt == password:
                admin_menu_choice = input(
                    "[R] Reset database\n[J] Export database as json\n[C] Export database as csv\n[Q] Return\n> "
                ).upper()

                if admin_menu_choice == "R":
                    Admin_menu.reset_database()
                elif admin_menu_choice == "J":
                    Admin_menu.export_database_json()
                elif admin_menu_choice == "C":
                    Admin_menu.export_database_csv()
                elif admin_menu_choice == "Q":
                    quit()
