from p5 import *
import winsound

yellow = Color(255, 255, 0, 255)
blue = Color(97, 156, 250, 255)
count = 0
precision = 2   # Precision value specifies the digits up to which Pi is recorded.
timestep = 100  # Make sure to increase the timestep as you increase precision, to avoid breaking the code.


class Box:
    def __init__(self, x, w, m, v, xConstraint):
        self.x = x
        self.w = w
        self.m = m
        self.v = v
        self.xConstraint = xConstraint

    def update(self):
        self.x += self.v

    def show(self):
        fill(blue)
        x = constrain(self.x, self.xConstraint, 800)
        square(x, 350 - self.w, self.w)

    def collide(self, other):
        if self.x + self.w < other.x or self.x > other.x + other.w:
            return False
        else:
            return True

    def collision(self, other):
        sumM = self.m + other.m
        finalV = ((self.m - other.m) / sumM) * self.v + (2 * other.m / sumM) * other.v
        return finalV

    def wall(self):
        if self.x < 0:
            return True
        else:
            return False


smallB = Box(100, 50, 1, 0, 0)  # (X_Position, Size, Mass, Initial_Velocity, ConstrainX)

largeB = Box(300, 150, 100 ** (precision - 1), -5 / timestep, 50)

# Constrain is not to blow the block beyond the wall

f = create_font("Arial.ttf", 30)

def setup():
    size(800, 400)




def draw():
    global smallB, largeB, count, timestep, f

    brkval = False
    sound = False
    background(0)
    stroke(yellow)
    stroke_weight(5)
    line(5, 350, 5, 0)
    line(5, 350, 800, 350)
    stroke_weight(3)
    for i in range(timestep):
        if smallB.collide(largeB):  # Checking collision with each other
            v1 = smallB.collision(largeB)
            v2 = largeB.collision(smallB)
            smallB.v = v1
            largeB.v = v2
            count += 1
            sound = True

        if smallB.wall():  # Checking Collision with Wall
            smallB.v *= -1
            count += 1
            sound = True

        if largeB.x > 800:
            brkval = True
            break

        smallB.update()  # Updating Velocities and Positions
        largeB.update()

    if brkval:
        exit()

    smallB.show()  # Drawing the Boxes
    largeB.show()
    if sound:
        winsound.PlaySound('clack.wav', winsound.SND_ASYNC)
    text_font(f, 30)
    text(f"Precision : {precision}", (10, 70))
    text(f"Pi Digits : {count/(10**(precision-1))}", (10, 100))

    print(f'Pi Digits : {count/(10**(precision-1))}')



run(frame_rate=60)
