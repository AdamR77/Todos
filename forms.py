from collections import namedtuple
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

@app.route("/todos/<int:todo_id>/", methods=["GET" , "POST"])
def todos_details(todo_id):
    todo = todos.get(todo - 1)
    form = TodoForm(data=todo)



