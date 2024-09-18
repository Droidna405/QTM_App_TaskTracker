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


import os
import logging
from flask import Flask, redirect, render_template, request
from core.services import create_task, view_tasks  # type: ignore


# Initialize the Flask application
app = Flask(__name__)


# Set up logging
logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)


# Configuration management
app.config['HOST'] = os.getenv('FLASK_HOST', '0.0.0.0')
app.config['PORT'] = int(os.getenv('FLASK_PORT', 5000))


# Define routes
@app.route('/')
def home():
    try:
        tasks = view_tasks()
    except Exception as e:
        # Log the error and return an error page or message
        app.logger.error(f"Error fetching tasks: {e}")
        return render_template('error.html', message="Error fetching tasks")
    return render_template('index.html', tasks=tasks)


@app.route('/create', methods=['POST'])
def create():
    task_name = request.form.get('task_name', '').strip()
    if not task_name:
        return render_template('error.html', message="Task name cannot be empty")
    try:
        create_task(task_name)
    except Exception as e:
        # Log the error and return an error page or message
        app.logger.error(f"Error creating task: {e}")
        return render_template('error.html', message="Error creating task")
    return redirect('/')


# Run the app
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])