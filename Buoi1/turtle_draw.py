from turtle import *

#direction

#pen
pensize(5)
color('pink')
shape(name='turtle')
#square
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
#pentagon   
up()
setposition(-300, 0)
down()

forward(100)
left(72)    
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
forward(100)  
# circle
up()
setposition(100, 40)
down()
circle(radius=60    )
# star 
up()
setposition(100, 100)
down()                                              
left(180-36)
left(180-36)
forward(100)
left(180-36)
forward(100)
left(180-36)    
forward(100)
left(180-36)
forward(100)
mainloop()