import math
print("введите коэфициенты a,b и c")
a=float(input())
b=float(input())
c=float(input())

d=b**2-4*a*c
if d>=0:
	x1 = (-b-math.sqrt(d))/(2*a)
	x2 = (-b+math.sqrt(d))/(2*a)
	if d==0:
		print("x=", x1)
	else:
		print("x1=", x1 , " x2=", x2)
else:
	print("Нет действительных корней")