import sqlite3
import sys
import os


class Event:

    def __init__(
        self,
        id,
        begin_date,
        end_date,
        begin_time,
        end_time,
        title,
        description,
        location,
    ):
        self.id = id
        self.begin_date = begin_date
        self.end_date = end_date
        self.begin_time = begin_time
        self.end_time = end_time
        self.title = title
        self.description = description
        self.location = location

    def create_event(self):
        con = sqlite3.connect(os.path.join(sys.path[0], "calendar.db"))
        cursor = con.cursor()

        cursor.execute(
            """
            INSERT INTO events(title, description, location, begin_date, end_date, begin_time, end_time) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                self.title,
                self.description,
                self.location,
                self.begin_date,
                self.end_date,
                self.begin_time,
                self.end_time,
            ),
        )
        con.commit()
        con.close()
        print("---Event succesfully added to the calendar database!---")

    def delete_event(self):
        con = sqlite3.connect(os.path.join(sys.path[0], "calendar.db"))
        cursor = con.cursor()

        cursor.execute(
            """
            DELETE FROM events WHERE id = ? AND title = ?  -- Fixed SQL syntax
            """,
            (self.id, self.title),
        )

        if cursor.rowcount > 0:
            con.commit()
            print("---Event successfully deleted from the calendar database!---")
        else:
            print("---No event found with that ID and title!---")

        con.close()

    def repeat_event():
        pass

    def edit_event():
        pass
