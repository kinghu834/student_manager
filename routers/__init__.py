from routers.route import student_bp
from routers.score import score_bp
from routers.auth import auth_bp
def register_routes(app) :
    app.register_blueprint(student_bp)
    app.register_blueprint(score_bp)
    app.register_blueprint(auth_bp)