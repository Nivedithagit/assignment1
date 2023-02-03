def twosum(x,sum):
    x.sort()
    left=0
    right=len(x)-1
    while(left<=right):
        if(x[left]+x[right]>sum):
            right=right-1
        elif(x[left]+x[right]<sum):
            left=left+1
        elif(x[left]+x[right]==sum):
            print("value pair",x[left],"&",x[right])
            right=right-1
            left=left+1
            
x=[1,2,3,4,5,6,7,8,9,-1]
sum=8
twosum(x,sum)
        
        
