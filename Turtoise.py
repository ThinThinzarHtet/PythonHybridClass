# from turtle import *

# color('red', 'yellow')
# begin_fill()
# while True:
# 	forward(200)
# 	left(170)
# 	if abs(pos()) < 1:
# 		break

# end_fill()
# done()

import turtle

triple = turtle.turtle()

for i in range(20):
	triple.forward(i * 10)
	triple.right(144)

turtle.done()