import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # nopa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEM_DATABASE_URL"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes  # nopa