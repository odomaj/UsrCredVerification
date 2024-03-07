import hashlib
import os

f = open("credentials1.txt", encoding = "utf8")
lines = f.read().splitlines()

#print(lines)

for l in lines:

    try:
        email,password = l.split(':')
    except ValueError:
        print("Error in format")

    print(email,password)

    sha256 = hashlib.sha256()
    sha256.update(email.encode())
    print(sha256.hexdigest())

    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    print(sha256.hexdigest())