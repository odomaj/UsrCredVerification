'''
    SqlHandler.py made by Alexander Odom and Megan Edwards in March 2024
    used for Project 1 in CS 444, Spring 2024

    contains SqlHandler class, which handles SQL queries
'''

import sqlite3


'''
    SqlHandler class handles all interactions with the SQL database
'''
class SqlHandler:
    def __init__(self, databasePath = "usr_pass.db"):
        self.connection = sqlite3.connect(databasePath)
        self.cursor = self.connection.cursor()
        self.createTable()

    def __del__(self):
        self.cursor.close()

    '''
        Creates a table with the specified table name
        will delete any preexisting table with that name
    '''
    def resetTable(self):
        self.cursor.execute("DROP TABLE IF EXISTS USERS")
        self.cursor.execute("CREATE TABLE USERS ( EMAIL VARCHAR(255) NOT NULL, PASSWORD VARCHAR(255) NOT NULL) ")
        self.connection.commit()

    '''
        Creates a table with the specified table name if it does not exist
        will not delete any preexisting tables
    '''
    def createTable(self):
        listOfTables = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USERS';").fetchall()
        if len(listOfTables) == 0:
            self.cursor.execute("CREATE TABLE USERS ( EMAIL VARCHAR(255) NOT NULL, PASSWORD VARCHAR(255) NOT NULL) ")
            self.connection.commit()

    '''
        inserts the email and passwords into a new row into the table
        does not commit the changes
    '''
    def insertNoSave(self, email, password):
        self.cursor.execute("INSERT INTO USERS VALUES ('" + email + "', '" + password + "')")

    '''
        calls commit to make changes visible to other connections
    '''
    def saveChanges(self):
        self.connection.commit()

    '''
        returns true if the email password pair are located in the table
        otherwise returns false
    '''
    def existInTable(self, email, password):
        return self.cursor.execute("SELECT COUNT(1) FROM USERS WHERE EMAIL='" + email + "' AND PASSWORD='" + password + "'").fetchall()[0][0]

    
    def firstTen(self):
        self.cursor.execute("SELECT *FROM USERS LIMIT 10;")
        result = self.cursor.fetchall()
        for row in result:
            print(row)
            print("\n")


    def tableLength(self):
        numRows = self.cursor.execute("SELECT COUNT(*) FROM USERS;").fetchall()
        print (numRows)