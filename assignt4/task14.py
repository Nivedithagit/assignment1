#14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
#Make sure to use only higher order functions.
num = int(input("enter max num : "))
integers= range(1,num+1)
final_list = list(filter(lambda x:x %7 ==0 and x%3 !=0 , integers))
print(final_list)
