import os
import json
import sqlite3

from flask import Flask, render_template, request

def save_signup(signup):
    con = sqlite3.connect("signups.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO signups(name,workshop) VALUES(?,?);",
        (signup["name"], signup["workshop"]),
    )
    con.commit()
    return

def get_signups():
    con = sqlite3.connect("signups.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM signups;")
    rows = cur.fetchall()

    return rows

def read_menu(filename):
    f = open(filename)
    temp = f.readlines()
    result = []
    for item in temp:
        new_item = item.strip()
        result.append(new_item)

    return result

workshops = read_menu("workshops.txt")
flavors = read_menu("flavors.txt")
toppings = read_menu("toppings.txt")

con = sqlite3.connect("signups.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS signups(name, workshop, flavor, topping);")


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/<name>")
def greet(name="Stranger"):
    return render_template("greeting.html", name=name)

@app.route("/signup", methods=("GET", "POST"))
def signup():
    if request.method == "POST":
        new_signup = {"name": request.form["name"],
                     "workshop": request.form["workshop"]
                     }
        save_signup(new_signup)
        return render_template(
            "print.html", new_signup=new_signup
        )

    return render_template("signup.html", workshops=workshops)

@app.route("/list", methods=["GET"])
def list():
    signups = get_signups()

    return render_template("list.html", signups=signups)
