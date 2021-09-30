#Calculator.py

def sum (m,n):

        if(n>=0):
            for i in range(0,n):
                m = m + 1
        else:
            for i in range(0,abs(n)):
                m = m -1
        return m
    
# divide m, n 
# must substract n from m until gets 0 
def divide(m,n):
    if(n==0):
        raise Exception("No zero division")
    count = 0
    sign = 1
    if(not(m<0 ^ n<0)):
        sign = -1

    m = abs(m)
    n = abs(n)
    while(m>=n):
        m = m - n
        count = count + 1
    return count*sign
