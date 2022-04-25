import json
from models import applications, outbox
from app import app, db
import uuid


@app.route("/")
def seed():
    application = applications(id=uuid.uuid4(), name="nikola", age=35)
    db.session.add(application)

    ob = outbox(
        domain="application",
        domain_id=application.id,
        type="app created",
        payload=application.to_dict(),
        status="Created",
        try_count=0,
    )
    db.session.add(ob)

    db.session.commit()

    return (
        json.dumps({"success": True}),
        200,
        {"ContentType": "application/json"},
    )


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
