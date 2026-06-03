from flask import Flask
from mapper.model import db,Student
from routers import register_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/student_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context() :
    db.create_all()

register_routes(app)

@app.route("/home")
def home() :
    return "欢迎进入学生信息管理系统"
if __name__ == "__main__" :
    app.run(debug = True)
    