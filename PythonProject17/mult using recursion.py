def mul(a,b):
    global c
    if b==1:
        return a
    else:
        return mul(a+c,b-1)
a=int(input("first number:"))
b=int(input("second number:"))
c=a
y=mul(a,b)
print(y)