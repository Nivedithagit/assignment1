#Create a new dictionary by concatenating the following two dictionaries:
#Sample input: a={1:10,2:20} b={3:30,4:40}
#Expected output: {1:10,2:20,3:30,4:40}
a={1:10, 2:20}
b={3:30, 4:40}
c={}

for x in (a,b):c.update(x)
print(c)
