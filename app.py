import os
import requests

from flask import Flask, render_template, session, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


# Check for environment variable !!!!!!!!!!!!!!!!!
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


# Configure session to use filesystem
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))



app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/logged_in", methods=['POST'])
def logged_in():
    return render_template("logged_in.html")

@app.route("/create_acc")
def create_acc():
    return render_template("create_acc.html")

@app.route("/process_data", methods=['POST']) #TODO: Continue  treating the data to redirect to correct page!!!
def process_data():
    error = "All fine"
    error_bool = False
    new_user = request.form.get("new_user")
    password_reg = request.form.get("password_reg")

    users_list = db.execute("SELECT * FROM users").fetchall()

    for a in users_list:
        b = a.username
        if b == new_user:
            error = "Userna already in use"
            error_bool = True
            break



    #db.execute("INSERT INTO users (username , password) VALUES ('%s','%s')"%(new_user,password_reg))
    #db.commit()


    return error
