'''
    CredentialHandler.py made by Alexander Odom in March 2024
    used for Project 1 in CS 444, Spring 2024

    contains CredentialHandler class, which handles all interactions with credential files
'''

import hashlib
import SqlHandler

'''
    CredentialHandler class handles all interactions with files that contain credential information
    reads files, and utilizes the SqlHandler class to update the database with the new information
'''
class CredentialHandler:
    '''
        initializes the hashing and SqlHandler objects when
        the class is initialized
    '''
    def __init__(self):
        self.sha256 = hashlib.sha256()
        self.sqlHanlder = SqlHandler.SqlHandler()

    '''
        takes a credential and encrypts it using the hashlib library
    '''
    def encrypt(self, credential):
        self.sha256.update(credential.encode())
        return self.sha256.hexdigest()

    '''
        takes and email and password, encrypts them, and sends them to the sqlHandler
        to update the values in the database
    '''
    def updateCredentials(self, email, password):
        self.sqlHanlder.updateTable(self.encrypt(email), self.encrypt(password))

    '''
        reads every line of a file where the usernames and passwords are split by a ':'
        updates the values of each set of credentials in the database
    '''
    def readCredentialFile(self, credentialFile, fileFormat):
        file = open(credentialFile, encoding = fileFormat, mode = 'r')
        counter = 0
        while True:
            line = file.readline()
            counter += 1
            if not line:
                break
            try:
                email, password = line.split(':')
                # need to remove endline character from password
                password = password[:-1]
                self.updateCredentials(email, password)
            except ValueError:
                print("Error in format at line " + str(counter))

    '''
        reads every line of all files where the usernames and passwords are split by a ':'
        updates the values of each set of credentials in the database
    '''
    def readCredentialFiles(self, credentialFiles = ['credentials1.txt', 'credentials2.txt'], fileFormat = 'utf8'):
        for file in credentialFiles:
            self.readCredentialFile(file, fileFormat)