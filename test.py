import random


arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
arrLen = len(arr)

for i in range(50):
    x = random.randint(0,arrLen-1)
    print(x,arr[x])
