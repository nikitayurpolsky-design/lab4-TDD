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
 
from src.exceptions import UsernameAlreadyExists, WeakPasswordException

class AuthService:
    def __init__(self):
        self.users = {}
        self.MIN_PASSWORD_LENGTH = 6
    
    def register(self, username, password, email):
        if username in self.users:
            raise UsernameAlreadyExists(f"Username '{username}' already exists")
        
        if len(password) < self.MIN_PASSWORD_LENGTH:
            raise WeakPasswordException(f"Password must be at least {self.MIN_PASSWORD_LENGTH} characters")
        
        from src.user import User
        user = User(username, password, email)
        self.users[username] = user
        return user

from src.exceptions import UsernameAlreadyExists, WeakPasswordException, InvalidEmailException

class AuthService:
    def __init__(self):
        self.users = {}
        self.MIN_PASSWORD_LENGTH = 6
    
    def register(self, username, password, email):
        if username in self.users:
            raise UsernameAlreadyExists(f"Username '{username}' already exists")
        
        if len(password) < self.MIN_PASSWORD_LENGTH:
            raise WeakPasswordException(f"Password must be at least {self.MIN_PASSWORD_LENGTH} characters")
        
        if "@" not in email:
            raise InvalidEmailException("Email must contain '@' symbol")
        
        from src.user import User
        user = User(username, password, email)
        self.users[username] = user
        return user
    
    def login(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == password:
                return user
        return None
from src.exceptions import UsernameAlreadyExists, WeakPasswordException, InvalidEmailException, InvalidCredentialsException

class AuthService:
    def __init__(self):
        self.users = {}
        self.MIN_PASSWORD_LENGTH = 6
    
    def register(self, username, password, email):
        if username in self.users:
            raise UsernameAlreadyExists(f"Username '{username}' already exists")
        
        if len(password) < self.MIN_PASSWORD_LENGTH:
            raise WeakPasswordException(f"Password must be at least {self.MIN_PASSWORD_LENGTH} characters")
        
        if "@" not in email:
            raise InvalidEmailException("Email must contain '@' symbol")
        
        from src.user import User
        user = User(username, password, email)
        self.users[username] = user
        return user
    
    def login(self, username, password):
        if username not in self.users:
            raise InvalidCredentialsException("Invalid username or password")
        
        user = self.users[username]
        if user.password != password:
            raise InvalidCredentialsException("Invalid username or password")
        
        return user
    def change_password(self, username, old_password, new_password):
        user = self.login(username, old_password)  # Проверяем старый пароль
        user.password = new_password  # Меняем на новый
    def change_password(self, username, old_password, new_password):
        if len(new_password) < self.MIN_PASSWORD_LENGTH:
            raise WeakPasswordException(f"Password must be at least {self.MIN_PASSWORD_LENGTH} characters")
        
        user = self.login(username, old_password)
        user.password = new_password
    def delete_account(self, username, password):
        self.login(username, password)  # Проверяем пароль
        del self.users[username]  # Удаляем пользователя