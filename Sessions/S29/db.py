import sqlite3
from pathlib import Path


class Database:

    def __init__(self, db_file_path: Path, create_table_query: str) -> None:
        self.connection = sqlite3.connect(db_file_path)
        self.cursor = self.connection.cursor()
        self.create_table_query = create_table_query
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS 'users'(
	            "number" INTEGER NOT NULL PRIMARY KEY UNIQUE,
	            "name" TEXT NOT NULL
            );"""
        )
        self.connection.commit
        
        # exectutati o metoda care creaza tabelul pe baza queryului

    # def create_db(self):
    #     table = self.cursor.execute(
    #         """CREATE TABLE "users" IF NOT EXISTS (
	#             "phone number"	INTEGER NOT NULL PRIMARY KEY UNIQUE,
	#             "name"	TEXT
    #         );"""
    #     )
    def create(self, name, number):
        self.name = name
        self.number = number

    def read_all(self):
        rows = self.cursor.execute(
            """SELECT * FROM ?;""", (self.table)) # numele tabelului se extrage din query de creare tabel
        return rows.fetchall()

    def update(self):
        return self.cursor.execute("""INSERT INTO "users" (number, name) VALUES (0745282461, "Ion");""")
    
    def delete(self):
        return self.cursor.execute("""UPDATE users SET  name = "Dan" WHERE number == "0745282461";""")
    
    # def create(self, name, tel)

    # def update

    # def delete

class ContactsDb:
    pass