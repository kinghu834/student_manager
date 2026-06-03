from mapper.model import db,Score,Student


def add_student(filter_data) :
    student = Student()
    for field in ["name","class_name"] :
        setattr(student,field,filter_data[field])
    db.session.add(student)
    db.session.commit()
    return [{
        "name" : student.name,
        "class_name" : student.class_name
    }]
    

def get_student(id) :
    student = Student.query.get(id)
    return {
        "id" : student.id,
        "name" : student.name,
        "class_name" : student.class_name
    }

def update_student(id,update_data) :
    student = Student.query.get(id)
    for field in ["name","class_name"] :
        setattr(student,field,update_data[field])
    db.session.commit()
    return {
        "success" : True,
        "message" : "学生信息修改成功",
        "update_data" : update_data,
        "id" : student.id
    }
    

def delete_student(id,delete_data) :
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return {
        "success" : True,
        "message" : "学生信息删除成功",
        "id" : student.id,
        "delete_data" : delete_data
    }
    