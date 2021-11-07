from codecs import xmlcharrefreplace_errors
import math
from random import choice, randint
import sys

import pygame
pygame.font.init()

letter = pygame.display.set_mode((600,50))
letter.fill((255, 255, 255))
localflag = False

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
g = 1

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x = 40, y = 450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = int(x)
        self.y = int(y)
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.flag = True
        self.time = 0

    def move(self):

        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        global g
        if self.x + self.vx <= 0 or self.x + self.vx >= 800:
            self.vx = - 0.5 * self.vx
            self.vy = 0.5 * self.vy
        if self.y + self.vy <= 0 or self.y + self.vy >= 600:
            self.vy = - 0.5 * self.vy
            self.vx = 0.5 * self.vx
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.flag:
            self.vy += g
        if self.y >= 600 - self.r and abs(self.vy) <= 2:
            self.y = 600 - self.r
            self.vy = 0
            self.vx = 0
            self.flag = False
        self.time += 5
        if self.time > 600:
            self.color = WHITE


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2:
            return True


class Gun:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.polygon(self.screen, self.color,
            (
                (
                    self.x,
                    self.y
                ),
                (
                    self.x + self.f2_power * math.cos(self.an),
                    self.y - self.f2_power * math.sin(self.an),  
                ),
                (
                    self.x + self.f2_power * math.cos(self.an) - 10 * math.sin(self.an),
                    self.y - self.f2_power * math.sin(self.an) - 10 * math.cos(self.an)
                ),
                (
                    self.x - 10 * math.sin(self.an),
                    self.y - 10 * math.cos(self.an)
                )
            )
        )


    def fire2_start(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        if event.type == pygame.MOUSEBUTTONUP:
            global balls, bullet
            bullet += 1
            new_ball = Ball(self.screen)
            new_ball.r += 5
            self.an = math.atan2((- event.pos[1] + new_ball.y), (event.pos[0] - new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            balls.append(new_ball)
            self.f2_on = 0
            self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[1] - self.x != 0:
                self.an = math.atan((self.y - event.pos[1]) / (event.pos[0] - self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target():
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()

    def __init__(self, screen: pygame.Surface):
        self.points = 0
        self.x = randint(600, 750)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
        self.live = 1
        self.screen = screen
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)

        

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(600, 750)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
        self.live = 1
        self.color = RED

    def draw(self):
        if self.live == 1:
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )

class Target1(Target):

    def __init__(self, screen: pygame.Surface):
        self.points = 0
        self.x = randint(600, 750)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
        self.live = 1
        self.screen = screen
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)

    def velo(self):
        self.vx = randint( -10, 10)
        self.vy = randint( -10, 10)

    def move(self):
        if self.x + self.vx <= 0 or self.x + self.vx >= 800:
            self.vx = - 0.5 * self.vx
        if self.y + self.vy <= 0 or self.y + self.vy >= 600:
            self.vy = - 0.5 * self.vy
        self.x = self.x + self.vx
        self.y = self.y + self.vy
    
    




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen, 50, 450)
target1 = Target(screen)
target2 = Target1(screen)
finished = False
Targets = [target1, target2]

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.velo()
    target2.move()
    target2.draw()
    if localflag == True:
        text = result.render(f'Вы уничтожили цели за {score} выстрелов', True, 10)
        screen.blit(text, (300, 300))
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
            localflag = False
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        for target in Targets:
            if b.hittest(target) and target.live:
                target.live = 0
                statusfinish = 0
                for k in Targets:
                    statusfinish += k.live
                if statusfinish == 0:
                    target.new_target()
                    score = len(balls)
                    balls = []
                    result = pygame.font.Font(None, 16)
                    localflag = True
                    for k in Targets:
                        k.live 
                        k.new_target()

        


    gun.power_up()

pygame.quit()
