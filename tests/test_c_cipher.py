import pytest
import logging
from src.c_cipher import encrypt

def test_kick_the_back_tires():
    assert encrypt() == 'dbc012'

def test_length_error(caplog):
    """Test that a length error message is logged for invalid email size"""
    with caplog.at_level(logging.INFO):
        result = encrypt("abcd1234")
    assert "Length check failed" in caplog.text
    assert "Email must be 6 characters long." in caplog.text
    assert result == "Length check failed\nEmail must be 6 characters long."
'''    
def test_alphanumeric_error(caplog):
    """Test that an alphanumeric error message is logged for invalid email format"""
    with caplog.at_level(logging.INFO):
        result = encrypt("abcd123")
    assert "alpha num check failed" in caplog.text
    assert "Email must have 3 letters followed by 3 digits." in caplog.text
    assert result == "alpha num check failed\nEmail must have 3 letters followed by 3 digits."

def test_successful_encryption(caplog):
    """Test that the email is encrypted correctly"""
    result = encrypt("abc012")
    assert result == "def345"
    assert "def345" not in caplog.text  # Ensure no logging output for successful encryption
'''

#TODO: when ready to test encrypt remove the '#' from lines 9 - 18
#def test_encrypt_valid_email():
#    assert encrypt("abc123") == "def456"

#def test_encrypt_invalid_size():
#    with pytest.raises(SizeConstraintError):
#        encrypt("abcd123")

#def test_encrypt_invalid_format():
#    with pytest.raises(AlphaNumericError):
#        encrypt("abc12@")

#TODO: when ready to test decrypt remove the '#' from lines 21 - 20
#def test_decrypt_valid_email():
#    assert decrypt("def456") == "abc123"

#def test_decrypt_invalid_size():
#    with pytest.raises(SizeConstraintError):
#        decrypt("def4567")

#def test_decrypt_invalid_format():
#    with pytest.raises(AlphaNumericError):
#        decrypt("abc12@")
