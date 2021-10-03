import pygame
import turtle
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 500))

pygame.draw.rect(screen, (255, 160, 110), (0, 0, 1000, 500))


def ell(x0, y0, s, angle): ## (x cord, y cord, size, angle)
    a = []
    for k in range(0, 100):
        pygame.draw.circle(screen, (0, 100, 0), (x0 + s * 20 * math.sin(angle / 180 * math.pi) * k / 100, y0 + s * 20 * math.cos(angle / 180 * math.pi) * k / 100), 2 * s * (1 + 1 * (k / 100) ** 0.8), width=0)
    for k in range(0, 100):
        pygame.draw.circle(screen, (0, 100, 0), (x0 + s * 20 * math.sin(angle / 180 * math.pi) * (1 + k / 100), y0 + s * 20 * math.cos(angle / 180 * math.pi) * (1 + k / 100)), 2* s * (2 - (k / 100) ** 1.25), width=0)


def stick(x, y, n, s, angle): ## (1st cord, 2nd cord, num_elip, angle)
    a = []
    b = 1
    if x[0] < y[0]:
        b = -1
    if angle < 0:
        b = b * (-1)
    for k in range(1, 101):
        a.append((x[0] + k / 100 * (y[0] - x[0]), x[1] + ((k / 100) ** (2 ** b)) * (y[1] - x[1])))
    pygame.draw.lines(screen, (0, 100, 0), False, a, width=2)
    for k in range(0, n ):
        ell(x[0] + (y[0] - x[0]) * (0.5 * abs((b - 1)) / 2 + k / n / 2), x[1] + (y[1] - x[1]) * (0.5 * abs((b - 1)) / 2 + k / n / 2), s, angle)
        
pygame.draw.rect(screen, (0, 100, 0), (200, 315, 15, 70))
pygame.draw.rect(screen, (0, 100, 0), (200, 225, 15, 80))
pygame.draw.polygon(screen, (0, 100, 0), [(210, 215), (200, 210), (205, 160), (215, 165)])
pygame.draw.polygon(screen, (0, 100, 0), [(215, 155), (210, 152), (217, 80), (222, 83)])
stick([135, 200], [195, 230], 3, 1, -30)
stick([320, 100], [220, 180], 5, 1, 30)
stick([135, 100], [195, 150], 5, 1, -30)
stick([270, 200], [220, 230], 3, 1, 30)
        
pygame.draw.rect(screen, (0, 100, 0), (400, 315, 15, 90))
pygame.draw.rect(screen, (0, 100, 0), (400, 225, 15, 80))
pygame.draw.polygon(screen, (0, 100, 0), [(410, 215), (400, 210), (405, 160), (415, 165)])
pygame.draw.polygon(screen, (0, 100, 0), [(415, 155), (410, 152), (417, 80), (422, 83)])
stick([335, 200], [395, 230], 3, 1, -30)
stick([520, 100], [420, 180], 5, 1, 30)
stick([335, 100], [395, 150], 5, 1, -30)
stick([470, 200], [420, 230], 3, 1, 30)

pygame.draw.rect(screen, (0, 100, 0), (600, 295, 25, 90))
pygame.draw.rect(screen, (0, 100, 0), (600, 205, 25, 80))
pygame.draw.polygon(screen, (0, 100, 0), [(610, 195), (600, 190), (610, 140), (620, 145)])
pygame.draw.polygon(screen, (0, 100, 0), [(615, 135), (610, 132), (627, 50), (632, 53)])
stick([455, 150], [595, 230], 3, 1.5, -30)
stick([780, 50], [620, 160], 5, 1.5, 30)
stick([435, 30], [595, 110], 5, 1.5, -30)
stick([770, 150], [640, 210], 3, 1.5, 30)

pygame.draw.rect(screen, (0, 100, 0), (800, 315, 15, 90))
pygame.draw.rect(screen, (0, 100, 0), (800, 225, 15, 80))
pygame.draw.polygon(screen, (0, 100, 0), [(810, 215), (800, 210), (805, 160), (815, 165)])
pygame.draw.polygon(screen, (0, 100, 0), [(815, 155), (810, 152), (817, 80), (822, 83)])
stick([735, 200], [795, 230], 3, 1, -30)
stick([920, 100], [820, 180], 5, 1, 30)
stick([735, 100], [795, 150], 5, 1, -30)
stick([870, 200], [820, 230], 3, 1, 30)

pygame.draw.ellipse(screen, (255, 255, 255), (650, 250, 250, 170))
pygame.draw.ellipse(screen, (0, 0, 0), (840, 330, 50, 120))
pygame.draw.circle(screen, (0, 0, 0), (850, 430), 25)
pygame.draw.polygon(screen, (0, 0, 0), [(845, 350), (860, 440), (825, 430) ])



pygame.draw.polygon(screen, (0, 0, 0), [(820, 250),(820, 400), (780, 430), (750, 457), (735, 400), (760, 370)])
pygame.draw.circle(screen, (0, 0, 0), (740, 430), 30)

pygame.draw.ellipse(screen, (0, 0, 0), (640, 270, 80, 180))

pygame.draw.ellipse(screen, (255, 255, 255), (630, 220, 160, 180))
pygame.draw.polygon(screen, (255, 255, 255), [(790, 310), (790, 350), (770, 380), (710, 400)] )

pygame.draw.polygon(screen, (0, 0, 0), [(670, 240), (630, 275), (620, 250), (650, 230)])
pygame.draw.ellipse(screen, (0, 0, 0), (750, 230, 40, 70))
pygame.draw.ellipse(screen, (0, 0, 0), (650, 365, 40, 25))
pygame.draw.circle(screen, (0, 0, 0), (660, 330), 20)
pygame.draw.circle(screen, (0, 0, 0), (710, 330), 20)



####

pygame.draw.ellipse(screen, (255, 255, 255), (510, 400, 100, 70))
pygame.draw.ellipse(screen, (0, 0, 0), (590, 430, 20, 50))
pygame.draw.circle(screen, (0, 0, 0), (595, 475), 10)

pygame.draw.polygon(screen, (0, 0, 0), [(560, 410),(560, 480), (540, 490), (530, 470)])
pygame.draw.circle(screen, (0, 0, 0), (545, 475), 15)

pygame.draw.ellipse(screen, (0, 0, 0), (500, 420, 25, 70))

pygame.draw.ellipse(screen, (255, 255, 255), (485, 390, 70, 70))

pygame.draw.polygon(screen, (0, 0, 0), [(510, 405), (485, 415), (490, 400), (500, 390)])
pygame.draw.ellipse(screen, (0, 0, 0), (540, 400, 15, 30))
pygame.draw.ellipse(screen, (0, 0, 0), (500, 450, 20, 10))
pygame.draw.circle(screen, (0, 0, 0), (500, 440), 10)
pygame.draw.circle(screen, (0, 0, 0), (520, 440), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()