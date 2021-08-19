from . import db
from  flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email = db.Column(db.String(30), unique=True,nullable=False)
    password = db.Column(db.String(80))
    # pi
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f'User{self.username}'
class Pitch (db.Model):
    __tablename__= "pitchs"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    message = db.Column(db.String(), unique=True,nullable=False)
    category = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    