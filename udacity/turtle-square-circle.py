#!/usr/bin/python
import turtle

class draw(turtle.Turtle):
	def square(self,size):
		for i in range(4):
			self.forward(size)
			self.right(90)
	def square_circle(self,right_angle,size=100,color="Pink"):
		self.color(color)
		self.speed(20)
		# the circle is in all 360 degree , so we just need to draw that number of squares 
		times = 360/right_angle
		for i in range(times):
			self.right(right_angle)
			self.square(size)


window = turtle.Screen()

brad = draw()
brad.square(50)
brad.square_circle(10,color="Red")


window.exitonclick()
