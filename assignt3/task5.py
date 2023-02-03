#5. Create a new list which contains the specified numbers after removing the even numbers from a
#predefined list.

lst=[1,2,3,4,5,6,7,8,9,10]
for x in lst:
     if(x%2==0):
         lst.remove(x)
print(lst)
