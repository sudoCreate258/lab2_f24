import unittest
from src.c_cipher import encrypt
from src.exceptions import SizeConstraintError, AlphaNumericError

class TestEncryptFunction(unittest.TestCase):

    def test_size_constraint_error(self):
        """Test that SizeConstraintError is raised for invalid email size."""
        with self.assertRaises(SizeConstraintError) as context:
            encrypt("abcd1234")  # Length is 8, should raise SizeConstraintError
        self.assertEqual(str(context.exception), "Email must be 6 characters long.")

    def test_alphanumeric_error(self):
        """Test that AlphaNumericError is raised for invalid email format."""
        with self.assertRaises(AlphaNumericError) as context:
            encrypt("abcd123")  # Length is 7, should raise AlphaNumericError
        self.assertEqual(str(context.exception), "Email must have 3 letters followed by 3 digits.")


'''import pytest
from src.c_cipher import encrypt


def test_kick_the_back_tires():
    assert encrypt() == 'dbc012'

def test_size_constraint_error(capsys):
    """Test that SizeConstraintError is raised for invalid email size."""
    with pytest.raises(SizeConstraintError, match="Email must be 6 characters long."):
        encrypt("abcd1234")  

def test_alphanumeric_error(capsys):
    """Test that AlphaNumericError is raised for invalid email format."""
    with pytest.raises(AlphaNumericError):
        encrypt("abcde1")   '''


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
