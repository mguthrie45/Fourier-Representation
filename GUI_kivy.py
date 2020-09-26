import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk
import Transform
import PiecewiseTransform

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (500, 600)

class Grid(GridLayout):
	def __init__(self, **kwargs):
		super(Grid, self).__init__(**kwargs)
		self.cols = 2

		self.piecewise_array = []

		self.inside = GridLayout(row_default_height=30, row_force_default=True)
		self.inside.cols = 2

		self.add_widget(self.inside)

		#self.inside.add_widget(Label(text='function f(x)', size_hint_x=None, width=100))
		'''self.function = TextInput(multiline=False, size_hint_x=None, width=150)
		self.inside.add_widget(self.function)

		self.inside.add_widget(Label(text='lowX', size_hint_x=None, width=100))
		self.lowx = TextInput(multiline=False, size_hint_x=None, width=150)
		self.inside.add_widget(self.lowx)
		self.inside.add_widget(Label(text='highX', size_hint_x=None, width=100))
		self.highx = TextInput(multiline=False, size_hint_x=None, width=150)
		self.inside.add_widget(self.highx)'''


		self.inside.add_widget(Label(text='New Piece', size_hint_x=None, width=100))
		self.inside.add_widget(Label(text='', size_hint_x=None, width=100))
		self.inside.add_widget(Label(text='piece p(x)', size_hint_x=None, width=100))
		self.new_function = TextInput(multiline=False, size_hint_x=None, width=150)
		self.inside.add_widget(self.new_function)
		self.inside.add_widget(Label(text='lowX', size_hint_x=None, width=100))
		self.piece_lowx = TextInput(multiline=False, size_hint_x=None, width=150)
		self.inside.add_widget(self.piece_lowx)
		self.inside.add_widget(Label(text='highX', size_hint_x=None, width=100))
		self.piece_highx = TextInput(multiline=False, size_hint_x=None, width=150)
		self.inside.add_widget(self.piece_highx)
		self.add_piece = Button(text='Add', size_hint_x=None, width=100)
		self.add_piece.bind(on_press=self.new_piece_press)
		self.inside.add_widget(self.add_piece)
		self.delete_piece_btn = Button(text='Delete Recent', size_hint_x=None, width=150)
		self.delete_piece_btn.bind(on_press=self.delete_piece)
		self.inside.add_widget(self.delete_piece_btn)

		self.plot = Button(text='plot', size_hint_x=None, width=100)
		self.plot.bind(on_press=self.plot_press)
		self.inside.add_widget(self.plot)


		self.function_inside = GridLayout(row_default_height=25, row_force_default=True)
		self.function_inside.cols = 1
		self.add_widget(self.function_inside)

		self.function_inside.add_widget(Label(text='Available Functions:', size_hint_x=None, width=200))
		self.function_inside.add_widget(Label(text='exponent: ^', size_hint_x=None, width=200))
		self.function_inside.add_widget(Label(text='multiplication: *', size_hint_x=None, width=200))
		self.function_inside.add_widget(Label(text='division: /', size_hint_x=None, width=200))
		self.function_inside.add_widget(Label(text='parenthases: ()', size_hint_x=None, width=200))
		self.function_inside.add_widget(Label(text='cosine: cos()', size_hint_x=None, width=200))
		self.function_inside.add_widget(Label(text='sine: sin()', size_hint_x=None, width=200))
		self.function_inside.add_widget(Label(text='arccosine: acos()', size_hint_x=None, width=200))
		self.function_inside.add_widget(Label(text='arcsine: asin()', size_hint_x=None, width=200))
		self.function_inside.add_widget(Label(text='arctangent: atan2()', size_hint_x=None, width=200))

		self.pieces_inside = GridLayout(row_default_height=25, row_force_default=True)
		self.pieces_inside.cols = 1
		self.add_widget(self.pieces_inside)

	def new_piece_press(self, instance):
		piece_lowx = self.piece_lowx.text
		piece_highx = self.piece_highx.text
		function = self.new_function.text

		if piece_lowx != "" and piece_highx != "" and function != "":
			piece_lowx = int(piece_lowx)
			piece_highx = int(piece_highx)
			self.piecewise_array.append({"function": Transform.Function(function), "lowx": piece_lowx, "highx": piece_highx})

			self.pieces_inside.clear_widgets()
			for i in self.piecewise_array:
				f = i['function'].string
				lx = i['lowx']
				hx = i['highx']
				self.pieces_inside.add_widget(Label(text=f'{f}, x in [{lx}, {hx}]'))

	def delete_piece(self, instance):
		if len(self.piecewise_array) > 0:
			self.piecewise_array.pop()

		self.pieces_inside.clear_widgets()
		for i in self.piecewise_array:
			f = i['function'].string
			lx = i['lowx']
			hx = i['highx']
			self.pieces_inside.add_widget(Label(text=f'{f}, x in [{lx}, {hx}]'))


	def plot_press(self, instance):
		if len(self.piecewise_array) > 0:
			PiecewiseTransform.plot_piecewise_fourier(self.piecewise_array)




class Application(App):
	def build(self):
		return Grid()

if __name__ == "__main__":
	Application().run()
