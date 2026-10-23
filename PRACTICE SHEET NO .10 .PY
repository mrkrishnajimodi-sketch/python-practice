""""difference btw sum of odd nuumbers and sum of even numbers take an integer
as input .calculate the sum of even number and the sum of odd number fron 1to N,
 then find the difference btw the two sums"""

"""N= int(input("tell your number N : "))
M= int(input("tell your number m : "))
even =0
odd=0
for i in range(1 , N+1) :
    if i%2==0 :
        even = even +1
for i in range(1 , M+1):
    if i%2!=0:
        odd= odd +1

sum=odd-even
print(sum)"""


"""difference btw largest  and smallest calculate the difference the largest and smalllest number"""

Num= int(input("tell yor range"))

for i in range(1 , Num+1):
    N= int(input("telll your number"))
    max=N
    min=N
    if N>max:
        max= N
    elif N<min:
        min= N
sum = max- min
print(sum)
