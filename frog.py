import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

frog = Actor('frog001')
images = ['frog{0:03}'.format(i) for i in range(1, 12)]
print(images)

frog.images = images

def draw():
    frog.draw()

counter = 0

def update():
    global counter
    if counter % 5 == 0:
        frog.next_image()
    counter += 1

pgzrun.go()

