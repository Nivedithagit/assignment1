
a=10
b=20
c=30
avg=float((a+b+c)/3)
print("avg=",avg)
if avg>a and avg>b and avg>c:
    print("avg is higher than a,b,c")
    if avg>a and avg>b:
        print("avg is higher than a,b,c")
    elif avg>a and avg>c:
        print("avg is higher than a,c")
    elif avg>b and avg>c:
        print("avg is higher than b,c")
    elif avg>a:
        print("avg is just higher than a")
    else:
        pass
elif avg>b:
    print("avg is higher than b")
elif avg>c:
    print("avg is just higher than c")
else:
    pass
