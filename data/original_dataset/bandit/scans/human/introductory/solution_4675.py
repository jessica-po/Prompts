# Enter your code here. Read input from STDIN. Print output to 


import math

class ComplexNumber(object): 
    def __init__(self, real, compl): 
        self.real = real 
        self.compl = compl
        pass
    def __str__(self):
        if (self.compl >= 0):
            return '{0:.2f}'.format(self.real) +'+'+ '{0:.2f}'.format(self.compl) +'i' 
        return '{0:.2f}'.format(self.real) +'-'+ '{0:.2f}'.format(abs(self.compl)) +'i' 
    def __add__(x, y):
        return ComplexNumber(x.real+y.real, x.compl+y.compl)
    def __sub__(x, y):
        return ComplexNumber(x.real-y.real, x.compl-y.compl)
    def __mul__(x, y):
        return ComplexNumber(x.real*y.real - x.compl*y.compl, x.compl*y.real + x.real*y.compl)
    def __truediv__(x, y):
        return ComplexNumber((x.real*y.real + x.compl*y.compl) / (y.real*y.real + y.compl*y.compl), 
                             (x.compl*y.real - x.real*y.compl) / (y.real*y.real + y.compl*y.compl))
    def mod(self):
        return ComplexNumber(math.sqrt(self.real*self.real + self.compl*self.compl), 0)
    
help = list(map(float, input().split(' ')))   
x = ComplexNumber(help[0], help[1])    
help = list(map(float, input().split(' ')))   
y = ComplexNumber(help[0], help[1])    

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x.mod())
print(y.mod())