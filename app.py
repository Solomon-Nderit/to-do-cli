class Task:
    def __init__ (self,id, title, description, due_date, completed):
        self.id = id
        self.title=title
        self.description = description
        self.completed = completed

    def mark_complete(self):
        print(f" This assignment is {self.completed}")

    def to_dict(self):
        pass
