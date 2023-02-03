str = input("enter a string")
n=l=0
for m in str:
    if m.isdigit():
        n=n+1
    elif m.isalpha():
        l=l+1
    else:
        pass
print("letters", l)
print("digits", n)

