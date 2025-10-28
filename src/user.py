class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
import hashlib
import secrets

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.salt = secrets.token_hex(16)  # Генерируем случайную соль
        self.password = self._hash_password(password)
        self.email = email
    
    def _hash_password(self, password):
        # Солим и хешируем пароль
        salted_password = password + self.salt
        return hashlib.sha256(salted_password.encode('utf-8')).hexdigest()
    
    def verify_password(self, password):
        salted_password = password + self.salt
        hashed_input = hashlib.sha256(salted_password.encode('utf-8')).hexdigest()
        return hashed_input == self.password