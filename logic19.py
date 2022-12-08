def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    x1=x%10
    x2=x//10%10
    x3=x//100
    return x%11==0 and (x3*100+x2*10+x1==x)
print(main(121))
print(main(123))