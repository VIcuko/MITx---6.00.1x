def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    top=len(aStr)
    pointer=top/2
    if (aStr==""):
        return False 
    elif aStr[pointer]==char:
        return True
    else:
        if (char < aStr[pointer]):
            return (False or isIn(char,aStr[:pointer]))
        else:
            return (False or isIn(char,aStr[pointer+1:]))
    
