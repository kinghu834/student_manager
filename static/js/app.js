// API基础URL
const API_BASE = '';

// 显示消息
function showMessage(text, type = 'info') {
    const message = document.getElementById('message');
    message.textContent = text;
    message.className = `message ${type} show`;
    
    setTimeout(() => {
        message.classList.remove('show');
    }, 3000);
}

// 切换显示区域
function showSection(section) {
    document.querySelectorAll('.section').forEach(s => s.style.display = 'none');
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    
    document.getElementById(`${section}-section`).style.display = 'block';
    event.target.classList.add('active');
}

// 添加学生
document.getElementById('add-student-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const name = document.getElementById('student-name').value;
    const className = document.getElementById('student-class').value;
    
    try {
        const response = await fetch(`${API_BASE}/student`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name,
                class_name: className
            })
        });
        
        const result = await response.text();
        showMessage(result, 'success');
        
        document.getElementById('student-name').value = '';
        document.getElementById('student-class').value = '';
    } catch (error) {
        showMessage('添加学生失败: ' + error.message, 'error');
    }
});

// 查询学生
document.getElementById('search-student-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const studentId = document.getElementById('search-student-id').value;
    const infoDiv = document.getElementById('student-info');
    
    try {
        const response = await fetch(`${API_BASE}/student/${studentId}`, {
            method: 'GET'
        });
        
        const result = await response.text();
        
        try {
            const data = JSON.parse(result.match(/\{[\s\S]*\}/)[0]);
            infoDiv.innerHTML = `
                <p><strong>学生ID:</strong> ${data.id}</p>
                <p><strong>姓名:</strong> ${data.name}</p>
                <p><strong>班级:</strong> ${data.class_name}</p>
            `;
        } catch {
            infoDiv.innerHTML = `<p>${result}</p>`;
        }
    } catch (error) {
        showMessage('查询学生失败: ' + error.message, 'error');
    }
});

// 修改学生
document.getElementById('update-student-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const id = document.getElementById('update-student-id').value;
    const name = document.getElementById('update-name').value;
    const className = document.getElementById('update-class').value;
    
    try {
        const response = await fetch(`${API_BASE}/student/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name,
                class_name: className
            })
        });
        
        const result = await response.text();
        showMessage(result, 'success');
        
        document.getElementById('update-student-id').value = '';
        document.getElementById('update-name').value = '';
        document.getElementById('update-class').value = '';
    } catch (error) {
        showMessage('修改学生失败: ' + error.message, 'error');
    }
});

// 删除学生
document.getElementById('delete-student-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const id = document.getElementById('delete-student-id').value;
    
    if (!confirm('确定要删除这个学生吗?此操作不可恢复！')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/student/${id}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        });
        
        const result = await response.text();
        showMessage(result, 'success');
        
        document.getElementById('delete-student-id').value = '';
    } catch (error) {
        showMessage('删除学生失败: ' + error.message, 'error');
    }
});

// 录入成绩
document.getElementById('add-score-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const studentId = document.getElementById('score-student-id').value;
    const subject = document.getElementById('score-subject').value;
    const score = document.getElementById('score-value').value;
    
    try {
        const response = await fetch(`${API_BASE}/score`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                student_id: parseInt(studentId),
                subject: subject,
                score: parseInt(score)
            })
        });
        
        const result = await response.text();
        showMessage(result, 'success');
        
        document.getElementById('score-student-id').value = '';
        document.getElementById('score-subject').value = '';
        document.getElementById('score-value').value = '';
    } catch (error) {
        showMessage('录入成绩失败: ' + error.message, 'error');
    }
});

// 查询成绩
document.getElementById('search-score-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const studentId = document.getElementById('search-score-student-id').value;
    const infoDiv = document.getElementById('score-info');
    
    try {
        const response = await fetch(`${API_BASE}/score/${studentId}`, {
            method: 'GET'
        });
        
        const result = await response.text();
        
        try {
            const data = JSON.parse(result.match(/\{[\s\S]*\}/)[0]);
            let html = `<p><strong>学生姓名:</strong> ${data.name}</p>`;
            
            if (data.score_list && data.score_list.length > 0) {
                html += `
                    <table>
                        <thead>
                            <tr>
                                <th>科目</th>
                                <th>分数</th>
                            </tr>
                        </thead>
                        <tbody>
                `;
                
                data.score_list.forEach(score => {
                    html += `
                        <tr>
                            <td>${score.subject}</td>
                            <td>${score.score}</td>
                        </tr>
                    `;
                });
                
                html += '</tbody></table>';
            } else {
                html += '<p>暂无成绩记录</p>';
            }
            
            infoDiv.innerHTML = html;
        } catch {
            infoDiv.innerHTML = `<p>${result}</p>`;
        }
    } catch (error) {
        showMessage('查询成绩失败: ' + error.message, 'error');
    }
});

// 计算平均分
document.getElementById('avg-score-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const studentId = document.getElementById('avg-student-id').value;
    const infoDiv = document.getElementById('avg-info');
    
    try {
        const response = await fetch(`${API_BASE}/score/${studentId}/get_avg`, {
            method: 'GET'
        });
        
        const result = await response.text();
        
        try {
            const data = JSON.parse(result.match(/\{[\s\S]*\}/)[0]);
            infoDiv.innerHTML = `
                <p><strong>平均分:</strong> ${data.avg.toFixed(2)}</p>
            `;
        } catch {
            infoDiv.innerHTML = `<p>${result}</p>`;
        }
    } catch (error) {
        showMessage('计算平均分失败: ' + error.message, 'error');
    }
});
