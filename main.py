from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import smtplib

# OWN_EMAIL = os.environ.get("EMAIL")
# OWN_PASSWORD = os.environ.get("PASSWORD")
OWN_EMAIL = os.getenv("EMAIL")
OWN_PASSWORD = os.getenv("PASSWORD")
load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/aboutme", methods=["GET", "POST"])
def aboutme():
    return render_template('aboutme.html')


if __name__ == "__main__":
    app.run(debug=True)
