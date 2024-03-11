import CredentialHandler

test = CredentialHandler.CredentialHandler()
test.readCredentialFiles()

print('[INFO] Number of unique credentials: ' + str(test.credentialHolder.len))

file = open('credentials1.txt')

line = file.readline()
email, password = test.splitCredentials(line)
print('[INFO] 1st entry: ' + test.encrypt(email) + ':' + test.encrypt(password))

line = file.readline()
email, password = test.splitCredentials(line)
print('[INFO] 2nd entry: ' + test.encrypt(email) + ':' + test.encrypt(password))

line = file.readline()
email, password = test.splitCredentials(line)
print('[INFO] 3rd entry: ' + test.encrypt(email) + ':' + test.encrypt(password))

line = file.readline()
email, password = test.splitCredentials(line)
print('[INFO] 4th entry: ' + test.encrypt(email) + ':' + test.encrypt(password))

line = file.readline()
email, password = test.splitCredentials(line)
print('[INFO] 5th entry: ' + test.encrypt(email) + ':' + test.encrypt(password))

line = file.readline()
email, password = test.splitCredentials(line)
print('[INFO] 6th entry: ' + test.encrypt(email) + ':' + test.encrypt(password))

line = file.readline()
email, password = test.splitCredentials(line)
print('[INFO] 7th entry: ' + test.encrypt(email) + ':' + test.encrypt(password))

line = file.readline()
email, password = test.splitCredentials(line)
print('[INFO] 8th entry: ' + test.encrypt(email) + ':' + test.encrypt(password))

line = file.readline()
email, password = test.splitCredentials(line)
print('[INFO] 9th entry: ' + test.encrypt(email) + ':' + test.encrypt(password))

line = file.readline()
email, password = test.splitCredentials(line)
print('[INFO] 10th entry: ' + test.encrypt(email) + ':' + test.encrypt(password))

line = file.readline()
email, password = test.splitCredentials(line)