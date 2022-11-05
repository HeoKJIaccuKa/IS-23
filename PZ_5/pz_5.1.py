import random

n = random.randint(1000, 9999)
print(n)

n1 = int(n/1000)
n2 = int((n%1000)/100)
n3 = int((n%100)/10)
n4 = int(n%10)

print (n1,n2,n3,n4)

if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
    print ("DA")

else:
    print ("NET")


