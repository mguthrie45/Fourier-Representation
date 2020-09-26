from math import sin, cos, sqrt
import parser

def parse_equation(equation):
	cleaned_equation_list = []
	for i in range(0, len(equation)):
		if equation[i] == '^':
			cleaned_equation_list.append('**')
		else:
			cleaned_equation_list.append(equation[i])
	cleaned_equation = ''.join(cleaned_equation_list)

	code = parser.expr(cleaned_equation).compile()
	return code