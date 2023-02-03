def foo():
    try:
      return 1
    finally:
      return 2
k = foo()
print(k)

#result 2

def a():
    try:
       f(x, 4)
    finally:
     print('after f')
print('after f?')
a()
  
# result - f is not defined here
  