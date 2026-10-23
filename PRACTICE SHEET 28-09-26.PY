#REVERSE NUMBER
"""N= int(input("tell your number"))
rev=0
while N!=0:
    rev=rev*10+N%10
    N=N//10

print(rev)"""

#cheak palindrome number
"""N= int(input("tell your number"))
rev=0
tem=N
while N!=0:
    rev= rev*10+N%10
    N= N//10
print(rev)
if rev==tem:
    print("the number s pallindrome")
else :
    ("the number is not pallindrome")"""





"""N = int(input("tell your number"))

while N != 0:

    digit = N % 10

    if digit > 5:
        print(digit)

    N = N // 10"""



"""N = int(input("tell your number"))
pro=1
while N != 0:
    digit=N%10
    pro = pro *digit

    N=N//10
    
print(pro)"""



#cheak wheather a number contain digit 7

"""N= int(input("tell your nuumber"))
while N!=0:
    digit=N%10
    N=N//10
    if digit==7:
        
        print("the number 7 is present")
        break
    
    else:
        print("the number 7 is not present")"""



"""N= int(input("tell your number"))
count=0
while N!=0:
    digit=N%3
    N=N//10

    if digit%3:
        count=count+1
        
        print("the number is divisible by 3", count)
    else:

    
        print("the number is not divisible by 3", )"""
    


"""N = int(input("Tell your number: "))

new_number = 0
place = 1

while N != 0:
    digit = N % 10
    N = N // 10

    if digit == N:
        digit = 7

    new_number = new_number + digit * place
    place = place * 10

print("New number:", new_number)"""





"""N=int(input("tell me your number"))
while N==N:
    N=N//10
    break
print(N)"""
