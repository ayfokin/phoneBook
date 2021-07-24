import sys

import mysql.connector


class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                user="root",
                password="rootroot",
                host="localhost",
                port=3306,
                database="phone_book"
            )
        except mysql.connector.Error as e:
            print(e)
            sys.exit(1)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def _execute(self, query, variables):
        self.cur.execute(query, variables)

    def addUser(self, username, password, email):
        self._execute("INSERT INTO users VALUES (%s, %s, %s)", (username, password, email))

    def addContact(self, name, phone, birthdate):
        self._execute("INSERT INTO contacts VALUES (%s, %s, %date)", (name, phone, birthdate))

    def deleteContact(self, name, phone, birthdate):
        self._execute("DELETE FROM contacts WHERE name = %s AND phone = %s AND birthdate = %date", (name, phone, birthdate))

    def checkUser(self, username, password=None):
        if password is None:
            self._execute("SELECT 1 FROM users WHERE username = %s", (username,))
        else:
            self._execute("SELECT 1 FROM users WHERE username = %s AND password = %s", (username, password))
        return True if self.cur.fetchall() else False

