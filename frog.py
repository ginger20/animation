import pgzrun
from pgzhelper import *
from glob import glob

WIDTH=400
HEIGHT=400

tunes = [m[6:] for m in glob('music/*')]
tune = 0
print (tunes)

def on_key_down(key, mod, unicode):
    global tune

    #print(key, mod, unicode)
    if key == keys.SPACE:
        if music.is_playing(True):
            music.pause()
        else:
            music.unpause()
    elif key == keys.RIGHT:
        tune += 1
        tune = tune % len(tunes)
        print("TUNE=", tune)
        music.play(tunes[tune])  



music.play(tunes[tune])  

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

