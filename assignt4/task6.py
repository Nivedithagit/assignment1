#Define a function that can receive two integral numbers in string form and compute their sum and
#print it in the console.

def recieveNum (a,b):
	add = int(a) + int(b)
	return add 

num1 = "20"
num2 = "20"
sum = recieveNum (num1, num2)

print("sum is:\n"+str(sum))
