from sqlalchemy import func
from . import db

class user(db.Model):
    __tablename__ = 'users'

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):

        return {
            "userid" : self.userid,
            "username" : self.username
            }