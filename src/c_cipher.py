import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# TODO: implement encrypt pseudocode and shift up 3
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
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below, implement functionality rather than literals
    anum_flag = email[:3] != 'abc' or email[3:] != '012' 

    # simple input validation
    if len_flag:
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output          
    # TODO: fix line below, process our string into a list
    email_lst = ["a", "b", "c", "0", "1", "2"]
        
    # TODO: fix line(s) below, update EACH element's ASCII value + 3
    new_ascii = ord(email_lst[0]) + 3
    email_lst[0] = chr(new_ascii)
        
    # TODO: fix line below, convert list into a string
    email_str = "dbc012"

    
    retVal = email_str
    return retVal 

# TODO: implement encrypt pseudocode but shift down 3
def decrypt(email="def345"):
    pass
