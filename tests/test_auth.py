def test_create_user_with_valid_data():
    from src.user import User
    
    user = User("test_user", "password123", "test@example.com")
    
    assert user.username == "test_user"
    assert user.password == "password123"
    assert user.email == "test@example.com"