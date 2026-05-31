from services.service import add_student,delete_student,update_student,get_student
from flask import Blueprint,request,jsonify
from mapper.model import db,Student

student_bp = Blueprint("student",__name__,url_prefix = "/student")

allow_field = ["id","name","class_name"]
@student_bp.route("",methods = ["POST"])
def add_student_route() :
    data = request.get_json()
    if not data :
        return "无法识别数据，请修改之后再试"
    filter_data = {}
    for field in allow_field :
        if field in data :
            filter_data[field] = data[field]
    result = add_student(filter_data)
    return f"学生信息添加成功,{result}"

@student_bp.route("<int:id>",methods = ["GET"])
def get_student_route(id) :
    if not id :
        return "数据错误，请修改后再重新试试"
    result = get_student(id)
    return f"该学生的信息是{result}"

@student_bp.route("<int:id>",methods = ["PUT"])
def update_student_route(id) :
    if not id :
        return "无法通过id找到相应的学生"
    data = request.get_json()
    update_data = {}
    if not data :
        return "数据错误，请重新上传"
    for field in ["name","class_name"] :
        if field in data :
            update_data[field] = data[field]
    result = update_student(id,update_data)
    return f"学生信息修改成功 : {result}"

@student_bp.route("<int:id>",methods = ["DELETE"])
def delete_student_route(id) :
    if not id :
        return "id不存在,无法找到"
    data = request.get_json()
    delete_data = {}
    for field in ["name","class_name"] :
        if field in data :
            delete_data[field] = data[field]
    result = delete_student(id,delete_data)
    return f"数据删除成功：{result}"









