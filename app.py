from flask import Flask, render_template
from mapper.model import db,Student,User
from routers import register_routes
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/student_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id) :
    return User.query.get(int(user_id))
with app.app_context() :
    db.create_all()
    if not User.query.filter_by(username='teacher').first():
        teacher = User(username='teacher', is_teacher=True)
        teacher.password_hash = generate_password_hash('123456')
        db.session.add(teacher)
        db.session.commit()
        print('默认账号 teacher/123456 已创建')

register_routes(app)

@app.route("/")
def index() :
    return render_template("index.html")

@app.route("/home")
def home() :
    return "欢迎进入学生信息管理系统"
if __name__ == "__main__" :
    app.run(debug = True)
    