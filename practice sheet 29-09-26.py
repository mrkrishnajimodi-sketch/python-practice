N = int(input("tell your number"))
total = 0
temp=N
while N != 0:
    z = N % 10
    fact = 1
    for i in range(1, z + 1):
        fact = fact * i
    total = total + fact
    N = N // 10
print(total)
if total==temp:
    print("the number is strong")
else:
    print("the number is not stronhg")"""


N= int(input("tell me your number"))
sum=0
square_count=0

while N!=0:

    z=N%10
    sum= sum+z
    N=N//10
print(sum)
    

    

"""for i in range(1,z+1):
        squ=z*sum
        print(squ)
        N=N//10
square_count=square_count+squ
print(square_count)
