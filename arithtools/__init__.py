def fibonacci_series(range, num1=0, num2=1) -> int:
    """
        Takes <range> from user and default parameter value is 0 and 1 and prints the fibonacci series in order.
    """
    range -= 2
    a, b = num1, num2
    print(a)
    print(b)
    while(range != 0):
        c = a+b
        a = b
        b = c
        print(c)
        range -= 1
    return None


def reverse(number) -> int:
    """
       Takes a integer number as input and returns the reverse of it.
    """
    rev = 0
    while number > 0:
        d = number % 10
        rev = rev*10+d
        number //= 10
    return rev


def numtoword(number) -> str:
    """
        Takes a number as input and converts the given number into words and returns it.
    """
    Num_Words = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    l = []
    while(number > 0):
        d = number % 10
        l.append(Num_Words[d])
        number //= 10
    l = l[::-1]
    return ' '.join([i for i in l])


def automorphic(number) -> bool:
    """
        Takes a Number as input and check whether the number is automorphic or not and return True or false accordingly.
    """
    square = str(number**2)
    return True if str(number) in square else False


print(automorphic(25))
