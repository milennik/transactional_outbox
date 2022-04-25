from app import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_serializer import SerializerMixin


class CustomSerializerMixin(SerializerMixin):
    serialize_types = ((UUID, lambda x: str(x)),)


class applications(db.Model, CustomSerializerMixin):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100))
    age = db.Column(db.INT)


class outbox(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    domain = db.Column(db.String(100))
    domain_id = db.Column(db.String(100))
    type = db.Column(db.String(100))
    payload = db.Column(db.JSON)
    status = db.Column(db.String(50))
    try_count = db.Column(db.Integer)
