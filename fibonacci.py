# ITERATIVE METHOD
def fib(n):
    a = 0
    b = 1
    for i in range(2, n):
        a, b = b, a+b
    print(b)

fib(5)

# RECUSIVE METHOD
# FIBONACCI SERIES = 0,1,1,2,3,5,8,13,21,34.......
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-1) + fibo(n-2)
v = fibo(5)
print(v)