import pygame
import os
pygame.init()
from spareScripts import Characters
#dis=pygame.display.set_mode((800,600))

black=(0,0,0)
color=(59,67,196)
gameClose=False

def img(imgname):
    os.path.join(os.path.dirname(__file__),"charImages",imgname+".png")

def run(pyname):
    os.path.join(os.path.dirname(__file__),"spareScripts",pyname)

dis=pygame.display.set_mode((1000,750))
dis.fill(color)
pygame.display.set_caption("aaaaa")



#alternative:
#subprocess.run(["python", "other.py"])

print(Characters.noelle.name)
#import Characters

#pygame.image.load( os.path.join(os.path.dirname(__file__),"testing.png"))

    
while not gameClose:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameClose=True
    pygame.display.update()
    pygame.time.Clock().tick(60)
    pygame.display.update()

pygame.quit()