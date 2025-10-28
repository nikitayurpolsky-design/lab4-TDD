class AuthService:
    def __init__(self):
        self.users = {}  # Простая "база данных" в памяти
    
    def register(self, username, password, email):
        from src.user import User
        user = User(username, password, email)
        self.users[username] = user
        return user

from src.exceptions import UsernameAlreadyExists

class AuthService:
    def __init__(self):
        self.users = {}
    
    def register(self, username, password, email):
        if username in self.users:
            raise UsernameAlreadyExists(f"Username '{username}' already exists")
        
        from src.user import User
        user = User(username, password, email)
        self.users[username] = user
        return user