'''d={"a":10,"b":25,"c":15,"d":40}
large=0
for i in d:
    if d[i]>large:
        large=d[i]
print(large)'''

'''d={"a":10,"b":25,"c":5,"d":40}
smallest=10

for keys,value in d.items():
    if value<smallest:
        smallest=value

print(smallest)'''



'''d={"a":10,"b":25,"c":15,"d":40}
even=0
odd=0
for i in d:
    if d[i]%2==0:
        even=even+1
    elif d[i]%2!=0:
        odd=odd +1

print(even)
print(odd)'''




'''
d={"a":10,"b":25,"c":15,"d":40}
count=0
for i in d: 
         count=count+d[i]

print(count)'''




'''d={"a":10,"b":25,"c":15,"d":40}
for i in d:
    d[i]=d[i]+5

print(d)'''

"""d={"a":10,"b":25,"c":15,"d":40}
number=20
count=0
for i in d:
    if d[i]>number:
        count+=1

print(count)"""


'''keys=["a","b","c"]
value=[10,20,30]
resuly={}
for i in range(len(keys)):
    resuly[keys[i]]=value[i]

print(resuly)
'''
"""d={"a":10,"b":25,"c":15,"d":40}
number=10
count=0
for i in d:
    if d[i]==number:
        count+=1

print(count)"""

"""d={"a":10,"b":25,"c":15,"d":40}
positive=0
negative=0
for i in d:
    if d[i]>0:
        positive+=1
    elif d[i]<0:
        negative+=1


print(positive)
print(negative)
