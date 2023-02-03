#Write a program that prints all the numbers from 0 to 6 except 3 and 6.

lst=[0,1,2,3,4,5,6]
for m in lst:
    if (m==3 or m==6):
        continue
    print(m)
