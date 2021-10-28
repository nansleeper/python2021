from random import randint, choice
import pygame
from pygame.constants import MOUSEMOTION
import pygame.draw
import math

pygame.init()

screen = pygame.display.set_mode((900, 900))
BOARDER = [50, 0, 850, 850]
red = (255, 0, 0)
dark_red = (100, 0, 0)
blue = (0, 255, 0)
dark_blue = (0, 100, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
FPS = 30
COLORS = [(red, dark_red, blue, dark_blue)]


class Pushka():
    
    def __init__(self, coard):
        self.angle = 0
        self.status = False
        self.length = 10
        self.x0 = coard[0]
        self.y0 = coard[1]
        self.color = black
        self.full_length = 90
        self.load_time = 100
        self.time = 0


    def move(self):
        if self.status == False:
            self.color = black
            self.time = 0
            self.length = 10
        elif self.time < self.load_time:
            self.color = yellow
            self.time += 1
            self.length = 10 + self.time / self.load_time * self.full_length
        else:
            self.length = 10 + self.full_length
            self.color = yellow

        pygame.draw.polygon(screen, self.color, 
            [
                (self.x0, self.y0),

                (self.x0 + self.length * math.cos(self.angle),
                self.y0 - self.length * math.sin(self.angle)),
            
                (self.x0 + self.length * math.cos(self.angle) + 5 * math.sin(self.angle),
                self.y0 - self.length * math.sin(self.angle) + 5 * math.cos(self.angle)),

                (self.x0 + 5 * math.sin(self.angle),
                self.y0 + 5 * math.cos(self.angle))
            ]
        )  






class Ball:


    def __init__(self):
        self.x = randint(100, 300)
        self.y = randint(100, 300)
        self.v_x = (self.status + 1) * randint(-5, 5)
        self.v_y = (self.status + 1) * randint(-5, 5)
        self.color = choice(COLORS)
        self.time = 0
        self.r = randint(10, 30)
        self.status = 0

    def collision(self, BOARDER):

        '''
        (function) collision: (boarders)
        boarders: game pole coordinates
        Function calculates collisions with boarders and changes moving direction.
        '''

        if (
            self.x + self.v_x + self.r >= BOARDER[2] or
            self.x + self.v_x - self.r <= BOARDER[0]
        ):
            self.v_x = -randint(0, 250) * self.v_x / 100
    
        if (
            self.y + self.v_y - self.r <= BOARDER[1] or
            self.y + self.v_y + self.r >= BOARDER[3]
        ):
            self.v_y = -randint(0, 250) * self.v_y / 100


    def move(self):

        '''
        (function) move: 
        Function calculates (x, y) coordinates and draws circles.
        '''

        self.x += self.v_x
        self.y += self.v_y
        pygame.draw.circle(screen, self.color,(self.x, self.y), self.r, width = self.status)



    def collups(self):

        '''
        (function) collups:
        Function destroys balls with self time > live time.
        '''

        if self.time > self.live_time:
            self.status
            
pushka = Pushka((60, 840))

clock = pygame.time.Clock()
finished = False

pool = []

while not finished:
    clock.tick(FPS)
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 900, 900))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pushka.status = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and pushka.status == True:
                pushka.status = False
                power = pushka.time
                angle = pushka.angle
                pool.append(Ball)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
        if event.type == MOUSEMOTION:
            if event.pos[0] != 0:
                pushka.angle = math.atan((pushka.y0 - event.pos[1])/ (event.pos[0] - pushka.x0))
    pushka.move()
    for i in pool:
        if i.time == 22:
            continue


    pygame.display.update()