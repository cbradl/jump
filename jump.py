import unicornhathd
import time
import random

class Canvas:
    def __init__(self, canvas):
        self.canvas = canvas
        self.opening_act()
    def opening_act(self):
        self.canvas.reset()
        # specify graphic
        # wait until key pressed
    def add_player(self):

    def add_platform(self, last):



class Player:
    def __init__(self):
        self.shape = [[1,2],[1,3],[2,2],[2,3]]
        self.yvel = 0

    def start_jump():
        yvel = 3

    def get_yvel():
        return yvel


class Platform:
    def __init__(self, last):

def generate_platforms(number):
    platforms = [Platform() for x in range(number)]

def main():
    canvas = Canvas(unicornhathd)
    canvas.add_player()
    x = 0 # 0 frames in
    y = 2 #height of player
    generate_platforms(50)
