import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt

class import_path(tk.Tk):

	'''This class provides the viualization window for the user to draw a path. 
	The coordinates of the path are then recorded in a list for future use
	
	credit to: stack_exchange_40604233 for base design'''

	def __init__(self):
		'''Initialize class; create canvas for gui and set initial variables'''
		tk.Tk.__init__(self)
		self.width = 600
		self.height = 600
		self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg = "black")
		self.canvas.pack(side="top", fill="both", expand=True)
		
		#intialize variables
		self.counter = 0
		self.previous_x = self.previous_y = 300
		self.current_x = self.current_y = 300
		self.coordinate_list = []
		
		#bind commands
		self.bind('<B1-Motion>', self.position_previous)
		self.canvas.bind('<B1-Motion>', self.draw_line)

	def position_previous(self,event):
		'''Need the track the previous position for drawing lines'''
	
		self.previous_x = event.x
		self.previous_y = event.y

	def draw_line(self, event):
		'''Visualize the path as it's being drawn'''
	
		#if this is the first click, intialize near the click
		if self.counter == 0:
			self.previous_x = event.x + 1
			self.previous_y = event.y
	
		self.current_x = event.x
		self.current_y = event.y

		self.canvas.create_line(self.previous_x, self.previous_y, 
			self.current_x, self.current_y,
			fill="white")
			
		self.previous_x = event.x
		self.previous_y = event.y
		
		self.counter += 1

if __name__ == "__main__":

	#create gui object, name main window root
	root = import_path()

	#start event driven loop
	root.mainloop()
	
	
	
	
	
	
