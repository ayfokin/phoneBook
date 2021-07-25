import json
import sys

import mysql.connector


class Database:
    def __init__(self):
        with open("conf.json", "r") as config_file:
            config = json.load(config_file)
        try:
            self.conn = mysql.connector.connect(
                user=config["user"],
                password=config["password"],
                host=config["host"],
                port=config["port"],
                database=config["database"]
            )
        except mysql.connector.Error as e:
            print(e)
            sys.exit(1)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def _execute(self, query, variables=None):
        self.cur.execute(query, variables)

    def addUser(self, username, password, email):
        self._execute("INSERT INTO users VALUES (%s, %s, %s)", (username, password, email))

    def addContact(self, name, phone, birthdate):
        self._execute("INSERT INTO contacts VALUES (%s, %s, DATE %s)", (name, phone, birthdate))

    def deleteContact(self, name, phone, birthdate):
        self._execute("DELETE FROM contacts WHERE name = %s AND phone = %s AND birthdate = DATE %s", (name, phone, birthdate))

    def editContact(self, name, phone, birthdate, new_name, new_phone, new_birthdate):
        self._execute("UPDATE contacts SET name = %s, phone = %s, birthdate = %s "
                      "WHERE name = %s AND phone = %s AND birthdate = DATE %s",
                      (new_name, new_phone, new_birthdate, name, phone, birthdate))

    def checkUser(self, username, password=None):
        if password is None:
            self._execute("SELECT 1 FROM users WHERE username = %s", (username,))
        else:
            self._execute("SELECT 1 FROM users WHERE username = %s AND password = %s", (username, password))
        return True if self.cur.fetchall() else False

    def selectContacts(self):
        self._execute("SELECT * FROM contacts ORDER BY name")
        return self.cur.fetchall()

