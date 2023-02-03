#12 Write a function to compute 5/0 and use try/except to catch the exceptions
def Zerodiv(y):
    try:
      x = y/0 
      print(x)
    
    except ZeroDivisionError:   
     print("can't divide by zero")
     
Zerodiv(5)
