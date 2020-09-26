from Transform import *

def piecewise_a0(piecewise_array):
	abs_highx = max([i['highx'] for i in piecewise_array])
	abs_lowx = min([i['lowx'] for i in piecewise_array])
	L = abs_highx-abs_lowx
	a0 = 0
	for i in piecewise_array:
		a0 += a_0(i['function'].string, i['lowx'], i['highx'], L)
	return a0
def piecewise_an(piecewise_array, n):
	abs_highx = max([i['highx'] for i in piecewise_array])
	abs_lowx = min([i['lowx'] for i in piecewise_array])
	L = abs_highx-abs_lowx
	an = 0
	for i in piecewise_array:
		an += a_n(i['function'].string, n, i['lowx'], i['highx'], L)
	return an
def piecewise_bn(piecewise_array, n):
	abs_highx = max([i['highx'] for i in piecewise_array])
	abs_lowx = min([i['lowx'] for i in piecewise_array])
	L = abs_highx-abs_lowx
	bn = 0
	for i in piecewise_array:
		bn += b_n(i['function'].string, n, i['lowx'], i['highx'], L)
	return bn

def get_piecewise_fourier_array(piecewise_array, x, N):
	left_terms = []
	right_terms = []

	abs_highx = max([i['highx'] for i in piecewise_array])
	abs_lowx = min([i['lowx'] for i in piecewise_array])
	period = abs_highx-abs_lowx
	for i in range(N):
		an = piecewise_an(piecewise_array, i)
		bn = piecewise_bn(piecewise_array, i)
		cosConst = (i*x*2*3.14159)/period
		left_term_equation = f'{an}*cos({cosConst})'
		left_term_function = Function(left_term_equation)
		left_term_val = left_term_function.evaluate(x)
		right_term_equation = f'{bn}*sin({cosConst})'
		right_term_function = Function(right_term_equation)
		right_term_val = right_term_function.evaluate(x)

		left_terms.append(left_term_val)
		right_terms.append(right_term_val)

	return {"left": left_terms, "right": right_terms}

def get_piecewise_fofx_fourier(piecewise_array, x, N):
	left_right_dict = get_piecewise_fourier_array(piecewise_array, x, N)
	left = left_right_dict['left']
	right = left_right_dict['right']

	a0 = piecewise_a0(piecewise_array)

	return a0/2 + sum(left) + sum(right)

def get_piecewise_fourier_xytuples(piecewise_array, iterations):
	abs_highx = max([i['highx'] for i in piecewise_array])
	abs_lowx = min([i['lowx'] for i in piecewise_array])

	period = abs_highx-abs_lowx
	step = period/iterations
	x_values = []
	y_values = []
	x_values = list(np.linspace(abs_lowx, abs_highx, iterations))
	y_values = [get_piecewise_fofx_fourier(piecewise_array, i, 50) for i in x_values]

	xy_array = np.array([x_values, y_values])
	return xy_array.T

def plot_piecewise_fourier(piecewise_array):
	plt.title("F(x)")

	represent = get_piecewise_fourier_xytuples(piecewise_array, 200)
	xf_array = represent.T[0]
	yf_array = represent.T[1]
	X = []
	Y = []

	abs_highx = max([i['highx'] for i in piecewise_array])
	abs_lowx = min([i['lowx'] for i in piecewise_array])


	for i in piecewise_array:
		lowx = i["lowx"]
		highx = i["highx"]
		function = i['function']
		#represent = function.get_fourier_xytuples(lowx, highx, 100)
		#xf_array += list(represent.T[0])
		#yf_array += list(represent.T[1])
		x_added = list(np.linspace(lowx*1.1, highx*1.1, 100))
		X += x_added
		Y += [function.evaluate(i) for i in x_added]

	maxY = max(max(Y), max(yf_array))
	minY = min(min(Y), min(yf_array))
	y_bounds = list(np.linspace(minY*1.1, maxY*1.1, 100))
		
	plt.plot([abs_lowx]*100, y_bounds, dashes=[1, 3], linewidth=1)
	plt.plot([abs_highx]*100, y_bounds, dashes=[1, 3], linewidth=1)

	plt.plot(xf_array, yf_array, label="Fourier Representation")
	plt.plot(X, Y, label="Original f(x)")
	plt.legend(loc='lower right')
	plt.show()