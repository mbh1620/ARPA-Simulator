import pygame
import math
from csv import reader


class plot:

	def __init__(self, _range, bearing, time, _pygame_class):
		self.range = _range
		self.bearing = bearing
		self.time = time
		self.x = 600+ (_range * math.sin(math.radians(bearing)))
		self.y = 600-(_range * math.cos(math.radians(bearing)))
		pygame.draw.circle(_pygame_class.screen,(0,0,255),(int(self.x),int(self.y)),2,1)


def read_in_plots(filename, _pygame_class):
	plots = []
	with open(filename) as file:
		csv_reader = reader(file, delimiter=",")
		for data in csv_reader:
			print(f"{data[0]} {data[1]} {data[2]}")
			new_plot = plot(int(data[0]), int(data[1]), int(data[2]), _pygame_class)
			plots.append(new_plot)

	return plots



class Vessel:

	def __init__(self, heading, speed, plots):
		self.heading = heading
		self.speed = speed
		self.plots = plots

	def draw(self, _pygame_class):
		pass


class Plotter:

	def __init__(self, heading, speed):
		self.heading = heading
		self.speed = speed

	def draw(self, _pygame_class):

		#Circle at center of screen

		pygame.draw.circle(_pygame_class.screen,(0,255,0),(600,600),600,1)
		pygame.draw.circle(_pygame_class.screen,(0,255,0),(600,600),500,1)
		pygame.draw.circle(_pygame_class.screen,(0,255,0),(600,600),400,1)
		pygame.draw.circle(_pygame_class.screen,(0,255,0),(600,600),300,1)
		pygame.draw.circle(_pygame_class.screen,(0,255,0),(600,600),200,1)
		pygame.draw.circle(_pygame_class.screen,(0,255,0),(600,600),100,1)
		# pygame.draw.line(_pygame_class.screen,(0,255,0),(600,600),300,1)

		# Center cross hair
		pygame.draw.line(_pygame_class.screen,(0,255,0), (605, 600), (595, 600), 1)
		pygame.draw.line(_pygame_class.screen,(0,255,0), (600, 605), (600, 595), 1)

		

		#Bearing rings
		x = 0
		while x < 360:
			x = x + 1
			x_comp = math.sin(math.radians(x))
			y_comp = math.cos(math.radians(x))
			if x <= 90:
				pygame.draw.line(_pygame_class.screen,(0,255,255), (600+(x_comp*600)-(5*x_comp), 600+(y_comp*600)-(5*y_comp)), (600+(x_comp*600), 600+(y_comp*600)), 1)
				if x % 10 == 0:
					pygame.draw.line(_pygame_class.screen,(0,255,255), (600+(x_comp*600)-(20*x_comp), 600+(y_comp*600)-(20*y_comp)), (600+(x_comp*600), 600+(y_comp*600)), 1)
				elif x % 5 == 0:
					pygame.draw.line(_pygame_class.screen,(0,255,255), (600+(x_comp*600)-(10*x_comp), 600+(y_comp*600)-(10*y_comp)), (600+(x_comp*600), 600+(y_comp*600)), 1)

			elif x <= 180 and x >= 90:
				pygame.draw.line(_pygame_class.screen,(0,255,255), (600-(x_comp*600)+(5*x_comp), 600-(y_comp*600)+(5*y_comp)), (600-(x_comp*600), 600-(y_comp*600)), 1)
				if x % 10 == 0:
					pygame.draw.line(_pygame_class.screen,(0,255,255), (600+(x_comp*600)-(20*x_comp), 600+(y_comp*600)-(20*y_comp)), (600+(x_comp*600), 600+(y_comp*600)), 1)
				elif x % 5 == 0:
					pygame.draw.line(_pygame_class.screen,(0,255,255), (600+(x_comp*600)-(10*x_comp), 600+(y_comp*600)-(10*y_comp)), (600+(x_comp*600), 600+(y_comp*600)), 1)

			elif x <= 270 and x >= 180:
				pygame.draw.line(_pygame_class.screen,(0,255,255), (600-(x_comp*600)+(5*x_comp), 600+(y_comp*600)-(5*y_comp)), (600-(x_comp*600), 600+(y_comp*600)), 1)
				if x % 10 == 0:
					pygame.draw.line(_pygame_class.screen,(0,255,255), (600+(x_comp*600)-(20*x_comp), 600+(y_comp*600)-(20*y_comp)), (600+(x_comp*600), 600+(y_comp*600)), 1)
				elif x % 5 == 0:
					pygame.draw.line(_pygame_class.screen,(0,255,255), (600+(x_comp*600)-(10*x_comp), 600+(y_comp*600)-(10*y_comp)), (600+(x_comp*600), 600+(y_comp*600)), 1)

			elif x <= 360 and x >= 270:
				pygame.draw.line(_pygame_class.screen,(0,255,255), (600+(x_comp*600)-(5*x_comp), 600-(y_comp*600)+(5*y_comp)), (600+(x_comp*600), 600-(y_comp*600)), 1)
				if x % 10 == 0:
					pygame.draw.line(_pygame_class.screen,(0,255,255), (600+(x_comp*600)-(20*x_comp), 600+(y_comp*600)-(20*y_comp)), (600+(x_comp*600), 600+(y_comp*600)), 1)
				elif x % 5 == 0:
					pygame.draw.line(_pygame_class.screen,(0,255,255), (600+(x_comp*600)-(10*x_comp), 600+(y_comp*600)-(10*y_comp)), (600+(x_comp*600), 600+(y_comp*600)), 1)

		#Draw own heading
		self.heading = int(self.heading)

		if self.heading <= 90:
			x = math.sin(math.radians(self.heading))*600
			y = -math.cos(math.radians(self.heading))*600
		elif self.heading <= 180 and self.heading >= 90:
			x = math.sin(math.radians(self.heading))*600
			y = -math.cos(math.radians(self.heading))*600
		elif self.heading <= 270 and self.heading >= 180:
			x = math.sin(math.radians(self.heading))*600
			y = -math.cos(math.radians(self.heading))*600
		elif self.heading <= 360 and self.heading >= 270:
			x = math.sin(math.radians(self.heading))*600
			y = -math.cos(math.radians(self.heading))*600

		pygame.draw.line(_pygame_class.screen, (0,255,255), (600,600), (600+x,600+y), 1)

		#Draw way of own (this is speed line and heading)
		x_speed = (x/600)*int(self.speed)
		y_speed = (y/600)*int(self.speed)

		pygame.draw.line(_pygame_class.screen, (255,0,0), (600,600), (600+x_speed,600+y_speed), 3)

		self.way_of_own_x = 600+x_speed
		self.way_of_own_y = 600+y_speed

		font = pygame.font.Font('freesansbold.ttf', 10)
		text = font.render(f'Speed: {self.speed} Heading:{self.heading}°', True, (0,255,0),(0,0,0))
		textRect = text.get_rect()
		textRect.center = (600, 20)
		_pygame_class.screen.blit(text, textRect)


