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