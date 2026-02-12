from datetime import date
import sqlite3


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

    def creat_event(
        self,
        begin_date,
        end_date,
        begin_time,
        end_time,
        title,
        description,
        location,
    ):
        con = sqlite3.connect(os.path.join(sys.path[0], "calender.db"))
        cursor = con.cursor()

        cursor.execute(
            """
            INSERT INTO events(title, description, location, begin_date, end_date, begin_time, end_time) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (self.title, self.description, self.location, self.begin_date, self.end_date, self.begin_time, self.end_time),
        )
        con.commit()

    def delete_event():
        pass

    def repeat_event():
        pass

    def edit_event():
        pass
