
import bone
from graphics import *

from tkinter.filedialog import askopenfilename

file_name = askopenfilename()
print(file_name)

width = 1280
height = 1024
win = GraphWin("Window 1", width, height)
win.setCoords(0, 0, width, height)
    
anchorPoint = Point(width/2,height/2)
    
img = Image(anchorPoint, file_name)
img.draw(win)


def main():  

    #Buttons to call bone angles

    lat = input("Lateral view? (y/n)" )

    t = bone.talus(win)
    
    print()
    
    n = bone.nav(win)

    print()
    
    c = bone.cune(win)

    print()
    
    mt = bone.meta_tar(win)

    print()

    if lat == "y" or "Y" or "yes" or "Yes":
        print()
        bone.bone_calc(t,n,c,mt,0)
        cp = bone.cal_p(win, t)
        ro = bone.ratio_overlap(win)
    else:
        print()
        pp = bone.prox_phal(win)
        bone.bone_calc(t,n,c,mt,pp)
        

    
    win.getMouse()
    
    win.close()
    

main()
