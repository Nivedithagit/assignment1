#1. Create a list of given structure and get the Access list as provided below:
#x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
#Access list: [1, 2, 3, 4]Access list: [600, 700]
#Access list: [100, 300, 500, 600, 800]
#Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
#Access list: [10]
#Access list: [ ]
x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x)
print(x[5][:4])
print(x[-3:-1])
print(x[::2])
print(x[::-1])
print(x[5][5][:1])
print(x[:0])
