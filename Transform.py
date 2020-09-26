import EquationHandling
import Integration
from math import sin, cos, sqrt
import numpy as np
import matplotlib.pyplot as plt

def a_0(function, lowx, highx, L):
	#L = highx-lowx
	f = Function(function)
	a0 = f.integrate(lowx, highx)*(2/L)
	return a0

def a_n(function, n, lowx, highx, L):
	#L = highx-lowx
	cosConst = (n*3.14159*2)/L

	function = f'({function})*cos(x*{cosConst})'
	f = Function(function)
	an = f.integrate(lowx, highx)*(2/L)
	return an


def b_n(function, n, lowx, highx, L):
	#L = highx-lowx
	cosConst = (n*3.14159*2)/L

	function = f'({function})*sin(x*{cosConst})'
	f = Function(function)
	bn = f.integrate(lowx, highx)*(2/L)
	return bn

class Function():
	def __init__(self, string):
		self.string = string
		self.parsed = EquationHandling.parse_equation(self.string)

	def evaluate(self, x):
		return eval(self.parsed)

	def integrate(self, lowx, highx):
		result = Integration.integrate(self.parsed, lowx, highx)
		return result

	def get_fourier_array(self, x, N, lowx, highx):
		left_terms = []
		right_terms = []
		L = highx-lowx
		for i in range(N):
			an = a_n(self.string, i, lowx, highx, L)
			bn = b_n(self.string, i, lowx, highx, L)
			cosConst = (i*x*2*3.14159)/L
			left_term_equation = f'{an}*cos({cosConst})'
			left_term_function = Function(left_term_equation)
			left_term_val = left_term_function.evaluate(x)
			right_term_equation = f'{bn}*sin({cosConst})'
			right_term_function = Function(right_term_equation)
			right_term_val = right_term_function.evaluate(x)

			left_terms.append(left_term_val)
			right_terms.append(right_term_val)

		return {"left": left_terms, "right": right_terms}


	def get_fofx_fourier(self, x, N, lowx, highx):
		left_right_dict = self.get_fourier_array(x, N, lowx, highx)
		left = left_right_dict['left']
		right = left_right_dict['right']

		a0 = a_0(self.string, lowx, highx, highx-lowx)

		return a0 + sum(left) + sum(right)

	def get_fourier_xytuples(self, lowx, highx, iterations):
		period = highx-lowx
		step = period/iterations
		x_values = []
		y_values = []
		x_values = list(np.linspace(lowx, highx, iterations))
		y_values = [self.get_fofx_fourier(i, 50, lowx, highx) for i in x_values]

		xy_array = np.array([x_values, y_values])
		return xy_array.T

	def plot_fourier_repr(self, lowx, highx):
		plt.title(self.string)
		fourier_representation = self.get_fourier_xytuples(lowx, highx, 100)
		X_f = fourier_representation.T[0]
		Y_f = fourier_representation.T[1]
		X = list(np.linspace(lowx*1.1, highx*1.1, 100))
		Y = [self.evaluate(i) for i in X]


		maxY = max(max(Y), max(Y_f))
		minY = min(min(Y), min(Y_f))
		y_bounds = list(np.linspace(minY*1.1, maxY*1.1, 100))
		
		plt.plot([lowx]*100, y_bounds, dashes=[1, 3], linewidth=1)
		plt.plot([highx]*100, y_bounds, dashes=[1, 3], linewidth=1)

		plt.plot(X_f, Y_f, label="Fourier Representation")
		plt.plot(X, Y, label="Original f(x)")
		plt.legend(loc='lower right')
		plt.show()



