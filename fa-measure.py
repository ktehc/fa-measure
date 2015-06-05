
#and 	as 	assert 	break 	class 	continue
#def 	del 	elif 	else 	except 	exec
#finally 	for 	from 	global 	if 	import
#in 	is 	lambda 	not 	or 	pass
#print 	raise 	return 	try 	while 	with
#yield 	  	  	  	  	 

import math
import bone

from graphics import *

import tkinter as tk

from tkinter.filedialog import askopenfilename

file_name = askopenfilename()
print(file_name)

width = 800
height = 800
win = GraphWin("Window 1", width, height)
win.setCoords(0, 0, width, height)
    
anchorPoint = Point(width/2,height/2)
    
img = Image(anchorPoint, file_name)
img.draw(win)

#gui = GraphWin("Options", 100, 100)

def main():  

    #Buttons to call bone angles
    
    txt = Text(Point(width/4,height/4), "Select Talus Points")
    color = "red"
    txt.setTextColor(color)
    txt.draw(win)


    t = bone.talus(win)
    
    print()
    n = bone.nav(win)

    print()
    c = bone.cune(win)
    

    bone.bone_calc(t,n,c)
    
    win.getMouse()
    win.close()

main()




    #prpnd = Line(mid,
        
    #mid = d.getCenter()

    #print(b.getX(),b.getY())
    #print(c.getX(),c.getY())
    
    #print("Midpoint(x,y) =", mid.x, mid.y)

"""talus_nav_angle = nav_angle - talus_angle
    print()
    print("Talo-Navicular Angle =", talus_nav_angle)
    if talus_nav_angle < 0:
        print("Valgus")
    elif talus_nav_angle > 0:
        print("Varus")
    else:
        print("Aligned")

    print()

    nav_cune_angle = cune_angle - nav_angle
    print("Naviculo-Cuneiform Angle =", nav_cune_angle)

    if nav_cune_angle < 0:
        print("Valgus")
    elif nav_cune_angle > 0:
        print("Varus")
    else:
        print("Aligned")
        
    print()"""

