import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def encrypt(email="abc012"):
    try:
        len_flag = len(email) != 6
        anum_flag = not (email[:3].isalpha() and email[3:].isdigit())
        
        if len_flag:
            logging.error("Email must be 6 characters long.")
            return  # Stop execution if the size is incorrect
        
        if anum_flag:
            logging.error("Email must have 3 letters followed by 3 digits.")
            return  # Stop execution if the format is incorrect

        # Process email if valid
        email_lst = list(email)
        email_lst = [chr(ord(c) + 3) for c in email_lst]
        email_str = ''.join(email_lst)

        return email_str

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise  # Re-raise the unexpected exception

    """
    TODO: What is the objective? 

    Args:
        TODO: what argument data types are expected? (i.e., email)

    Returns:
        TODO: what data types are being returned?   

    Raises:
        SizeConstraintError: If the email is not exactly 6 characters long.
        AlphaNumericError: If the email does not consist of 3 letters followed by 3 digits.
    
    try:
        len_flag = len(email) != 6
        #anum_flag = email[:3] != 'abc' and email[3:] != '012' 
        # TODO: fix line above, what built in functions can we implement?
        print(len_flag)
        print(email)
        if len_flag:
            logging.error("Email must be 6 characters long.")
            return None        
             
            if anum_flag:
            
            raise AlphaNumericError("Email must have 3 letters followed by 3 digits.")

        # TODO: fix line below, process our string into a list
        email_lst = ["a", "b", "c", "0", "1", "2"]
        
        # TODO: fix line(s) below, update EACH element's ASCII value + 3
        new_ascii = ord(email_lst[0]) + 3
        email_lst[0]2 = chr(new_ascii)
        
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
'''
