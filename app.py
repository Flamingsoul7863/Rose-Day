from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Correct password
PASSWORD = "Mommy"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_input = request.form.get("password")
        if user_input == PASSWORD:
            return redirect(url_for("lily_flowers"))
        else:
            return render_template("login.html", error="Incorrect password. Try again!")
    return render_template("login.html", error=None)

@app.route("/lily")
def lily_flowers():
    return render_template("lily.html")

@app.route("/tulip")
def tulip_flowers():
    return render_template("tulip.html")

@app.route("/roses")
def roses():
    return render_template("roses.html")

if __name__ == "__main__":
    app.run(debug=True)
# Flask app will be here