import sqlite3
import sys
import os
from event import Event
from check_admin import Check_admin


def main():
    Check_admin.make_password()

    con = sqlite3.connect(os.path.join(sys.path[0], "calendar.db"))

    con.execute(
        """CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description DEFAULT NULL,
            location DEFAULT NULL,
            begin_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            begin_time TEXT NOT NULL,
            end_time TEXT NOT NULL
        );"""
    )

    while True:
        main_menu_choice = input(
            "[C] Create event\n[D] Delete event\n[A] Administrator menu\n[Q] Quit\n> "
        ).upper()

        if main_menu_choice == "C":
            while True:

                begin_date = input("Please enter a begin date (dd-mm-yyyy).\n> ")
                if (
                    not begin_date[0].isdigit()
                    or not begin_date[1].isdigit()
                    or begin_date[2] != "-"
                    or not begin_date[3].isdigit()
                    or not begin_date[4].isdigit()
                    or begin_date[5] != "-"
                    or not begin_date[6].isdigit()
                    or not begin_date[7].isdigit()
                    or not begin_date[8].isdigit()
                    or not begin_date[9].isdigit()
                    or len(begin_date) != 10
                ):
                    print("Invalid date, please try again!")
                else:
                    print(f"The date you entered is {begin_date}.")
                    break

            while True:

                begin_time = input("Please enter a begin time (hh:mm).\n> ")
                if (
                    not begin_time[0].isdigit()
                    or not begin_time[1].isdigit()
                    or begin_time[2] != ":"
                    or not begin_time[3].isdigit()
                    or not begin_time[4].isdigit()
                    or len(begin_time) != 5
                ):
                    print("Invalid time, please try again!")
                else:
                    print(f"The time you entered is {begin_time}.")
                    break

            while True:

                end_date = input("Please enter an end date (dd-mm-yyyy).\n> ")
                if (
                    not end_date[0].isdigit()
                    or not end_date[1].isdigit()
                    or end_date[2] != "-"
                    or not end_date[3].isdigit()
                    or not end_date[4].isdigit()
                    or end_date[5] != "-"
                    or not end_date[6].isdigit()
                    or not end_date[7].isdigit()
                    or not end_date[8].isdigit()
                    or not end_date[9].isdigit()
                    or len(end_date) != 10
                ):
                    print("")
                else:
                    print(f"The date you entered is {end_date}.")
                    break

            while True:

                end_time = input("Please enter an end time (hh:mm).\n> ")
                if (
                    not end_time[0].isdigit()
                    or not end_time[1].isdigit()
                    or end_time[2] != ":"
                    or not end_time[3].isdigit()
                    or not end_time[4].isdigit()
                    or len(end_time) != 5
                ):
                    print("Invalid time, please try again!")
                else:
                    print(f"The time you entered is {end_time}.")
                    break

            title = input("Please enter an appropriate title.\n> ")

            while True:

                description_bool = input(
                    "Would you like to add a description? (Y/N)\n> "
                ).upper()
                if description_bool == "Y":
                    description = input("Please enter an appropriate description.\n> ")
                    break
                elif description_bool == "N":
                    description = None
                    break
                else:
                    print("Invalid description, please try again!")

            while True:

                location_bool = input(
                    "Would you like to add a location? (Y/N)\n> "
                ).upper()
                if location_bool == "Y":
                    location = input("Please enter an appropriate location.\n> ")
                    break
                elif location_bool == "N":
                    location = None
                    break
                else:
                    print("Invalid location, please try again!")

            event = Event(
                None,
                begin_date,
                end_date,
                begin_time,
                end_time,
                title,
                description,
                location,
            )

            event.create_event()

        if main_menu_choice == "D":
            delete_input = input(
                "Please enter the id and title of the event you would like to delete! (id, title)\n> "
            ).strip()
            delete_id, delete_title = [x.strip() for x in delete_input.split(",")]

            delete_id = int(delete_id)

            delete_event = Event(
                delete_id,
                None,
                None,
                None,
                None,
                delete_title,
                None,
                None,
            )

            delete_event.delete_event()

        if main_menu_choice == "A":
            admin_password = input("Please enter the password!\n> ")

            admin_check = Check_admin(
                admin_password,
            )

            admin_check.check_password()

        if main_menu_choice == "Q":
            quit()


if __name__ == "__main__":
    main()
