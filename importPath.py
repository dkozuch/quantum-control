import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt

"""@package docstring`

This module exists to hold the import_path class, which takes user input and returns the data array for the desired path
All inputs come through the Tkinter GUI that is opened for the user
The user is given the option to: 
    1. Draw their path with the cursor
    2. Load a path from file
    3. Enter an analytic formula
.
"""

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
		
		#add buttons		
		self.button_clear = tk.Button(self, text = "Select File", command = self.load_from_file)
		self.button_clear.pack(side="top", fill="both", expand=True)
		
		self.button_clear = tk.Button(self, text = "Clear", command = self.clear)
		self.button_clear.pack(side="top", fill="both", expand=True)
		
		#bind commands
		self.bind('<B1-Motion>', self.position_previous)
		self.canvas.bind('<B1-Motion>', self.draw_line)
		self.bind('<B1-Motion>',self.record_coordinates)

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
		
	def record_coordinates(self, event):
		'''Keep every coordinate in a list, but not repeating coordinates
		NOTE: need to subtract y from height since pixels are recorded from top'''
		
		if len(self.coordinate_list) == 0:
			self.coordinate_list.append([event.x, self.height - event.y])
		#don't record duplicates
		else:
			if event.x != self.coordinate_list[-1][0] or event.y != self.coordinate_list[-1][1]:
				self.coordinate_list.append([event.x, self.height - event.y])
				
	def clear(self):
		'''Clear all data held in the object and start over'''
		
		#clear canvas
		self.canvas.delete("all")
		
		#re-instatiate variables
		#intialize variables
		self.counter = 0
		self.previous_x = self.previous_y = 300
		self.current_x = self.current_y = 300
		self.coordinate_list = []
		
	def load_from_file(self):
		'''Allow user to choose file for input'''
		filename = filedialog.askopenfilename(parent=root, initialdir="./", title='Please select a file')
		self.coordinate_list = np.loadtxt(filename, comments = ('#'))
		self.destroy()
		
	def get_coordinates(self):
		'''Returns the list of coordinates as numpy array'''
		coords = np.array(self.coordinate_list)
		return coords
		
	def plot_coordinates(self):
		'''Plot coordinates held in coordinate list'''
		coords = self.get_coordinates()
		coords = root.get_coordinates()
		color_idx = np.linspace(0, 1, len(coords))
		for i in range(0,len(coords)):
			plt.plot([coords[i,0]],[coords[i,1]],'o',color=plt.cm.cool(color_idx[i]))
		plt.show()

if __name__ == "__main__":

	#create gui object, name main window root
	root = import_path()

	#start event driven loop
	root.mainloop()
	
	#plot to check
	root.plot_coordinates()
	
	
	
	
	
	
