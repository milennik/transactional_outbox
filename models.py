from app import db


class applications(db.Model):
    id = db.Column("application_id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.INT)
