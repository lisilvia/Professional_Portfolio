from flask import Flask, render_template
import os
import smtplib

OWN_EMAIL = os.environ.get("EMAIL")
OWN_PASSWORD = os.environ.get("PASSWORD")

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

if __name__ == "__main__":
    app.run(debug=True)
