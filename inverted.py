n = int(input())
k = n * 2 - 1 
p = 0 
for i in range(n):
    print(" " * p +"*" * k)
    k = k - 2 
    p = p + 1