import random

N = random.randrange(2,11)

print("N = ", N)
a = [random.randrange(1,11) for i in range(N)]
print("Initial:",a)
print("Even Indices:",a[::2])
print("Minimum:",min(a[::2]))