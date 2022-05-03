import os
from google.cloud import pubsub_v1
import polling
from models import outbox
from app import db

creds = "/home/nikola/repos/transactional_outbox/transactional-outbox-private-key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds

publisher = pubsub_v1.PublisherClient()
topic_path = "projects/mpsyt-292223/topics/app-topic-1"


def check_outbox():
    try:
        new_messages = db.session.query(outbox).filter_by(status="Created")
        for m in new_messages:
            m.status = "Published"
            m.try_count += 1
            attributes = m.payload
            data = f"New application created {attributes['id']}"
            data = data.encode("utf-8")
            attributes["age"] = str(attributes["age"])
            attributes["guid"] = str(attributes["id"])
            future = publisher.publish(topic_path, data, **attributes)
            print(f"published message id = {future.result()}")

        db.session.commit()
    finally:
        print("done.")


if __name__ == "__main__":
    polling.poll(lambda: check_outbox(), step=5, poll_forever=True)
