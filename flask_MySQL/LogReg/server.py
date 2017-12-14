from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLconnector

app = Flask(__name__)
mysql = MYSQLConnector(app,"users_db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def index():







