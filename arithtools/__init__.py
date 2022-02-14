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
        
def auto_biographical(n):
    """DESCRIPTION:::::::::An autobiographical number is a number N such that the first digit of N counts how many zeroes are in N,
    the second digit counts how many ones are in N and so on. In our example, 1210 has 1 zero, 2 ones, 1 two and 0 threes."""
    sum=0
    ct=0
    while(n!=0):
        r=n%10
        ct+=1
        sum+=r
        n=n//10
    if(sum==ct):
        print("Auto-Biographical number") 
    else:
        print("Not an Auto-Biographical number") 
n=int(input("Enter the number"))
auto_biographical(n)
