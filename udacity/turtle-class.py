#!/usr/bin/python

import turtle

class Turtle_Artist(turtle.Turtle):
	def square(self, size):
		for i in range(4):
			self.forward(size)
			self.right(90)

	def triangle(self,ang_step1,ang_step2):
		self.turn_move(ang_step1)
		self.turn_move(ang_step2)
		self.home()

	def turn_move(self, angle_dist):
		"""Pass in (ang, dist) for turtle to turn and move """
		self.right(angle_dist[0])
		self.forward(angle_dist[1])

	def draw_crazy_circle(self, size):
		for i in range(80):
			self.right(5)
			self.square(size)

	def style(self, color='#009b30', shape='turtle', speed=0.1, pen=(0,0,0)):
		self.color(color)
		self.pencolor(pen[0], pen[1], pen[2])
		self.shape(shape)
		self.speed(speed)


def turtle_power():
	''''Create the window and watch turtles play '''
	win = turtle.Screen()
	# Set bg to image of sand
	win.bgpic('sand.gif')
	win.screensize(400,400)


	# Bradley, average turtle, likes squares
	brad = Turtle_Artist()
	brad.style()
	# Have Bradely use the custom square method
	brad.square(100)

	# Angie, Change her color and shape
	angie = Turtle_Artist()
	angie.style(shape='arrow',pen=(0.6, 0.0, 0.0))
	# since circle is defined by turtle.Turtle, we don't need to create it
	angie.circle(80)

	# Wesley, the circle who draws triangles quickley!
	wesley = Turtle_Artist()
	wesley.style(speed=10, shape='circle', pen=(0.5, 0.2, 0.3))
	# Call custom triangle method with 2 sets of (angle, distance)
	wesley.triangle((120,220), (40,100))
	wesley.draw_crazy_circle(60)

	win.exitonclick()


turtle_power()