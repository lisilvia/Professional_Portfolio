# from flask import Flask, render_template, redirect, url_for, flash
# from flask_bootstrap import Bootstrap
# from flask_ckeditor import CKEditor
# from datetime import date
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship
# from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
# from forms import CreatePostForm
# from flask_gravatar import Gravatar

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
