def test_create_user_with_valid_data():
    from src.user import User
    
    user = User("test_user", "password123", "test@example.com")
    
    assert user.username == "test_user"
    assert user.password == "password123"
    assert user.email == "test@example.com"
    
def test_register_new_user_success():
    from src.auth import AuthService
    
    auth_service = AuthService()
    user = auth_service.register("new_user", "password123", "user@example.com")
    
    assert user.username == "new_user"
    assert user.email == "user@example.com"
import pytest
from src.exceptions import UsernameAlreadyExists

def test_register_duplicate_username_should_fail():
    from src.auth import AuthService
    
    auth_service = AuthService()
    auth_service.register("duplicate_user", "pass123", "test1@example.com")
    
    with pytest.raises(UsernameAlreadyExists):
        auth_service.register("duplicate_user", "pass456", "test2@example.com")
 
from src.exceptions import WeakPasswordException
def test_register_with_short_password_should_fail():
    from src.auth import AuthService
    
    auth_service = AuthService()
    
    with pytest.raises(WeakPasswordException):
        auth_service.register("short_pass_user", "123", "test@example.com")

from src.exceptions import InvalidEmailException

def test_register_with_invalid_email_should_fail():
    from src.auth import AuthService
    
    auth_service = AuthService()
    
    with pytest.raises(InvalidEmailException):
        auth_service.register("invalid_email_user", "password123", "invalid-email")
def test_login_success():
    from src.auth import AuthService
    
    auth_service = AuthService()
    auth_service.register("login_user", "password123", "login@example.com")
    
    user = auth_service.login("login_user", "password123")
    
    assert user.username == "login_user"
    assert user.email == "login@example.com"