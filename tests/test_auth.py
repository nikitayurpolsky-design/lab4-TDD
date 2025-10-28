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

from src.exceptions import InvalidCredentialsException

def test_login_with_wrong_password_should_fail():
    from src.auth import AuthService
    
    auth_service = AuthService()
    auth_service.register("wrong_pass_user", "password123", "test@example.com")
    
    with pytest.raises(InvalidCredentialsException):
        auth_service.login("wrong_pass_user", "wrong_password")
def test_login_with_nonexistent_username_should_fail():
    from src.auth import AuthService
    
    auth_service = AuthService()
    
    with pytest.raises(InvalidCredentialsException):
        auth_service.login("nonexistent_user", "password123")
def test_change_password_success():
    from src.auth import AuthService
    
    auth_service = AuthService()
    auth_service.register("change_pass_user", "old_password", "test@example.com")
    
    # Меняем пароль
    auth_service.change_password("change_pass_user", "old_password", "new_password")
    
    # Проверяем, что старый пароль не работает
    with pytest.raises(InvalidCredentialsException):
        auth_service.login("change_pass_user", "old_password")
    
    # Проверяем, что новый пароль работает
    user = auth_service.login("change_pass_user", "new_password")
    assert user.username == "change_pass_user"
def test_change_password_with_wrong_old_password_should_fail():
    from src.auth import AuthService
    
    auth_service = AuthService()
    auth_service.register("wrong_old_pass_user", "correct_old", "test@example.com")
    
    with pytest.raises(InvalidCredentialsException):
        auth_service.change_password("wrong_old_pass_user", "wrong_old", "new_password")
def test_change_password_with_weak_new_password_should_fail():
    from src.auth import AuthService
    
    auth_service = AuthService()
    auth_service.register("weak_new_pass_user", "old_strong_pass", "test@example.com")
    
    with pytest.raises(WeakPasswordException):
        auth_service.change_password("weak_new_pass_user", "old_strong_pass", "123")
def test_delete_account_success():
    from src.auth import AuthService
    
    auth_service = AuthService()
    auth_service.register("delete_user", "password123", "test@example.com")
    
    # Удаляем аккаунт
    auth_service.delete_account("delete_user", "password123")
    
    # Проверяем, что вход невозможен
    with pytest.raises(InvalidCredentialsException):
        auth_service.login("delete_user", "password123")
def test_password_is_hashed_in_storage():
    from src.auth import AuthService
    
    auth_service = AuthService()
    user = auth_service.register("hashed_user", "password123", "test@example.com")
    
    # Пароль в хранилище должен быть хешированным (не исходным)
    stored_user = auth_service.users["hashed_user"]
    assert stored_user.password != "password123"
    # Проверяем, что пароль представляет собой хеш (шестнадцатеричная строка)
    assert len(stored_user.password) == 64  # Длина SHA-256 хеша
    assert all(c in '0123456789abcdef' for c in stored_user.password)
def test_find_user_by_username():
    from src.auth import AuthService
    
    auth_service = AuthService()
    auth_service.register("find_user", "password123", "find@example.com")
    
    user = auth_service.find_by_username("find_user")
    assert user.username == "find_user"
    assert user.email == "find@example.com"
    
    # Поиск несуществующего пользователя
    nonexistent = auth_service.find_by_username("nonexistent")
    assert nonexistent is None
def test_complete_user_lifecycle():
    from src.auth import AuthService
    
    auth_service = AuthService()
    
    # 1. Регистрация
    user = auth_service.register("lifecycle_user", "initial_pass", "lifecycle@example.com")
    assert user.username == "lifecycle_user"
    
    # 2. Вход
    logged_in_user = auth_service.login("lifecycle_user", "initial_pass")
    assert logged_in_user.username == "lifecycle_user"
    
    # 3. Смена пароля
    auth_service.change_password("lifecycle_user", "initial_pass", "new_strong_pass")
    
    # 4. Повторный вход с новым паролем
    relogged_user = auth_service.login("lifecycle_user", "new_strong_pass")
    assert relogged_user.username == "lifecycle_user"
    
    # 5. Удаление аккаунта
    auth_service.delete_account("lifecycle_user", "new_strong_pass")
    
    # 6. Проверка, что аккаунт удален
    with pytest.raises(InvalidCredentialsException):
        auth_service.login("lifecycle_user", "new_strong_pass")