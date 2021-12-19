from flask import Flask, request, jsonify, render_template
from flask import make_response, redirect, url_for
from flask_wtf import FlaskForm
from forms import LoginForm, TodoForm
from models import todos

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


app = Flask(__name__)
app.config["SECRET_KEY"] = "qwerty123"

@app.route("/login/")
def login():
    form = LoginForm()
    if request.method == "POST":
        if (
            form.username.data == user.username and
            form.password.data == user.password
            ):
            return "You are logged id"
        else:
            return "Wrong credentials!!"
    return render_template("login.html", form = form)

@app.route("/api/todos/", methods=["GET"])
def todos_api():
    return jsonify(todos.all())

@app.route("/api/todos/", methods=["POST"])
def add_todo():
    if not request.json or not 'todo' in request.json:
        abort(400)
    todo = {
        'id': todos.all()[-1]['id'] + 1,
        'todo': request.json.get['todo'],
        'decription': request.json.get('description', ""),
    }
    todos.create(todo)
    return jsonify({'todo': todo}), 201

@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
def get_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        abort(404)
    return jsonify({'todo:': todo})

    form = TodoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            todos.create(form.data)
            todos.save_all()
        return redirect(url_for("todos_list"))



    return render_template("todos.html", form=form, todos=todos.all(), error=error)


    if request.method == "POST":
        if form.validate_on_submit():
            todos.update(todo_id - 1, form.data)
        return redirect(url_for("todos_list"))
    return render_template("todo.html", form=form, todo_id=todo_id)


if __name__ == "__main__":
    app.run(debug=True)