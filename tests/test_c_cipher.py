import pytest
from io import StringIO
import sys
from src.c_cipher import encrypt

def test_kick_the_back_tires():
    assert encrypt() == 'dbc012'

@pytest.fixture
def capture_output():
    """Fixture to capture stdout"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    yield sys.stdout
    sys.stdout = old_stdout

def test_length_error(capture_output):
    """Test that an error message is printed for invalid email size"""
    encrypt("abcd1234")
    output = capture_output.getvalue().strip()
    expected_output = "Length check failed\nEmail must be 6 characters long."
    assert output == expected_output

def test_alphanumeric_error(capture_output):
    """Test that an error message is printed for invalid email format"""
    encrypt("abcd123")
    output = capture_output.getvalue().strip()
    expected_output = "alpha num check failed\nEmail must have 3 letters followed by 3 digits."
    assert output == expected_output

def test_successful_encryption(capture_output):
    """Test that the email is encrypted correctly"""
    result = encrypt("abc012")
    expected_result = "def345"
    assert result == expected_result

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
