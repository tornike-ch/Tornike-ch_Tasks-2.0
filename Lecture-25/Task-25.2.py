from datetime import datetime

class TimestampMixin:
    def __init__(self):
        self._creation_time = datetime.now()
        self._modification_time = self._creation_time

    def get_creation_time(self):
        return self._creation_time

    def get_modification_time(self):
        return self._modification_time

    def update_modification_time(self):
        self._modification_time = datetime.now()

class File(TimestampMixin):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def set_filename(self, filename):
        self.filename = filename
        self.update_modification_time()

class User(TimestampMixin):
    def __init__(self, username):
        super().__init__()
        self.username = username

    def set_username(self, username):
        self.username = username
        self.update_modification_time()

# ფუნქციონალის ტესტი

def main():
    file = File("file.txt")
    user = User("Giorgi")

    print(f"ფაილის შექმნის დრო: {file.get_creation_time()}")
    print(f"მომხმარებლის შექმნის დრო: {user.get_creation_time()}")

    file.set_filename("new_file.txt")
    user.set_username("Daviti")

    print(f"ფაილის ცვლილების დრო: {file.get_modification_time()}")
    print(f"მომხმარებლის ცვლილების დრო: {user.get_modification_time()}")
