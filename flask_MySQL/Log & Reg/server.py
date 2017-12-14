from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLconnector

app = Flask(__name__)
mysql = MYSQLConnector(app,"users_db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if len(request.form['first']) < 1:
        errors.append ("First name MUST be completed")
    elif len request.form ['first']) < 2:    
        errors.append ("First name MUST be longer than 1 letters.")

    if len(request.form['last']) < 1:
        errors.append("Last name MUST be longer than 1 letters")
    elif len request.form ['last']) < 2:
        errors.append ("Last name MUST be long than 1 letters.")

    if len(request.form['']) < 1:
        errors.append("Email MUST be completed")
    elif errors.append(                    )

    for error in errors:
    flash (error)

    if errors == []:
        query = "INSERT INTO users (first_name, last_name, e-mail, password, 
            created_at, updated_at) VALUES (:first, :last,:email, :password, NOW()
            , NOW())"

        print errors
        return redirect("/")
app.run(debug=True)







