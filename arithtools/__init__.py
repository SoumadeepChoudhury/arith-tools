
import math


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


def keith(number) -> bool:
    """
        Takes a number as input and checks whether the given number is Keith or repfigit Number or not.
    """
    n = number
    terms = []
    while number > 0:
        terms.append(number % 10)
        number //= 10
    terms = terms[::-1]
    length = len(terms)
    while True:
        sum = 0
        for i in range(1, length+1):
            sum += terms[len(terms)-i]
        terms.append(sum)
        if(terms[-1] == n):
            return True
        elif(terms[-1] > n):
            return False
        else:
            continue


def repfigit(number) -> bool:
    """
        Takes a number as input and checks whether the given number is Keith or repfigit Number or not.
    """
    keith(number)


def neon(number) -> bool:
    """
        Takes a number as input and checks whether the given number is Neon Number or not.
    """
    square, sum = number**2, 0
    while square > 0:
        d = square % 10
        sum += d
        square //= 10
    return True if(sum == number) else False


def spy(number) -> bool:
    """
        Takes a number as input and checks whether the given number is Spy Number or not.
    """
    sum, prod = 0, 1
    while number > 0:
        d = number % 10
        sum += d
        prod *= d
        number //= 10
    return True if(sum == prod) else False


def atm():
    """In the ATM program, the user has to select an option from the options displayed on the screen. The options are related to withdraw the money, deposit the money, check the balance, and exit."""
    balance = 10000
    print("..........WELCOME TO OUR ATM.........\n1. Withdraw Money \n2. Deposit Money\n3. Check Balance\n4. Exit\n")
    while True:
        userChoice = int(input("Enter Your Choice: "))
        if(userChoice == 1):
            amt = float(input("Enter the Amount you wanna withdraw...."))
            balance -= amt
            print("Successfully Withdrawn...Take the Cash...")
        elif(userChoice == 2):
            amt = float(input("Enter the Amount you wanna Deposit...."))
            balance += amt
            print("Successfully Deposited.....")
        elif(userChoice == 3):
            print(f"Your current account balance is {balance}")
        else:
            break
    return "Thanks For Visiting...."


def emirp(number) -> bool:
    """Takes a number as input and checks if the given number is emirp or not."""
    c = 1
    for i in range(1, number):
        if(number % i == 0):
            c += 1
    if(c <= 2):
        n = 0
        while number > 0:
            d = number % 10
            n = n*10+d
            number //= 10
        c = 1
        for i in range(1, n):
            if(n % i == 0):
                c += 1
        return True if(c <= 2) else False
    else:
        return False


def boiled_egg(number) -> str:
    """Takes number of terms as input from user and display/print the following Boiled Egg Series:\n
    SUNDAY, MONDAY, WEDNESDAY, SATURDAY ...……. n terms..."""
    li = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY",
          "THURSDAY", "FRIDAY", "SATURDAY"]
    user_Inp = number
    t = 0
    d = 0
    z = 1
    for i in range(user_Inp):
        if(t == 21):
            t, z, d = 0, 1, 0
        t = t+d
        d = d+1
        if(t <= 6):
            print(li[t])
        else:
            print(li[t - 7*z])
            z += 1


def auto_biographical(number) -> bool:
    """Check whether the entered number is auto_biographical number or not."""
    number = str(number)
    if len(number) > 9:
        return False
    for i in range(len(number)):
        if(number.count(str(i)) != int(number[i])):
            return False
    return True


def pascal_triangle(number):
    """User will enter the row and it will print the pascal's triangle along with space."""
    for i in range(0, number):
        for k in range(number, i, -1):
            print(end=' ')
        num = 1
        for j in range(0, i+1):
            print(num, end=' ')
            num = num*(i-j)//(j+1)
        print()


def two_digit_special(number) -> bool:
    """It will check whether the entered number is a two digit special number or not."""
    s = 0
    n = number
    p = 1
    a = n
    if(n > 9 and n < 100):
        while(n != 0):
            r = n % 10
            p = p*r
            s = s+r
            n = n//10
        if(s+p == a):
            return True
        else:
            return False
    else:
        return False


def krishnamurti(number) -> bool:
    """It will check whether the entered number is a krishnamurti number or not."""
    s = 0
    n = number
    a = n
    while(n != 0):
        f = 1
        r = n % 10
        for i in range(1, r+1):
            f = f*i
        s = s+f
        n = n//10
    if(s == a):
        return True
    else:
        return False


