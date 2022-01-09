import json

class Todos:
    def __init__(self):
        try:
            with open("todos.json","r") as f:
                self.todos = json.load(f)
        except FileNotFoundError:
            self.todos = []

    def all(self):
        return self.todos

    def get(self, id):
        todo = [ todo for todo in self.all() if ['id'] == id]
        if todo:
            return todos[0]
        return self.todos[id]

    def create(self, data):
        #data.pop('csrf.token')
        self.todos.append(data)

    def save_all(self):
        with open("todos.json", "w") as f:
            json.dump(self.todos, f)

    def update(self):
        data.pop("csrf_token")
        self.todos[id] = data
        self.save_all()


todos = Todos()





