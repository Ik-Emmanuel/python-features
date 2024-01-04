# ===================== old 
import logging
import sqlite3


class SQLite:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.connection = sqlite3.connect(self.file_name)

    def __enter__(self):
        logging.info("Calling __enter__")
        return self.connection.cursor()

    def __exit__(self, error: Exception, value: object, traceback: object):
        logging.info("Calling __exit__")
        self.connection.commit()
        self.connection.close()


def main():
    logging.basicConfig(level=logging.INFO)
    with SQLite(file_name="application.db") as cursor:
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())



# ============================== new
        
import logging
import sqlite3
from contextlib import contextmanager


@contextmanager
def open_db(file_name: str):
    conn = sqlite3.connect(file_name)
    try:
        logging.info("Creating connection")
        yield conn.cursor()
    finally:
        logging.info("Closing connection")
        conn.commit()
        conn.close()


def main_2():
    logging.basicConfig(level=logging.INFO)
    with open_db(file_name="application.db") as cursor:
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())

if __name__ == "__main__":
    main_2()
