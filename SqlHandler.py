'''
    SqlHandler.py made by Alexander Odom in March 2024
    used for Project 1 in CS 444, Spring 2024

    contains class SqlHandler, which handles SQL queries
'''

import sqlite3


'''
    SqlHandler class handles all interactions with the SQL database
'''
class SqlHandler:
    def __init__(self, databasePath = "usr_pass.db"):
        self.connection = sqlite3.connect(databasePath)
        self.cursor = self.connection.cursor()