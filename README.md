"""
Rixsor — Smart Dashboard
A tiny, dependency-light Flask app.

There's no login and no database: the To-Do list and Quick Notes
live in the visitor's browser (localStorage), so the backend's only
job is to serve the page. Kept intentionally minimal and clean.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
