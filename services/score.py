from mapper.model import db,Score,Student

def add_score(add_data) :
    score = Score()
    for field in ["student_id","subject","score"] :
        setattr(score,field,add_data[field])
    db.session.add(score)
    db.session.commit()
    return {
        "success" : True,
        "message" : "成绩录入成功",
        "student_id" : score.student_id,
        "add_data" : add_data
    }
    

def get_score(student_id) :
    scores = Score.query.filter_by(student_id = student_id).all()
    student = Student.query.get(student_id)
    score_list = []
    for s in scores:
        score_list.append({
            "subject": s.subject,
            "score": s.score,
            "student_id" : s.student_id
        })
    return {
        "success" : True,
        "message" : "查询成功",
        "name" : student.name,
        "score_list" : score_list
    }

def update_score(student_id, subject, update_data) :
    score_record = Score.query.filter_by(student_id=student_id, subject=subject).first()
    if not score_record:
        return {"success": False, "message": "成绩记录不存在"}
    for field in ["score"] :
        setattr(score_record, field, update_data[field])
    db.session.commit()
    return {
        "success": True,
        "update_data": update_data
    }
def get_score_avg(student_id) :
    scores_list = Score.query.filter_by(student_id = student_id).all()
    subject_num = len(scores_list)
    scores = [s.score for s in scores_list]
    total = sum(scores)
    avg = total / subject_num
    return {
        "avg" : avg
    }
    
    
