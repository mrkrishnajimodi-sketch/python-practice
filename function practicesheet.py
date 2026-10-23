"""def add(a,b):
   return a+b
print(add(10,20))"""


"""def check_even_odd(a):
    
    if a%2==0:
        print("the number is even")
    else:
        print("njumber is odd")
check_even_odd(20)"""

"""def square(a):


    return a*a

print(square(20))"""


"""def maximum(a,b):
    if a>b:
        print("a is greater than b")
    elif b>a:
        print("b is greater than a")
    else:
        print("both number are equal")

maximum (20 ,10)
maximum(10,20)
maximum(10,10)"""




"""def check_number(a):
    if a>0:
        print("the number is psoitive")
    elif a<0:
        print("the number is negative")
    else:
        print("the number is equal to zero")

check_number(40)
check_number(-40)
check_number(0)"""






"""def largest(a, b, c):

    if a > b and a > c:
        print("a is bigger")

    elif b > a and b > c:
        print("b is greater")

    elif c > a and c > b:
        print("c is greater")

largest(49,95,65)"""




"""def prime(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count=count+1

    if count==2:
        print("the number is prime")
    else :
        print("the number is not prime")

prime(15)  
prime(17) 
prime(13)
prime(11) 
prime(9)    """
"""
def sum_of_digits(n):
    sum = 0

    while n != 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10

    return sum


print(sum_of_digits(12345))"""





"""def sum_of_digits(n):
    rev = 0
    

    while n != 0:
        digit = n % 10
        rev=rev*10+ digit
        n = n // 10

    return rev


print(sum_of_digits(12345))"""

"""def check_palindrome(n):
    original = n
    reverse = 0

    while n != 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"


print(check_palindrome(121))
print(check_palindrome(123))"""



"""def gcd(a,b):
    if a>b: 
        for i in range(a,0,-1):
            if b%i==0 and a%i==0:
                print(f"hcf-{i}")
                break
    if b>a:
     for i in range(a,0,-1):
          if b%i==0 and a%i==0:
               print(f"hcf-{i}")
               break
          else :
              print(f"hcf-{a}")


gcd(12,16)"""








def largest_digit(a ):
    digit= a%10
    a=a//10
