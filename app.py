from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://admin:admin@localhost:54320/outbox"

db = SQLAlchemy(app)
