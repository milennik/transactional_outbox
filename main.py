import json
from flask import Flask, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://admin:admin@localhost:54320/outbox"

db = SQLAlchemy(app)


class applications(db.Model):
    id = db.Column("application_id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.INT)


def __init__(self, name, age):
    self.name = name
    self.age = age


@app.route("/")
def seed():
    application = applications(name="nikola", age=35)
    db.session.add(application)
    db.session.commit()
    return (
        json.dumps({"success": True}),
        200,
        {"ContentType": "application/json"},
    )


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
