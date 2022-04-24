import os
from google.cloud import pubsub_v1
import polling
from models import applications

creds = "/home/nikola/repos/transactional_outbox/transactional-outbox-private-key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds

publisher = pubsub_v1.PublisherClient()
topic_path = "projects/mpsyt-292223/topics/app-topic-1"


def check_outbox():
    try:
        new_messages = applications.query.all()
        print(new_messages)
        data = "New application created."
        data = data.encode("utf-8")
        attributes = {"name": "Nikola", "age": "35"}
        future = publisher.publish(topic_path, data, **attributes)
        print(f"published message id = {future.result()}")
    finally:
        print("done.")


if __name__ == "__main__":
    polling.poll(lambda: check_outbox(), step=5, poll_forever=True)
