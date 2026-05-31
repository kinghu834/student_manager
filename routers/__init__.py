from routers.route import student_bp
from routers.score import score_bp
def register_routes(app) :
    app.register_blueprint(student_bp)
    app.register_blueprint(score_bp)