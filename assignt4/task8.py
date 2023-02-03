#8. Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).

def square(a,b): 
    l=[]
    x=()
    for i in range(a,b+1): 
       l.append(i*i) 
    return(l) 
    
print(tuple(square(1,20)))


