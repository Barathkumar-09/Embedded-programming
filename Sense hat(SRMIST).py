from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)  
def S():
    B = blue
    O = yellow
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, B, B, B, B, O, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, O, O, O,
    O, O, B, B, B, B, O, O,
    O, O, O, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    O, O, B, B, B, B, O, O,
    ]
    return logo
def R():
    B = blue
    O = yellow
    logo = [
    O, B, B, B, B, B, O, O, 
    O, B, B, B, B, B, O, O,
    O, B, B, O, O, B, B, O, 
    O, B, B, O, O, B, B, O,
    O, B, B, B, B, O, O, O,
    O, B, B, O, B, B, O, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    ]
    return logo
def M():
    B = blue
    O = yellow
    logo = [
    B, O, O, O, O, O, O, B, 
    B, B, O, O, O, O, B, B,
    B, B, B, O, O, B, B, B, 
    B, B, O, B, B, O, B, B,
    B, B, O, B, B, O, B, B, 
    B, B, O, O, O, O, B, B,
    B, B, O, O, O, O, B, B, 
    B, B, O, O, O, O, B, B,   
    ]
    return logo
def I():
    W = blue
    O = yellow
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
def T():
    P = blue
    O = yellow
    logo = [
    O, O, O, O, O, O, O, O,
    P, P, P, P, P, P, P, P,
    P, P, P, P, P, P, P, P,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    ]
    return logo
def heart():
    P = red
    O = yellow
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
images = [S,R,M,I,S, T, heart]
count = 0
while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1