class ARPA:

	def __init__(self,plotter, _pygame_class):
		self.plotter = plotter
		self._pygame_class = _pygame_class


	def calculate_Way_Of_Own(self, vessel):
		#Simply translate Way of own from plotter onto first point of vessels plots
		pygame.draw.line(self._pygame_class.screen, (255,0,0), (vessel.plots[0].x,vessel.plots[0].y), (vessel.plots[0].x - self.plotter.way_of_own_x+600,vessel.plots[0].y - self.plotter.way_of_own_y+600), 3)

	def calculate_Way_Of_Another(self, vessel):
		pygame.draw.line(self._pygame_class.screen, (255,255,100), (vessel.plots[0].x - self.plotter.way_of_own_x+600, vessel.plots[0].y - self.plotter.way_of_own_y+600), (vessel.plots[2].x,vessel.plots[2].y), 2)
		#Work out true course of other boat
		print(vessel.plots[2].x)
		print(vessel.plots[0].x - self.plotter.way_of_own_x+600)
		print(vessel.plots[2].y)
		print(vessel.plots[0].y - self.plotter.way_of_own_y+600)


		x_var = (vessel.plots[0].x - self.plotter.way_of_own_x+600) - vessel.plots[2].x 
		#print(f"vesselplot[0]({vessel.plots[0].x} - (self.plotter.way_of_own_x({self.plotter.way_of_own_x}+600)) - vessel.plots[2].x({vessel.plots[2].x}")
		print(f"x_var: {x_var}")
		y_var = -((vessel.plots[0].y - self.plotter.way_of_own_y+600) - vessel.plots[2].y)
		print(f"y_var: {y_var}")
		print

		add_factor = 0
		true_course = 90-math.degrees(math.atan((y_var)/x_var))
		print(f"true_course before correction {true_course}")

		# while true_course < 0:
		# 	print("add")
		# 	#add 90 until it becomes between 0 and 90 
		# 	true_course = true_course + 90
		# while true_course > 90: 
		# 	print("minus")
		# 	true_course = true_course - 90

		# if x_var >= 0 and y_var <= 0:
		# 	print("first quadrant")
		# 	#Must be in first quadrant
		# 	true_course = 90 - true_course
		# elif x_var >= 0 and y_var >= 0:
		# 	print("second quadrant")
		# 	#Second Quadrant so add 90 degrees
		# 	true_course = 90 + true_course
		# elif x_var <= 0 and y_var >= 0:
		# 	print("third quadrant")
		# 	#Third Quadrant so add 180 degrees
		# 	true_course = 270 - true_course
		# elif x_var <= 0 and y_var <= 0:
		# 	print("fourth quadrant")
		# 	#Fourth Quadrant so add 270 degrees
		# 	true_course = 270 + true_course

		'''


		'''
		print(f"True Course of another: {true_course}")
		#Work out true speed of other boat
		# (distance/plot length)*60 (Their true speed)
		#Distance between first and last/time * 60 
		y1 = vessel.plots[0].y
		y2 = vessel.plots[2].y
		x1 = vessel.plots[0].x
		x2 = vessel.plots[2].x

		distance = math.sqrt(math.pow(y1-y2,2) + math.pow(x1-x2,2))
		plot_length = vessel.plots[2].time - vessel.plots[0].time
		true_vessel_speed = (distance/plot_length) * 60

		print(f"True Vessel Speed: {true_vessel_speed}")

		self.target_vessel_true_speed = true_vessel_speed
		self.target_vessel_true_course = true_course

	def calculate_CPA(self, vessel):
		#Work out equation of line
		#y = mx + c REMEMBER Y IS FLIPPED

		#Work out m - gradient

		y1 = vessel.plots[0].y
		y2 = vessel.plots[2].y
		x1 = vessel.plots[0].x
		x2 = vessel.plots[2].x

		#gradient = Y2-Y1/ X1-X2

		self.gradient = (y2-y1)/(x2-x1)

		#now find y intercept using y1 and x1 and m

		#y1 - mx1 = c

		self.intercept = y1 - (self.gradient*x1)

		#Then use a function to find where along that line is closest and say what the distance of it is

		#distance between other ship and your ship 
		
		self.distances = {}
		x = 0
		while x < 1200:
			x = x + 1
			x1_dist = 600
			x2_dist = x
			y1_dist = 600
			y2_dist = (self.gradient*x2_dist)+self.intercept
			curr_distance = math.sqrt(math.pow(y1_dist-y2_dist,2) + math.pow(x1_dist-x2_dist,2))
			self.distances[x] = curr_distance

		self.min_dist = min(self.distances, key=lambda key: self.distances[key])

		y = (self.gradient*self.distances[self.min_dist]) + self.intercept

		#print(f"x: {distances[min_dist]}")
		#print(f"y: {y}")
		# print(distances)

		if self.distances[self.min_dist] < 1:

			print(f"WARNING! COLLISION COURSE The CPA is: {self.distances[self.min_dist]:.0f} miles")
			font = pygame.font.Font('freesansbold.ttf', 10)
			text = font.render(f'WARNING COLLISION', True, (255,0,0),(0,0,0))
			textRect = text.get_rect()
			textRect.center = (vessel.plots[0].x+70, vessel.plots[0].y+45)
			self._pygame_class.screen.blit(text, textRect)
		else:
			print(f"The CPA is: {self.distances[self.min_dist]:.0f} miles")

		#Draw on line of CPA 
		#work out whether to use which x above 600 or below 600

		if vessel.plots[0].x > 600:
			x = 1
		elif vessel.plots[0].x < 600:
			x = 1200

		pygame.draw.line(self._pygame_class.screen, (255,0,100), (vessel.plots[0].x, vessel.plots[0].y), (x,(self.gradient*x) + self.intercept), 1)
		
		font = pygame.font.Font('freesansbold.ttf', 10)
		text = font.render(f'CPA: {self.distances[self.min_dist]:.0f} miles', True, (0,0,255),(0,0,0))
		textRect = text.get_rect()
		textRect.center = (vessel.plots[0].x+70, vessel.plots[0].y+20)
		self._pygame_class.screen.blit(text, textRect)




	def calculate_TCPA(self, vessel):
		# Time = Distance/Speed

		#Distance from last plot to position of closest approach

		y1 = (self.gradient*self.distances[self.min_dist]) + self.intercept
		y2 = vessel.plots[2].y
		x1 = self.distances[self.min_dist]
		x2 = vessel.plots[2].x

		curr_distance = math.sqrt(math.pow(y1-y2,2) + math.pow(x1-x2,2))

		TCPA = curr_distance/self.target_vessel_true_speed
		font = pygame.font.Font('freesansbold.ttf', 10)
		text = font.render(f'TCPA: {TCPA:.0f} minutes', True, (0,0,255),(0,0,0))
		textRect = text.get_rect()
		textRect.center = (vessel.plots[0].x+70, vessel.plots[0].y+30)
		self._pygame_class.screen.blit(text, textRect)



	def text_to_screen(self, vessel):
		font = pygame.font.Font('freesansbold.ttf', 10)
		text = font.render(f'Speed: {self.target_vessel_true_speed:.2f}', True, (0,0,255),(0,0,0))
		text2 = font.render(f'Heading:{self.target_vessel_true_course:.2f}°', True, (0,0,255),(0,0,0))
		textRect = text.get_rect()
		textRect2 = text2.get_rect()
		textRect.center = (vessel.plots[0].x+70, vessel.plots[0].y)
		textRect2.center = (vessel.plots[0].x+70, vessel.plots[0].y+10)
		self._pygame_class.screen.blit(text, textRect)
		self._pygame_class.screen.blit(text2, textRect2)









class Pygame_class:

	def __init__(self, x=1200, y=1200):
		pygame.init()
		self.screen = pygame.display.set_mode((x, y))



