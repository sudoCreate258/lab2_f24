import pytest
from src.cipher import encrypt

def test_kick_the_back_tires(capsys):
    encrypt("abcd123")
    captured = capsys.readouterr()
    assert "Email must be 6 characters long." in captured.err

def test_size_constraint_error(capsys):
    encrypt("abc1234")
    captured = capsys.readouterr()
    assert "Email must be 6 characters long." in captured.err

def test_alphanumeric_error(capsys):
    encrypt("abcd123")
    captured = capsys.readouterr()
    assert "Email must have 3 letters followed by 3 digits." in captured.err



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
