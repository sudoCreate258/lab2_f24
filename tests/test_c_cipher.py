import pytest
import logging
from src.c_cipher import encrypt

# Configure logging to capture test results
logging.basicConfig(level=logging.INFO, format='%(message)s')

def test_kick_the_back_tires():
    assert encrypt() == 'dbc012'

def test_length_error(caplog):
    """Test that a length error message is logged for invalid email size"""
    with caplog.at_level(logging.INFO):
        result = encrypt("abcd1234")
    if "Length check failed" in caplog.text:
        logging.info("Test Passed: Length error correctly logged")
    else:
        logging.error("Test Failed: Length error not logged")
    assert "Length check failed" in caplog.text
    assert "Email must be 6 characters long." in caplog.text
    assert result == "Length check failed\nEmail must be 6 characters long."

def test_alphanumeric_error(caplog):
    """Test that an alphanumeric error message is logged for invalid email format"""
    with caplog.at_level(logging.INFO):
        result = encrypt("abcd123")
    if "alpha num check failed" in caplog.text:
        logging.info("Test Passed: Alphanumeric error correctly logged")
    else:
        logging.error("Test Failed: Alphanumeric error not logged")
    assert "alpha num check failed" in caplog.text
    assert "Email must have 3 letters followed by 3 digits." in caplog.text
    assert result == "alpha num check failed\nEmail must have 3 letters followed by 3 digits."

def test_successful_encryption(caplog):
    """Test that the email is encrypted correctly"""
    result = encrypt("abc012")
    if result == "def345":
        logging.info("Test Passed: Encryption successful")
    else:
        logging.error("Test Failed: Encryption unsuccessful")
    assert result == "def345"

'''
def test_decrypt_successful(caplog):
    """Test that the email is decrypted correctly"""
    # Assuming 'def345' is the encrypted form of 'abc012'
    result = decrypt("def345")
    if result == "abc012":
        logging.info("Test Passed: Decryption successful")
    else:
        logging.error("Test Failed: Decryption unsuccessful")
    assert result == "abc012"

def test_decrypt_invalid_format(caplog):
    """Test that decryption handles invalid formats"""
    result = decrypt("invalid")
    # Expected result should be some indication of failure, change as needed
    expected_output = "Decryption failed or invalid format"
    if result == expected_output:
        logging.info("Test Passed: Invalid format correctly handled")
    else:
        logging.error("Test Failed: Invalid format not handled correctly")
    assert result == expected_output
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
