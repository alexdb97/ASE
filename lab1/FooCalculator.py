import Calculator as c

class FooCalculator:
    def __init__(self):
        pass
    def sum (self,m,n):
        return c.sum(m,n)
    def divide (self,m,n):
        return c.divide(m,n)

f = FooCalculator()
print(f.sum(3,5))
print(f.divide(8,2))

