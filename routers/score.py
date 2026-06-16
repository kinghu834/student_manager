from flask import Blueprint,request,jsonify
from mapper.model import db,Score,Student
from services.score import add_score,get_score,get_score_avg,update_score

score_bp = Blueprint("score",__name__,url_prefix = "/score")

allow_field = ["student_id","subject","score"]
@score_bp.route("",methods = ["POST"])
def add_score_route() :
    data = request.get_json()
    if not data :
        return "数据不匹配，请重新输入"
    add_data = {}
    for field in allow_field :
        if field in data :
            add_data[field] = data[field]
    result = add_score(add_data)
    return f"成绩录入成功：{result}"

@score_bp.route("/<int:student_id>",methods = ["GET"])
def get_score_route(student_id) :
    if not student_id :
        return "id错误,请重新输入"
    result = get_score(student_id)
    return f"查询结果：{result}"

@score_bp.route("/<int:student_id>/<subject>",methods = ["PUT"])
def update_score_route(student_id, subject) :
    if not student_id :
        return "id错误,请重新上传"
    data = request.get_json()
    if not data :
        return "数据错误，请重新输入"
    update_data = {"subject": subject}
    for field in ["score"] :
        if field in data :
            update_data[field] = data[field]
    result = update_score(student_id, subject, update_data)
    return f"学生数据修改完成：{result}"

@score_bp.route("/<int:student_id>/get_avg",methods = ["GET"])
def get_score_avg_route(student_id) :
    if not student_id :
        return "id错误,请重新输入"
    result = get_score_avg(student_id)
    return f"成绩统计结果：{result}"