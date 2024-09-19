import pytest
from src.c_cipher import encrypt, decrypt
from src.exceptions import SizeConstraintError, AlphaNumericError

def test_kick_the_front_tires():
  assert encrypt() == "dbc012"

def test_kick_the_back_tires():
    with pytest.raises(SizeConstraintError):
        encrypt("abcd123")  # This should raise SizeConstraintError

def test_size_constraint_error():
    with pytest.raises(SizeConstraintError):
        encrypt("abc1234")  # This should also raise SizeConstraintError

def test_alphanumeric_error():
    with pytest.raises(AlphaNumericError):
        encrypt("abcd123")  # This should raise AlphaNumericError if the email is invalid

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
