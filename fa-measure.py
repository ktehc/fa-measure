
import bone
from graphics import *

from tkinter.filedialog import askopenfilename

file_name = askopenfilename()
print(file_name)

width = 1200
height = 800
win = GraphWin("Window 1", width, height)
win.setCoords(0, 0, width, height)
    
anchorPoint = Point(width/2,height/2)
    
img = Image(anchorPoint, file_name)
img.draw(win)


def main():  

    #Buttons to call bone angles

    color = 'red'
    
    txt = Text(Point(width/4,height/4), "Select Talus Points")
    txt.setTextColor(color)
    txt.draw(win)

    t = bone.talus(win)
    
    print()
    
    n = bone.nav(win)

    print()
    
    c = bone.cune(win)

    print()
    
    mt = bone.meta_tar(win)

    print()
    
    pp = bone.meta_tar(win)

    bone.bone_calc(t,n,c,mt,pp)

    
    win.getMouse()
    win.close()

main()
