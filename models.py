from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.firstname}', '{self.email}')"

def create_user(firstname, email):
    user = User(firstname=firstname, email=email)
    db.session.add(user)
    db.session.commit()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()
