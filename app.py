from flask import Flask, render_template, request, jsonify
import CredentialHandler
import time

app = Flask(__name__)

enteredCreds = CredentialHandler.CredentialHandler()
print('loading compromised credentials...')
loadStartTime = time.time()
enteredCreds.readCredentialFiles()
loadEndTime = time.time()
print('finished reading credentials in ' + str(loadEndTime - loadStartTime) + ' seconds')

@app.route("/", methods = ["GET", "POST"])
def gfg():
    if request.method == "POST":
        #getting input with email = email in HTML form
        email = request.form.get("email")
        #getting input with password = password in HTML form
        password = request.form.get("password")

        #hashes the email and password
        email = enteredCreds.encrypt(email)
        password = enteredCreds.encrypt(password)

        startTime = time.time()
        credentialsExist = enteredCreds.credentialsExist(email, password)
        endTime = time.time()
        if credentialsExist:
            return 'The entered credentials have been compromised. (result found in ' + str((endTime - startTime) * 1000) + ' milliseconds)'
        return 'The entered credentials are not on our list of compromised credentials. (result found in ' + str((endTime - startTime) * 1000) + ' milliseconds)'
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug = True)