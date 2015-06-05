
#and 	as 	assert 	break 	class 	continue
#def 	del 	elif 	else 	except 	exec
#finally 	for 	from 	global 	if 	import
#in 	is 	lambda 	not 	or 	pass
#print 	raise 	return 	try 	while 	with
#yield 	  	  	  	  	 

import math

from graphics import *

import tkinter as tk

from tkinter.filedialog import askopenfilename
file_name = askopenfilename()
print(file_name)

def main():

    width = 800
    height = 800
    win = GraphWin("Window 1", width, height)

    win.setCoords(0, 0, width, height)
    
    anchorPoint = Point(width/2,height/2)
    
    img = Image(anchorPoint, file_name)
    img.draw(win)

    #Buttons to call bone angles
    
    talus_pt1 = win.getMouse()
    talus_pt1.draw(win)
    
    talus_pt2 = win.getMouse()
    talus_pt2.draw(win)

    talus_line = Line(talus_pt1, talus_pt2)
    talus_line.draw(win)

    talus_slope = (talus_pt2.y - talus_pt1.y)/(talus_pt2.x - talus_pt1.x)
    talus_angle = math.degrees(math.atan(talus_slope))
    
    print("Talus slope =", talus_slope)
    print("Talus angle =", talus_angle)

    #adjust div by zero
    #if talus_pt2.x != talus_pt1.x:
        #talus_slope = (talus_pt2.y - talus_pt1.y)/(talus_pt2.x - talus_pt1.x)
        #talus_angle = math.degrees(math.atan(talus_slope))
    #else:
        #print("Select a valid point")

    


    nav_pt1 = win.getMouse()
    nav_pt1.draw(win)
    
    nav_pt2 = win.getMouse()
    nav_pt2.draw(win)

    nav_line = Line(nav_pt1, nav_pt2)
    nav_line.draw(win)

    nav_slope = (nav_pt2.y - nav_pt1.y)/(nav_pt2.x - nav_pt1.x)
    nav_angle = math.degrees(math.atan(nav_slope))
    print("Navicular slope =", nav_slope)
    print("Navicular angle =", nav_angle)


    talus_nav_angle = nav_angle - talus_angle
    print("Talo-Navicular Angle =", talus_nav_angle)

    if talus_nav_angle < 0:
        print("Valgus")
    elif talus_nav_angle > 0:
        print("Varus")
    else:
        print("Aligned")
    
    #prpnd = Line(mid,
        
    #mid = d.getCenter()

    #print(b.getX(),b.getY())
    #print(c.getX(),c.getY())
    
    #print("Midpoint(x,y) =", mid.x, mid.y)
    
    
    win.getMouse()
    win.close()

main()





