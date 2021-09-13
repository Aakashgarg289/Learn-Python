# ITERATIVE APPROACH OR METHOD
def factor(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
v = factor(5)
print(v)

# RECURSION METHOD
def facto(n):
    if n==1:
        return 1
    return n * facto(n-1)
v = facto(5)
print(v)