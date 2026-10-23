"""N= int(input("tell your number"))
count= 0
for i  in range(1 , N+1):
    if i%3==0:
        count= count+1
print(count)"""

"""find the largest among N number take N numbers as input  and determine the largest 
number among then"""


"""Num = int(input("kitne numbers daloge: "))
max_num = 0
for i in range(Num):
    N = int(input("enter number: "))
    if N > max_num:
        max_num = N
print("Maximum number is:", max_num)"""


Num = int(input("tell your num  number"))
max=0
for i in range(1, Num+1):
    N= int(input("tell your number"))
    if N>i:
        max=N
        
print(max) 















       
# Take N numbers as input and find the largest

"""N = int(input("Kitne numbers dalna hai: "))   
numbers = []   

for i in range(N):
    num = int(input(f"Number {i+1} dalo: "))
    numbers.append(num)

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest number hai:", largest)"""

"""NUM= int(input("tell your num number")) 
count= 0
total= 0
for i in range(1 , NUM+1) :
    N= int(input("tell your number"))
    if N>0 :
        total = total+N
        count= count+1
if count>0:
    avg= total/count
    print("the avg is , " , avg)
else :
    print("the avg is not corrected")"""

NUM = int(input("tell your num number")) 
count = 0
total = 0

for i in range(1 , NUM+1):
    N = int(input("tell your number"))
    if N > 0:
        total += N
        count += 1

if count > 0:   # ✔️ yaha condition lagao
    avg = total / count
    print("The average is:", avg)
else:
    print("No positive numbers entered, average not possible")






#find highest common factors

"""N= int(input("tell your first number"))
B= int(input("tell your second number"))
if N>B :
    for i in range (B,0,-1):
        if B%i==0 and N%i==0 :
            print(f"hcf-{i}")
            break
elif B>N :
    for i in range(N , 1 , -1):
        if B%i==0 and N%i==0 :
            print(f"hcf-{i}")
            break
else :
    print("HCf-{N}")"""
#

#seperate the digit of _5279

A= 5379
