from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class Student(db.Model) :
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50))
     class_name = db.Column(db.String(50))

class Score(db.Model) :
      id = db.Column(db.Integer, primary_key=True)
      student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
      subject = db.Column(db.String(50))
      score = db.Column(db.Integer)

class User(UserMixin, db.Model):
     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     username = db.Column(db.String(50), unique=True, nullable=False)
     password_hash = db.Column(db.String(255), nullable=False)
     is_teacher = db.Column(db.Boolean, default=True)