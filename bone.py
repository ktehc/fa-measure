#Bone Functions:

"""Calculates angles of bone articular surface relative to standard XY axis,
with lower left corner defined as (0,0) in the image viewing window"""

from graphics import *
import math

def talus(win):
    """Talus Angle Calculation"""
        
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
    
    return talus_angle


def nav(win):
    """Navicular Angle Calculation"""
    
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
    
    return nav_angle

def cune(win):
    """Cuneiform Angle Calculation"""
    
    cune_pt1 = win.getMouse()
    cune_pt1.draw(win)
    
    cune_pt2 = win.getMouse()
    cune_pt2.draw(win)

    cune_line = Line(cune_pt1, cune_pt2)
    cune_line.draw(win)

    cune_slope = (cune_pt2.y - cune_pt1.y)/(cune_pt2.x - cune_pt1.x)
    cune_angle = math.degrees(math.atan(cune_slope))
    
    print("Cuneiform slope =", cune_slope)
    print("Cuneiform angle =", cune_angle)
    
    return cune_angle


def bone_calc(talus_angle,nav_angle,cune_angle,mt=0,pp=0):
    
    talus_nav_angle = nav_angle - talus_angle
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
        
    print()