def pronic(number) -> bool:
    """It will check whether the entered number is a pronic number."""
    flag = 0
    n = number
    for i in range(0, n):
        if(i*(i+1) == n):
            flag = 1
            break
    if(flag == 1):
        return True
    else:
        return False


def darsium(number) -> bool:
    """It will check whether the entered number is a darsium number or not."""
    s = 0
    n = number
    c = 0
    p = n
    x = n
    while(p != 0):
        p = p//10
        c += 1
    while(n != 0):
        r = n % 10
        s = s+(r**c)
        c = c-1
        n = n//10
    if(s == x):
        return True
    else:
        return False


def happy(number) -> bool:
    """It will check whther the entered number is a happy one or not"""
    p = 0
    n = number
    if(n > 0 and n < 10):
        return False
    else:
        while True:
            s = 0
            while(n != 0):
                r = n % 10
                s = s+(r*r)
                n = n//10
            if(s < 10):
                p = s
                break
            else:
                n = s
        if(p == 1):
            return True
        else:
            return False


def unique(n) -> bool:
    """Checks whether the given number is Unique or not..."""
    if(n == 0):
        return False
    f = 0
    for i in range(0, 10):
        cp = n
        ct = 0
        while(cp != 0):
            r = cp % 10
            if(r == i):
                ct += 1
            cp = cp//10
        if(ct > 1):
            f = 1
            return False
    if(f == 0):
        return True


def strong(n) -> bool:
    """Checks whether the given number is Strong Number or not."""
    sum = 0
    temp = n
    while(n):
        i = 1
        f = 1
        r = n % 10
        while(i <= r):
            f = f*i
            i = i+1
        sum = sum+f
        n = n//10
    if(sum == temp):
        return True
    else:
        return False


def amicable(userInput1, userInput2) -> bool:
    """Checks whether the given pair of numbers is amicable or not..."""
    s1 = 0
    s2 = 0
    for i in range(1, userInput1):
        if(userInput1 % i == 0):
            s1 += i
    for j in range(1, userInput2):
        if(userInput2 % j == 0):
            s2 += j
    if(s1 == userInput2 and s2 == userInput1):
        return True
    else:
        return False


def Nearest_Prime(n, dist=1) -> int:
    """Returns the nearest prime of a given input.For certain cases two values could be at near,to find the nearest prime from 0 to that number give ```dist=1``` otherwise ```dist=2```.."""
    a = n
    m = n
    while(1):
        ct = 0
        a = a+1
        for i in range(1, a+1):
            if(a % i == 0):
                ct += 1
        if(ct == 2):
            break
    while(1):
        ct = 0
        m = m-1
        for j in range(1, m+1):
            if(m % j == 0):
                ct += 1
        if(ct == 2):
            break
    if((a-n) < (n-m)):
        return a
    elif((n-m) < (a-n)):
        return m
    else:
        if dist == 1:
            return m
        elif dist == 2:
            return a


def equilateral_triangle(n):
    """Print a equilateral triangle with * for ```(n+1)//2``` number of rows"""
    for i in range(1, n+1, 2):
        print(" "*n, "*"*i, " "*n)
        n = n-1


def terrace(userNum1, userNum2) -> bool:
    """Check whether the input number is Terrace or not..."""
    temp1, temp2 = userNum1, userNum2
    gcd = math.gcd(temp1, temp2)
    li = [2, 3, 5, 7, 11, 13, 17, 19]
    i = 0
    while True:
        if(userNum1 % li[i] == 0 and userNum2 % li[i] == 0):
            userNum1, userNum2 = userNum1//li[i], userNum2//li[i]
            i = 0
            lis1 = list(str(userNum1))
            lis2 = list(str(userNum2))
            z, k = 0, 0
            if len(lis1) == len(lis2):
                for z in lis1:
                    if(z in lis2):
                        k += 1
                for z in lis2:
                    if(z in lis2):
                        k += 1
                if(k == len(lis1)*2):
                    if(temp1//gcd == temp2//gcd - 1 or temp1//gcd == temp2//gcd+1):
                        return True
                    else:
                        return False
        elif(userNum1 < 1 or userNum2 < 1 or i == len(li)-1):
            return False
        else:
            i += 1
