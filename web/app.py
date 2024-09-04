#!/usr/bin/env python3
"""
web.app
=======

This module serves as the entry point for the QTM web application.
It provides the routes and views for users to interact with the QTM system
through a web interface.

Routes:
    /: Displays the user's task list.
    /create: Allows the user to create a new task.
"""


from flask import Flask, render_template
from core.services import create_task, view_tasks


app = Flask(__name__)


@app.route('/')
def home():
    tasks = view_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/create', methods=['POST'])
def create():
    task_name = request.form['task_name']
    create_task(task_name)
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
