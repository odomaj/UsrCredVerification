from flask import Flask, render_template, request, jsonify
import CredentialHandler


app = Flask(__name__)

enteredCreds = CredentialHandler.CredentialHandler()
print('loading compromised credentials...')
enteredCreds.readCredentialFiles()
print('finished reading credentials')

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

        if enteredCreds.credentialsExist(email, password):
            return "The entered credentials have been compromised"
        return "The entered credentials are not on our list of compromised credentials"
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug = True)