#10. Generate and print another tuple whose values are even numbers in the given tuple
#(1,2,3,4,5,6,7,8,9,10).

tup = (1,2,3,4,5,6,7,8,9,10)
print("Tuple Items = ", tup)

print("\nThe Even Numbers in this evTuple Tuple are:")
for i in range(len(tup)):
    if(tup[i] % 2 == 0):
        print(tup[i])
