#Bone Functions:

"""Calculates angles of bone articular surface relative to standard XY axis,
with lower left corner defined as (0,0) in the image viewing window"""

from graphics import *
import math

def talus(win):
    """Talus Angle Calculation"""

    print("Select Talus points.")
    
    talus_pt1 = win.getMouse()
    talus_pt1.draw(win)
    
    talus_pt2 = win.getMouse()
    talus_pt2.draw(win)

    talus_line = Line(talus_pt1, talus_pt2)
    talus_line.setFill("red")
    talus_line.setWidth(3)
    talus_line.draw(win)

    talus_slope = (talus_pt2.y - talus_pt1.y)/(talus_pt2.x - talus_pt1.x)
    talus_angle = math.degrees(math.atan(talus_slope))
    
    print("Talus slope =", talus_slope)
    print("Talus angle =", talus_angle)
    
    return talus_angle


def nav(win):
    """Navicular Angle Calculation"""

    print("Select Navicular points.")
    
    nav_pt1 = win.getMouse()
    nav_pt1.draw(win)
    
    nav_pt2 = win.getMouse()
    nav_pt2.draw(win)

    nav_line = Line(nav_pt1, nav_pt2)
    nav_line.setFill("cyan")
    nav_line.setWidth(3)
    nav_line.draw(win)

    nav_slope = (nav_pt2.y - nav_pt1.y)/(nav_pt2.x - nav_pt1.x)
    nav_angle = math.degrees(math.atan(nav_slope))
    
    print("Navicular slope =", nav_slope)
    print("Navicular angle =", nav_angle)
    
    return nav_angle

def cune(win):
    """Cuneiform Angle Calculation"""

    print("Select Cuneiform points.")
    
    cune_pt1 = win.getMouse()
    cune_pt1.draw(win)
    
    cune_pt2 = win.getMouse()
    cune_pt2.draw(win)

    cune_line = Line(cune_pt1, cune_pt2)
    cune_line.setFill("yellow")
    cune_line.setWidth(3)
    cune_line.draw(win)

    cune_slope = (cune_pt2.y - cune_pt1.y)/(cune_pt2.x - cune_pt1.x)
    cune_angle = math.degrees(math.atan(cune_slope))
    
    print("Cuneiform slope =", cune_slope)
    print("Cuneiform angle =", cune_angle)
    
    return cune_angle

def meta_tar(win):
    """1st Metatarsal Angle Calculation"""

    print("Select proximal points for 1st Metatarsal.")
    
    mt_pt1 = win.getMouse()
    mt_pt1.draw(win)
    
    mt_pt2 = win.getMouse()
    mt_pt2.draw(win)

    prox_mt_line = Line(mt_pt1, mt_pt2)
    prox_mt_line.draw(win)

    print("Select distal points for 1st Metatarsal.")
    
    mt_pt3 = win.getMouse()
    mt_pt3.draw(win)
    
    mt_pt4 = win.getMouse()
    mt_pt4.draw(win)

    dist_mt_line = Line(mt_pt3, mt_pt4)
    dist_mt_line.draw(win)


    prox_mt_mid = prox_mt_line.getCenter()
    dist_mt_mid = dist_mt_line.getCenter()
    
    mt_la = Line(prox_mt_mid, dist_mt_mid)
    mt_la.setFill("orange")
    mt_la.setWidth(3)
    mt_la.draw(win)

    if dist_mt_mid.x == prox_mt_mid.x:
        mt_angle = 90
    else:
        mt_slope = (dist_mt_mid.y - prox_mt_mid.y)/(dist_mt_mid.x - prox_mt_mid.x)
        mt_angle = math.degrees(math.atan(mt_slope))
    
    print("1st Metatarsal slope =", mt_slope)
    print("1st Metatarsal angle =", mt_angle)
    
    return mt_angle

def prox_phal(win):
    """Proximal Phalanx Angle Calculation"""

    print("Select proximal points for Proximal Phalanx")
    
    pp_pt1 = win.getMouse()
    pp_pt1.draw(win)
    
    pp_pt2 = win.getMouse()
    pp_pt2.draw(win)

    prox_pp_line = Line(pp_pt1, pp_pt2)
    prox_pp_line.draw(win)

    print("Select distal points for Proximal Phalanx")

    pp_pt3 = win.getMouse()
    pp_pt3.draw(win)
    
    pp_pt4 = win.getMouse()
    pp_pt4.draw(win)

    dist_pp_line = Line(pp_pt3, pp_pt4)
    dist_pp_line.draw(win)

    prox_pp_mid = prox_pp_line.getCenter()
    dist_pp_mid = dist_pp_line.getCenter()
    
    pp_la = Line(prox_pp_mid, dist_pp_mid)
    pp_la.setFill("white")
    pp_la.setWidth(3)
    pp_la.draw(win)

    if dist_pp_mid.x == prox_pp_mid.x:
        pp_angle = 90
    else:
        pp_slope = (dist_pp_mid.y - prox_pp_mid.y)/(dist_pp_mid.x - prox_pp_mid.x)
        pp_angle = math.degrees(math.atan(pp_slope))
    
    print("Proximal Phalanx slope =", pp_slope)
    print("Proximal Phalanx angle =", pp_angle)
    
    return pp_angle


def bone_calc(talus_angle,nav_angle,cune_angle,mt_angle,pp_angle):

    talus_mt_angle = 90 - (mt_angle - talus_angle)
    print("Talus90-1st Metatarsal Angle =", talus_mt_angle)
        
    print()
    
    talus_nav_angle = nav_angle - talus_angle
    print("Talo-Navicular Angle =", talus_nav_angle)

    print()

    nav_cune_angle = cune_angle - nav_angle
    print("Naviculo-Cuneiform Angle =", nav_cune_angle)

    print()

    cune_mt_angle = 90 - (mt_angle - cune_angle)
    print("90Cuneiform-1st Metatarsal Angle =", cune_mt_angle)
        
    print()

    mt_pp_angle = pp_angle - mt_angle
    print("1st Metatarsal-Proximal Phalanx Angle =", mt_pp_angle)


    
