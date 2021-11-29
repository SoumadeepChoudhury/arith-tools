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


def peterson(number) -> bool:
    """
        Takes a number as input and check whether a given number is Peterson or not.
    """
    n, sum = number, 0
    while number > 0:
        d = number % 10
        f = d
        for i in range(1, d):
            f *= i
        sum += f
        number //= 10
    if(sum == n):
        return True
    else:
        return False


def sunny(number) -> bool:
    """
        Takes a number as input and checks whether the given number is Sunny Number or not.
    """
    number += 1
    return True if(number**(1/2) == int(number**(1/2))) else False


def tech(number) -> bool:
    """
        Takes a number as input and checks whether the given number is Tech Number or not.
    """
    if(len(str(number)) % 2 != 0):
        return False
    else:
        return True if(((number % 100)+(number//100))**2 == number) else False


def fascinating(number) -> bool:
    """
        Takes a number as input and checks whether the given number is Fascinating Number or not.
    """
    number = str(number) + str(number*2) + str(number*3)
    f = 0
    for i in range(1, 10):
        if(str(i) not in number or number.count(str(i)) > 1):
            f = 1
            break
    return True if(f == 0) else False


print(fascinating(2018))
