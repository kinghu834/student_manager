from flask import Blueprint,request,jsonify
from services.auth import check_login
from flask_login import login_user
auth_bp = Blueprint("auth",__name__,url_prefix = "/auth")

@auth_bp.route("",methods = ["POST"])
def check_login_route() :
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    if not username or not password :
        return "账号或密码不存在，请重新输入"
    result = check_login(username,password)
    if result :
        login_user(result)
        return "登陆成功"
    else :
        return "账号或密码错误，请重新输入"
    


