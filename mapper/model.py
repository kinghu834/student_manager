from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Student(db.Model) :
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50))
     class_name = db.Column(db.String(50))

class Score(db.Model) :
      id = db.Column(db.Integer, primary_key=True)
      student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
      subject = db.Column(db.String(50))
      score = db.Column(db.Integer)


