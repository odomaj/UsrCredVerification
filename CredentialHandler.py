'''
    CredentialHandler.py made by Alexander Odom and Megan Edwards in March 2024
    used for Project 1 in CS 444, Spring 2024

    contains CredentialHandler class, which handles all interactions with credential files
'''

import hashlib
import CredentialHolder

'''
    CredentialHandler class handles all interactions with files that contain credential information
    reads files, and utilizes the CredntialHolder class to update the dictionary with the new information
'''
class CredentialHandler:
    '''
        initializes the CredentialHolder object when
        the class is initialized
    '''
    def __init__(self):
        self.credentialHolder = CredentialHolder.CredentialHolder()

    '''
        takes a credential and encrypts it using the hashlib library
    '''
    def encrypt(self, credential):
        sha256 = hashlib.sha256()
        sha256.update(credential.encode())
        return sha256.hexdigest()

    '''
        takes and email and password, encrypts them, and sends them to the CredentialHolder
        to update the values in the dictionary
    '''
    def insertCredentials(self, email, password):
        self.credentialHolder.insert(self.encrypt(email), self.encrypt(password))

    def splitCredentials(self, line):
        email, password = line.split(':')
        # need to remove enline character
        password = password[:-1]
        return email, password

    '''
        reads every line of a file where the usernames and passwords are split by a ':'
        updates the values of each set of credentials in the dictionary
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
                pass

    '''
        reads every line of all files where the usernames and passwords are split by a ':'
        updates the values of each set of credentials in the dictionary
    '''
    def readCredentialFiles(self, credentialFiles = ['credentials1.txt', 'credentials2.txt'], fileFormat = 'utf8'):
        for file in credentialFiles:
            self.readCredentialFile(file, fileFormat)
            
    def credentialsExist(self, encryptedUsername, encryptedPassword):
        return self.credentialHolder.exists(encryptedUsername, encryptedPassword)