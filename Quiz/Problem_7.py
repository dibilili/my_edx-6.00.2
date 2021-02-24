# Problem 7
#  Bookmark this page

#Write a function that meets the specification below:


def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    n = 0
    while True:
        if test(n) == True:
            return n
        elif test(-n) == True:
            return -n
        n += 1

