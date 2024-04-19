import flask
import os
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from flask_bootstrap import Bootstrap5
import gunicorn


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

Bootstrap5(app)


@app.route("/")
def home():
    with open("static/files/security-skills.txt") as file:
        general_skills = file.readlines()

    with open("static/files/python-skills.txt") as file:
        python_skills = file.readlines()

    with open("static/files/Certifications.txt") as file:
        certifications = file.readlines()
    return render_template("index.html",
                           skill1=general_skills,
                           skill2=python_skills,
                           certs=certifications)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/HTB-writeups")
def htb():
    return render_template("HTB.html")

@app.route("/projects")
def projects():
    return render_template("coding-projects.html")


if __name__ == "__main__":
    app.run(debug=False)


