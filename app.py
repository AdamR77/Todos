from flask import Flask, request, jsonify, render_template, abort
from flask import make_response, redirect, url_for
from flask_wtf import FlaskForm
from forms import LoginForm
from models import todos
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwerty123"
csrf = CSRFProtect()

username = "adam"
password = "qwerty123"

def create_app():
    app = flask(__name__)
    csrf.init_app(app)


@app.route("/login/", methods = ['GET', "POST"])
@csrf.exempt
def login():
    form = LoginForm()
    if request.method == "POST":
        if (
            form.data.get("username") == username and
            form.data.get("password") == password
            ):
            return "You are logged id"
        else:
            return "Wrong credentials!!"
    return render_template("login.html", form = form)

@app.route("/api/todos/", methods=["GET"])
@csrf.exempt
def todos_api():
    return jsonify(todos.all())

@app.route("/api/todos/", methods=["POST"])
@csrf.exempt
def add_todo():
    if not request.json:
        abort(400)
    todo = {
        'id': todos.all()[-1]['id'] + 1,
        'title': request.json.get('title'),
        'decription': request.json.get('description', ""),
    }
    todos.create(todo)
    return jsonify({'todo': todo}), 201

@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
@csrf.exempt
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
    return render_template("todos.html", form=form, todo_id=todo_id)

@app.route("/todos/<int:todo_id>/", methods=["GET" , "POST"])
@csrf.exempt
def todos_details(todo_id):
    todo = todos.get(todo - 1)
    form = TodoForm(data=todo)

if __name__ == "__main__":
    app.run(debug=True)
