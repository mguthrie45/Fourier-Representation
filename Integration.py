import EquationHandling
from math import sin, cos, sqrt

class Trapezoid():
	def __init__(self, x1, x2, y1, y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

	@property
	def area(self):
		a = self.y2
		b = self.y1
		h = self.x2 - self.x1
		return 0.5*(a+b)*h

def get_trapezoid_array(function, lowx, highx, n):
	t_array = []

	interval = float((highx-lowx)/n)
	for i in range(n):
		x1 = i*interval+lowx
		x2 = (i+1)*interval+lowx
		x=x1
		y1 = eval(function)
		x=x2
		y2 = eval(function)

		trapezoid = Trapezoid(x1, x2, y1, y2)
		t_array.append(trapezoid)

	return t_array

def integrate(parsed_function, lowx, highx):
	trap_array = get_trapezoid_array(parsed_function, lowx, highx, 100)
	area_array = [i.area for i in trap_array]

	return sum(area_array)