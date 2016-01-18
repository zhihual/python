from mylib import my_abs
from mylib import move
from mylib import x2func
from mylib import fact
from mylib import make_arry

import math

print(my_abs(-1))


x, y= move(100,100,60, math.pi/6)
print (x, ':',y)

a= 5
b = -4
c = 0
x = x2func(a,b,c)
print(x)
print (a,b,c)
print(x[0],round((x[0]*x[0]*a+(b*x[0])+c),0))
print(x[1],round((x[1]*x[1]*a+(b*x[1])+c),0))
print(fact(5))
l = make_arry(5)
print(l)
print(l[0:3])


		