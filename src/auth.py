class AuthService:
    def __init__(self):
        self.users = {}  # Простая "база данных" в памяти
    
    def register(self, username, password, email):
        from src.user import User
        user = User(username, password, email)
        self.users[username] = user
        return user