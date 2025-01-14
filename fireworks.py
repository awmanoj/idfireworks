#!/usr/bin/env python3

from asciimatics.effects import Stars, Print
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
    PalmFirework
from asciimatics.renderers import SpeechBubble, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers.images import ColourImageFile
from random import randint, choice
import sys
from playsound import playsound
import threading

def play_anthem():
    playsound('anthem.mp3')

def demo(screen):
    scenes = []
    effects = [
        Stars(screen, screen.width),
        Print(screen,
              SpeechBubble("Press space to see it again or q to quit"),
              y=screen.height - 3,
              start_frame=300)
    ]
    for _ in range(20):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (RingFirework, 20, 30),
            (SerpentFirework, 30, 35),
        ]
        firework, start, stop = choice(fireworks)
        effects.insert(
            1,
            firework(screen,
                     randint(0, screen.width),
                     randint(screen.height // 8, screen.height * 3 // 4),
                     randint(start, stop),
                     start_frame=randint(0, 250)))

    effects.append(Print(screen,
                         FigletText("Happy"),
                         screen.height // 2 - 10,
                         speed=1,
                         colour=1,
                         start_frame=100))
    effects.append(Print(screen,
                         FigletText("79th Birthday"),
                         screen.height // 2 - 3,
                         speed=1,
                         start_frame=100))    
    effects.append(Print(screen,
                         FigletText("Indonesia!"),
                         screen.height // 2 + 4,
                         speed=1,
                         start_frame=100))
    effects.append(Print(screen,
                         ColourImageFile(screen, "flag.gif"),
                         screen.height // 2 - 16,
                         speed=1,
                         start_frame=200))

    scenes.append(Scene(effects, -1))
    # Create a thread to play the sound
    sound_thread = threading.Thread(target=play_anthem)

    # Start the thread
    sound_thread.start()

    screen.play(scenes, stop_on_resize=True)

    # Optionally, wait for the thread to finish
    sound_thread.join()

while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass
