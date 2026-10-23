# 18-09-2026

#question  01
#N= int(input(" tell your number"))
#for i in range(1 , N+1) :
 #   print(i)

#question 02
"""N= int(input("tell your number"))
for i in range(0,N+1 , 2):
    print(i)"""
        

#questin 03
"""N= int(input("tell your number"))
for i in range(1 , N+1 , 2):
    print(i)"""

#question 04
"""N= int(input("tell your number"))
sum = 0
for i in range(1,N+1):
    sum=sum+i
print(sum)"""

#question 05
"""N= int(input("tell your number"))
for i in range(1 ,11):
    multi= N*i
    print(multi)"""

#question06
#text = input("Enter a string: ")

"""for i in range(len(text)):
    print(f"Character at index {i}: {text[i]}")"""


#question 07
"""N= int(input("tell your number"))
for i in range(N, N*10+1 , N):
    print(i)"""






#221-09-20026

"""N= int(input("enter the number"))
for i in range(1 , N+1):
    print(f"{i**2}")"""


"""N= int(input("enter your number"))
for i in range(0, N+1 , 5):
    print(i)"""

"""N= int(input("tell your number"))
count=0
for i in range(1 ,N+1):
    if i%2==0:
        count=count+1 # iss line ka mtlb ky hua yeh bta de bs mujhe
print(count)"""



"""N= int(input("enter your number"))
sum=0
for  i in range(1,N+1):
    if i%2==0:
        sum= sum+i
print(sum)"""

"""N= int(input("tell your number"))
count=0
for i in range(1 ,N+1):
    if i%2==0:
        count=count+i # iss line ka mtlb ky hua yeh bta de bs mujhe
        print(count)"""


"""N= int(input("tell your range of input"))
pos=0
neg=0
for i in range(1,N+1):
    A= int(input("tell your number"))
    if A>0:
        pos= pos+1
    else:
        neg=neg+1
print(pos)
print(neg)"""



"""text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for i in text:
    if i in vowels:
        count += 1

print("Total vowels:", count)"""



"""text=input("teke a string")
char= input("take a char")
count=0
for i in text:
    if i==char:
        count=count+1
print("total number of character is " , count)"""


#22-09-2026


"""N= int(input("tell how many days classes are going"))
pas=0
fail=0
for i in range(1,N+1):

    A=input("tell present or absent")
    if A=="p":
        pas=pas+1
    elif A=="f":
        fail=fail+1
print(pas)
print(fail)"""


#question 2

"""N=int(input("tell the product are inspecting"))
pas=0
fail=0
for i in range(1 , N+1):
    A= int(input("tell your  product"))
    if A==1:
        pas=pas+1
    elif A==0:
        fail=fail+1
print(pas)
print(fail)"""



#question=3
"""N= int(input("enter how many days person saved money : "))
sav=0
not_save=0
for i in range(1,N+1):
    A= int(input("tell your amount save"))
    if A>=500:
        sav=sav+1
    elif A<500:
        not_save=not_save+1
print(not_save)
    
print(sav)"""

#question 4

"""N= int(input("tell how many days u consumes electricity"))
units=0
less_consumption=0

for i in range(1,N+1):
    A= int(input("tell how much units you consumes"))
    if A>10:
        units=units+1
    elif A<10:
        less_consumption=less_consumption+1

print(units)
print(less_consumption)
print(f"total units are {units+less_consumption}")"""

#23-09-2026

#question no 1
"""N= int(input("tell your number"))
count=0
for i in range(1,N+1):
    if i%3==0:
        count=count+1
print(count)"""


#question no 2
"""N= int(input("how much number take as input"))
max=0
for i in range(1, N+1):
    A= int(input("tell your number"))
    if A>i:
        max=N
print(max)"""


#question no 03

"""N = int(input("tell your input"))
count = 0
sum = 0

for i in range(1, N+1):
    A = int(input("tell your number"))
    if A > 0:
        sum = sum + A   # number add karo
        count = count + 1   # positive number count karo

if count > 0:
    avg = sum / count
    print("Average is:", avg)
else:
    print("No positive numbers entered")"""



#question no 5   

"""N= int(input("tell your number"))
count=0
for i in range(1, N+1):
    if N%i==0:
        count=count+i
        print(count)"""





"""N=int(input("tell your number"))
count=0
for i in range(1,N+1):
    if i%10==0:
        count=count+i
print(count)"""



       

"""N= int(input("tell your number"))
for i in range(1, N+1):
    if i%7==0:
        print(i)
        break"""



"""N= int(input("tell your number"))
for i in range(1 , N+1):
    if i%7==0:
        continue
    print(i)"""









"""N= int(input("tell your number"))
for i in range(1, N+1):
    if i%7==0:
        print(i)
        break"""




"""correctpass=123456
for i in range(1, 4):
    N=int(input('tell your number'))
    if N==correctpass:
        print("lofgin suuccessful")
        break
    else:
        left=3-i
    if left>0:
        print("you have attempt left" , left)
    else:
        print("account blocked")"""


"""N= int(input("tell your number"))
while N!=0:
    print(N%10)
    if N==7:
        print("number 7 is found")
        break
    else:
        
        
        
        
        print("the number 7 is not found")

    N=N//10"""



"""N= int(input("tell your number"))
sum=0
for i in range(1 ,N+1):
    if i%3==0:
        sum=sum+i
        print(sum)
        continue
        
    elif sum>100:
        print("loop is out of 100")
        break"""

N= int(input("tell your number"))
while N!=0:


    z=N%10
    print(z)
    if N==0: 
        continue
    elif N%2==0:
        print(N)
    elif N%2!=0:
        continue
    elif N==7:
        print("7 is founded")
        break
    N=N//10
          











    
