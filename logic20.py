def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    tim_1=0
    tim_0=0

    x1=n%10
    n//=10
    print(n)
    tim_1+=x1==1
    tim_0+=x1==0 and n>=1

    x2=n%10
    n//=10
    print(n)
    tim_0+=x2==0 and n>=1
    tim_1+=x2==1

    x3=n%10
    n//=10
    print(n)
    tim_1+=x3==1
    tim_0+=x3==0 and n>=1
    
    x4=n%10
    n//=10
    print(n)
    tim_1+=x4==1
    tim_0+=x4==0 and n>=1

    x5=n%10
    n//=10
    print(n)
    tim_1+=x5==1
    tim_0+=x5==0 and n>=1
    
    return tim_1>tim_0
print(main(110))
print(main(11001))

