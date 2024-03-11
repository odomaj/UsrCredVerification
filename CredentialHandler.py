'''
    CredentialHandler.py made by Alexander Odom in March 2024
    used for Project 1 in CS 444, Spring 2024

    contains CredentialHandler class, which handles all interactions with credential files
'''

import hashlib
import SqlHandler
import CredentialHolder

'''
    CredentialHandler class handles all interactions with files that contain credential information
    reads files, and utilizes the SqlHandler class to update the database with the new information
'''
class CredentialHandler:
    '''
        initializes the SqlHandler objects when
        the class is initialized
    '''
    def __init__(self):
        #self.sqlHandler = SqlHandler.SqlHandler()
        self.credentialHolder = CredentialHolder.CredentialHolder()

    '''
        takes a credential and encrypts it using the hashlib library
    '''
    def encrypt(self, credential):
        sha256 = hashlib.sha256()
        sha256.update(credential.encode())
        return sha256.hexdigest()

    '''
        takes and email and password, encrypts them, and sends them to the sqlHandler
        to update the values in the database
        does not call the changes to be commited
    '''
    def insertCredentials(self, email, password):
        #self.sqlHandler.insertNoSave(self.encrypt(email), self.encrypt(password))
        self.credentialHolder.insert(self.encrypt(email), self.encrypt(password))

    def splitCredentials(self, line):
        email, password = line.split(':')
        # need to remove enline character
        password = password[:-1]
        return email, password

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
                email, password = self.splitCredentials(line)
                self.insertCredentials(email, password)
            except ValueError:
                #print("Error in format at line " + str(counter))
                pass

    '''
        reads every line of all files where the usernames and passwords are split by a ':'
        updates the values of each set of credentials in the database
    '''
    def readCredentialFiles(self, credentialFiles = ['credentials1.txt', 'credentials2.txt'], fileFormat = 'utf8'):
        #self.sqlHandler.resetTable()
        for file in credentialFiles:
            self.readCredentialFile(file, fileFormat)
        #self.sqlHandler.saveChanges()
        #print(self.credentialHolder.len)
        #self.sqlHandler.tableLength()
        #self.sqlHandler.firstTen()