def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>= 0:
        return x
    else:
        return -x
import math    
def move(x,y,step, angle=0):
	nx = x+step*math.cos(angle)
	ny = y-step*math.sin(angle)
	return nx,ny

def x2func(a,b,c):
	x1 = (-b+math.sqrt(b*b-4*a*c))/2/a
	x2 = (-b-math.sqrt(b*b-4*a*c))/2/a
	return x1,x2
	
def fact(n):
		return fact_iter(n,1)

def fact_iter(num, product):
	if num ==1:
		return product
	return fact_iter(num-1, num*product)

def make_arry(n):
	L=[]
	while n<=99:
		L.append(n)
		n = n+2
	return L
		