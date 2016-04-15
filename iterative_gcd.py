def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    GCD=min(a,b)
    result=1
    while(GCD>1):
        if (a%GCD==0 and b%GCD==0):
            result=GCD
            break
        GCD-=1
    return result