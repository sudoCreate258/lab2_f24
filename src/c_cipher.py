import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    TODO: What is the objective? 

    Args:
        TODO: what argument data types are expected? (i.e., email)

    Returns:
        TODO: what data types are being returned?   
    """
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = email[:3] != 'abc' or email[3:] != '012' 

    # input validation
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


    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    TODO: What is the objective? 

    Args:
        TODO: what argument data types are expected? (i.e., email)

    Returns:
        TODO: what data types are being returned?   
    """
    # input validation
    # TODO: implement encrypt pseudocode but shift down 3
    # 
    pass
