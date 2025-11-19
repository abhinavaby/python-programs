#addition of two numbers using recursion
def add(a,b):
    if b==0:
        return a
    else:
        return add(a+1,b-1)
print(add(1,5))

