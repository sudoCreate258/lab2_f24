import pytest
from src.c_cipher import encrypt, decrypt
from src.exceptions import SizeConstraintError, AlphaNumericError

def test_kick_the_tires():
  assert encrypt() == "dbc012"

#def test_encrypt_valid_email():
#    assert encrypt("abc123") == "def456"

#def test_decrypt_valid_email():
#    assert decrypt("def456") == "abc123"

#def test_encrypt_invalid_size():
#    with pytest.raises(SizeConstraintError):
#        encrypt("abcd123")

#def test_encrypt_invalid_format():
#    with pytest.raises(AlphaNumericError):
#        encrypt("abc12@")

#def test_decrypt_invalid_size():
#    with pytest.raises(SizeConstraintError):
#        decrypt("def4567")
