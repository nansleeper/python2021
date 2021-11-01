from random import randint, choice
import pygame
import pygame.draw

pygame.init()

name = input()

BOARDERS =[0, 0, 400, 400] 
'game screen coordinates'
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLORS = [RED, BLUE]
screencolor = (50, 50, 50)
num_standart = 5
num_epic = 1
'number of circles'
finishtime = 700
globaltime = 0
FPS = 30
screen = pygame.display.set_mode((800, 400))
scorelist = ['123567', '63', '12467', '13467', '3456', 
    '13457', '123457', '367', '1234567', '134567', '0']
score = 0
miss_num = 0

def schet(x, y):

    '''
    (function) schet: (x , y, score)
    x, y : start coordinates (left down angle of scoreboard).
    Function draws scoreboard.
    '''

    pygame.draw.rect(screen, (255, 255, 255), (x-20 , y - 105, 80, 140))
    b = list(map(int, scorelist[score]))
    for k in b:
        if k == 1:
            pygame.draw.rect(screen, (255, 0, 0), (x + 10, y - 10, 20, 10))
        elif k == 2:
            pygame.draw.rect(screen, (255, 0, 0), (x + 0, y - 30, 10, 20))
        elif k == 3:
            pygame.draw.rect(screen, (255, 0, 0), (x + 30, y - 30, 10, 20))
        elif k == 4:
            pygame.draw.rect(screen, (255, 0, 0), (x + 10, y - 40, 20, 10))
        elif k == 5:
            pygame.draw.rect(screen, (255, 0, 0), (x + 0, y - 60, 10, 20))
        elif k == 6:
            pygame.draw.rect(screen, (255, 0, 0), (x + 30, y - 60, 10, 20))
        elif k == 7:
            pygame.draw.rect(screen, (255, 0, 0), (x + 10, y - 70, 20, 10))

def timebar():

    '''
    (function) timebar: 
    Function draws timebar.
    '''
    
    pygame.draw.rect(screen, (0, 255, 0), (440, 30, 320 * (globaltime / finishtime), 40))

class Ball:

    def __init__(self):
        self.status = 0
        self.x = randint(100, 300)
        self.y= randint(100, 300)
        self.v_x = (self.status + 1) * randint(-5, 5)
        self.v_y = (self.status + 1) * randint(-5, 5)
        self.r = randint(20, 30)
        self.color = choice(COLORS)
        self.time = 0

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
        Function destroys balls with self time > live time and creates new.
        '''

        if self.time >= 100:
            self.x = randint(100, 300)
            self.y= randint(100, 300)
            self.v_x = (self.status + 1) * randint(-5, 5)
            self.v_y = (self.status + 1) * randint(-5, 5)
            self.r = abs(self.status - 0.7) * randint(20, 50)
            if self.status == 0:
                self.color = choice(COLORS)
            self.time = 0

    def hit(self, coord):

        '''
        (function) hit: (coord)
        coord: click coordinates
        Function destroys hitted balls, creates new and pluses score.
        '''

        global score

        if (coord[0] - self.x) ** 2 + (coord[1] - self.y) ** 2 <= (self.r) ** 2:
            self.x = randint(100, 300)
            self.y= randint(100, 300)
            self.v_x = (self.status + 1) * randint(-5, 5)
            self.v_y = (self.status + 1) * randint(-5, 5)
            self.r = abs(self.status - 0.7) * randint(20, 50)
            if self.status == 0:
                self.color = choice(COLORS)
            self.time = 0
            score += self.status * 2 + 1

    def miss(self, coord):

        '''
        (function)  miss: (coord)
        coord: click coordinates
        Function calculates miss clicks.
        '''

        global score, miss_num

        if (coord[0] - self.x) ** 2 + (coord[1] - self.y) ** 2 > (self.r) ** 2:
            miss_num += 1


pool1 = []
for k in range(num_standart):
    pool1.append(Ball())

pool2 = []
for k in range(num_epic):
    pool2.append(Ball())

for k in pool2:
    k.status = 1
    print(k.status)
    k.color = YELLOW
    k.r = 0.3 * randint(20, 30)


clock = pygame.time.Clock()
finished = False
finished0 = False

schet(580, 235)
pygame.draw.rect(screen, (255, 255, 255), (420, 20, 360, 60), width = 0)

flag = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        schet(580, 235)
        if event.type == pygame.QUIT:
            finished = True
            flag = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
                flag = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for k in pool1:
                    k.miss(event.pos)
                    k.hit(event.pos)
                for k in pool2:
                    k.miss(event.pos)
                    k.hit(event.pos)
                if miss_num == num_standart + num_epic and score > 0:
                    score -= 1
                miss_num = 0
    for k in pool2:
        k.collision(BOARDERS)
        k.time += 0.5
        k.move()
        k.collups()
    for k in pool1:
        k.collision(BOARDERS)
        k.time += 1
        k.move()
        k.collups()
    pygame.display.update()
    
    globaltime +=2
    pygame.draw.rect(screen, screencolor, (0, 0, BOARDERS[2], BOARDERS[3]))
    timebar()

    if score >= 10:
        finished = True
        print('YOU WON!')
    if globaltime == finishtime:
        finished = True
        print('YOU LOSE!')

pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 400))
pygame.display.update()
if flag == False:
    result = finishtime - globaltime
else:
    result = 'Заранее окончил игру'
print(result)


import yaml
with open("./sps.yaml", "r") as f:
    loaded = yaml.load(f)

loaded['result'].append({'name': name, 'points': result})
with open("./sps.yaml", "w") as f:
    yaml.dump(loaded, f)
pygame.quit()

