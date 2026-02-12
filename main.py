import sqlite3
import sys
import os
from event import Event


def main():
    con = sqlite3.connect(os.path.join(sys.path[0], "calender.db"))
    cursor = con.cursor()

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

    main_menu_choice = input("[C] Create event\n> ").upper()

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
                or len(begin_date) != 9
            ):
                print("Invalid date, please try again!")
            else:
                print(f"The date you entered is {begin_date}.")
                break

            begin_time = input("Please enter a begin time (hh:mm).\n> ")
            if (
                not begin_time[0].isdigit()
                or not begin_time[1].isdigit()
                or begin_time[2] != ":"
                or not begin_time[3].isdigit()
                or not begin_time[4].isdigit()
            ):
                print("Invalid time, please try again!")
            else:
                print(f"The time you entered is {begin_time}.")
                break

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
                or len(end_date) != 9
            ):
                print("")
            else:
                print(f"The date you entered is {end_date}.")
                break

            end_time = input("Please enter an end time (hh:mm).\n> ")
            if (
                not end_time[0].isdigit()
                or not end_time[1].isdigit()
                or end_time[2] != ":"
                or not end_time[3].isdigit()
                or not end_time[4].isdigit()
            ):
                print("Invalid time, please try again!")
            else:
                print(f"The time you entered is {end_time}.")
                break

            title = input("Please enter an appropriate title.")

            description_bool = input(
                "Would you like to add a description? (Y/N)"
            ).upper()
            if description_bool == "Y":
                description = input("Please enter an appropriate description.")
                break
            elif description_bool == "N":
                description = "NULL"
                break
            else:
                print("Invalid description, please try again!")

            location_bool = input("Would you like to add a location? (Y/N)").upper()
            if location_bool == "Y":
                location = input("Please enter an appropriate location.")
                break
            elif location_bool == "N":
                location = "NULL"
                break
            else:
                print("Invalid location, please try again!")

        Event.creat_event(begin_date, end_date, begin_time, end_time, title, description, location)



if __name__ == "__main__":
    main()
