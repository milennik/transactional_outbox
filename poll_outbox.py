import polling
from models import applications


def check_outbox():
    try:
        new_messages = applications.query.all()
        print(new_messages)
    finally:
        print("done.")


if __name__ == "__main__":
    polling.poll(lambda: check_outbox(), step=5, poll_forever=True)
