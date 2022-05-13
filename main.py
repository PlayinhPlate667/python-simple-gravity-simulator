import pygame
pygame.init()
from pygame import display, event, time, draw, Surface
import math as m

XS, YS = 1200, 700

win = display.set_mode((XS, YS))
display.set_caption("Gravity simulator - sucsess stable work")
timer = time.Clock()
FPS = 60
# constant in formule
G = 6

class vec2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @property
    def xy(self): return self.x, self.y

class vec3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    @property
    def xy(self):return self.x, self.y
    @property
    def xz(self):return self.x, self.z
    @property
    def yz(self):return self.y, self.z
    @property
    def xyz(self):return self.x, self.y, self.z

class Body:
    def __init__(self, pos:vec2, direction:vec2, mass:int, radius:float, color:vec3):
        self.mass = mass
        self.pos = pos
        self.dir = direction
        self.radius = radius
        self.color = color
    
    def render(self, sc:Surface):
        draw.circle(sc,  self.color.xyz, self.pos.xy, self.radius)

    def update(self):
        self.pos.x += self.dir.x
        self.pos.y += self.dir.y

bl = []
bl.append(Body(pos=vec2(400, 400), direction=vec2(0, 0), mass=1000, radius=15., color=vec3(63, 7, 88)))
bl.append(Body(pos=vec2(600, 400), direction=vec2(0, -5), mass=10, radius=5., color=vec3(7, 56, 88)))
bl.append(Body(pos=vec2(200, 400), direction=vec2(0, 5), mass=10, radius=5., color=vec3(7, 56, 88)))
bl.append(Body(pos=vec2(400, 600), direction=vec2(5, 0), mass=10, radius=5., color=vec3(7, 56, 88)))
bl.append(Body(pos=vec2(400, 200), direction=vec2(-5, 0), mass=10, radius=5., color=vec3(7, 56, 88)))

def renderAll(bl:list[Body], sc: Surface):
    for obj in bl:
        obj.render(sc)
    
def updateAll(bl:list[Body]):
    for obj in bl:
        obj.update()

def calcAll(bl:list[Body]):
    for b1 in bl:
        for b2 in bl:
            if b1.pos.xy != b2.pos.xy:
                R22 = (b1.pos.x-b2.pos.x)**2 + (b1.pos.y-b2.pos.y)**2
                R = m.sqrt(R22)
                b1sin = (b1.pos.y-b2.pos.y)/R
                b1cos = (b1.pos.x-b2.pos.x)/R
                F = G*(b1.mass*b2.mass)/R22
                b1.dir.x -= b1cos*(F/b1.mass)
                b1.dir.y -= b1sin*(F/b1.mass)


def debugPrintPos(bl:list[Body]):
    for o in bl: print(o.pos.xy, end=" ")
    print()

def debugPrintDir(bl:list[Body]):
    for o in bl: print(o.dir.xy, end=" ")
    print()

while True:
    timer.tick(FPS)
    win.fill((0, 0, 0))
    [exit(0) for ev in event.get() if ev.type == pygame.QUIT]

    #debugPrintPos(bl)
    #debugPrintDir(bl)
    updateAll(bl)
    renderAll(bl, win)
    calcAll(bl)

    display.update()