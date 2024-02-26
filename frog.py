import pgzrun
from pgzhelper import *
from glob import glob

WIDTH=400
HEIGHT=400

play_button = Actor('pause', (50, 350))
play_button.scale = 0.1
next_button = Actor('next', (110, 350))
next_button.scale = 0.1

tunes = [m[6:] for m in glob('music/*')]
tune = 0
print (tunes)

def next_tune():
    global tune

    tune += 1
    tune = tune % len(tunes)
    print("TUNE=", tune)
    music.play(tunes[tune])  

def startstop():
    if music.is_playing(True):
        music.pause()
        play_button.image = 'play'
        play_button.scale = 0.1

    else:
        music.unpause()
        play_button.image = 'pause'
        play_button.scale = 0.1


def on_key_down(key, mod, unicode):

    #print(key, mod, unicode)
    if key == keys.SPACE:

       startstop()
        
    elif key == keys.RIGHT:
        next_tune()

def on_mouse_down(pos):
    print(pos)

    #(82, 321)
    #(139, 376)

    if 82 <= pos[0] <= 321 and 139 <= pos[1] <= 376:
        next_tune()   
    elif 28 <= pos[0] <= 60 and 323 <= pos[1] <= 366:
        startstop()          


music.play(tunes[tune])  

frog = Actor('frog001')
images = ['frog{0:03}'.format(i) for i in range(1, 12)]
print(images)

frog.images = images

def draw():
    frog.draw()
    play_button.draw()
    next_button.draw()

counter = 0

def update():
    global counter
    if counter % 5 == 0:
        frog.next_image()
    counter += 1

pgzrun.go()

