from sqlalchemy.orm import backref
from . import db

class Role(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref ='role',lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    post = db.Column(db.String(255))

    def save_post(self):
        db.session.add(self)
        db.session.commit()
       
    

    def __repr__(self):
        return f'User {self.name}'

    