from src.exceptions import SizeConstraintError, AlphaNumericError

def encrypt(email="abc012"):
    """
    TODO: What is the objective? 

    Args:
        TODO: what argument data types are expected? (i.e., email)

    Returns:
        TODO: what data types are being returned?   

    Raises:
        SizeConstraintError: If the email is not exactly 6 characters long.
        AlphaNumericError: If the email does not consist of 3 letters followed by 3 digits.
    """
    try:
        len_flag = len(email) != 6
        anum_flag = email[:3] != 'abc' and email[3:] != '012' 
        # TODO: fix line above, what built in functions can we implement?
        
        if len_flag:
            raise SizeConstraintError("Email must be 6 characters long.")
        if anum_flag:
            raise AlphaNumericError("Email must have 3 letters followed by 3 digits.")

        # TODO: fix line below, process our string into a list
        email_lst = ["a", "b", "c", "0", "1", "2"]
        
        # TODO: fix line(s) below, update EACH element's ASCII value + 3
        new_ascii = ord(email_lst[0]) + 3
        email_lst[0] = chr(new_ascii)
        
        # TODO: fix line below, convert list into a string
        email_str = "dbc012"
        retVal = email_str

        return retVal 

    except SizeConstraintError as e: 
        output = "Error"
        # TODO: fix line above, use string formatting for a specific error message
        print(output)
    except AlphaNumericError as e:
        output = "Error"
        # TODO: fix line above, use string formatting for a specific error message
        print(output)

def decrypt(email="def345"):
    pass
