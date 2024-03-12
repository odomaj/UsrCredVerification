from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.get("/")
def indes_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    return('New Message')

if __name__ == "__main__":
    app.run(debug = True)