
from .db import db, environment, SCHEMA, add_prefix_for_prod
from .type import Type
from sqlalchemy.sql import func
from flask_login import current_user
class Room(db.Model):
    __tablename__ = 'rooms'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    createdby = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    type = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('types.id')), nullable=False)
    createdat = db.Column(db.DateTime, server_default=func.now(),default=func.now())
    updatedat = db.Column(db.DateTime, onupdate=func.now(),default=func.now())

    #relationships
    members = db.relationship('Room_Member', backref='room', lazy=True, cascade="all, delete")
    messages = db.relationship('Message', backref='room', lazy=True, cascade="all, delete")

    @property
    def roomtype(self):
        return Type.query.filter(Type.id == self.type).first().name


    @property
    def member_list(self):
        return [roommember.user for roommember in self.members]


    @property
    def message_list(self):
        return [message for message in self.messages]

    def to_dict(self):
        if self.type == 1:
            members = [member.to_dict() for member in self.member_list]
            # get the member that is not the current user
            other_member = [member for member in members if member['id'] != current_user.id][0]

            return {
                'id': self.id,
                'name': self.name,
                'createdby': self.createdby,
                'type': self.type,
                'createdat': self.createdat,
                'updatedat': self.updatedat,
                'user': other_member,
            }
        return {
            'id': self.id,
            'name': self.name,
            'createdby': self.createdby,
            'type': self.type,
            'createdat': self.createdat,
            'updatedat': self.updatedat,
            'roomtype': self.roomtype,
        }
