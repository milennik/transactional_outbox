import json
from models import applications
from app import app, db


@app.route("/")
def seed():
    application = applications(name="nikola", age=35)
    db.session.add(application)
    application = applications(name="jelena", age=30)
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
