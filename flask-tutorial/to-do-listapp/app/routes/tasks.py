# from flask import Blueprint, render_template,request,redirect,url_for,flash,session

# from app import db
# from app.models import Task

# tasks_bp = Blueprint('tasks',__name__)

# @tasks_bp.route('/')
# def view_tasks():
#     if 'user' not in session:
#         return redirect(url_for('auth.login'))
    
#     tasks = Task.query.all()
#     return render_template('tasks.html',task=tasks)


# @tasks_bp.route('/add',method=["POST"])
# def add_tasks():
#     if 'user' not in session:
#         return redirect(url_for('auth.login'))
    
#     title = request.form.get('title')
#     if title:
#         new_task = Task(title=title,status="pending")
#         db.session.add(new_task)
#         db.session.commit()
#         flash('Task added successfully','success')
#     return redirect(url_for('tasks.view_tasks'))

# @tasks_bp.route('/toggle/<int:task_id',methods=["POST"])
# def toggle_status(task_id):
#     task = Task.query.get(task_id)
#     if task:
#         if task.status == "Pending":
#             task.status = "Working"
#         elif task.status == "working":
#             task.status = "Done"
#         else:
#             task.status = "Pending"
#         db.session.commit()
#     return redirect(url_for('tasks.view_tasks'))

# @tasks_bp.route('/clear')
# def clear_tasks():
#     Task.query.delete()
#     db.session.commit()
#     flash('All tasks deleted','info')
#     return redirect(url_for('tasks.view_tasks'))

from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from app import db
from app.models import Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)  # Fixed: should be 'tasks', not 'task'

@tasks_bp.route('/add', methods=["POST"])  # Fixed: 'methods' not 'method'
def add_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status="Pending")  # Consistent status naming
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully', 'success')
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=["POST"])  # Fixed: missing closing parenthesis
def toggle_status(task_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    task = Task.query.get(task_id)
    if task:
        if task.status == "Pending":
            task.status = "Working"
        elif task.status == "Working":  # Fixed: consistent capitalization
            task.status = "Done"
        else:
            task.status = "Pending"
        db.session.commit()
        flash('Task status updated', 'success')
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear')
def clear_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    Task.query.delete()
    db.session.commit()
    flash('All tasks deleted', 'info')
    return redirect(url_for('tasks.view_tasks'))