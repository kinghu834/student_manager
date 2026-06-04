from mapper.model import db,User
from werkzeug.security import check_password_hash


def check_login(username,password) :
    user = User.query.filter_by(username = username).first()
    if user and check_password_hash(user.password_hash,str(password)) :
        return user
    else :
        return None

