#9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
#Sample input: 12abcbacbaba344ab
#Expected output: a=5 b=5 c=2
#: Make sure to avoid counting the occurrence of numeric values in the string.
import re
string_data=input("enter a string")
string_data1=re.sub("[^a-zA-Z]+", "", string_data)
list1=[]
for ch in string_data1:
    if ch not in list1:
        list1.append(ch)
        print(ch,"=",string_data1.count(ch))
