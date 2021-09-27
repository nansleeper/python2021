import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 500))

pygame.draw.rect(screen, (255, 160, 110), (0, 0, 1000, 500))

pygame.draw.rect(screen, (0, 100, 0), (200, 315, 15, 60))
pygame.draw.rect(screen, (0, 100, 0), (200, 235, 15, 70))
pygame.draw.polygon(screen, (0, 100, 0), [(210, 225), (200, 220), (205, 160), (215, 165)])
pygame.draw.polygon(screen, (0, 100, 0), [(215, 155), (210, 152), (217, 100), (222, 103)])

pygame.draw.rect(screen, (0, 100, 0), (400, 315, 15, 90))
pygame.draw.rect(screen, (0, 100, 0), (400, 225, 15, 80))
pygame.draw.polygon(screen, (0, 100, 0), [(410, 215), (400, 210), (405, 160), (415, 165)])
pygame.draw.polygon(screen, (0, 100, 0), [(415, 155), (410, 152), (417, 80), (422, 83)])

pygame.draw.rect(screen, (0, 100, 0), (600, 295, 25, 90))
pygame.draw.rect(screen, (0, 100, 0), (600, 205, 25, 80))
pygame.draw.polygon(screen, (0, 100, 0), [(610, 195), (600, 190), (610, 140), (620, 145)])
pygame.draw.polygon(screen, (0, 100, 0), [(615, 135), (610, 132), (627, 50), (632, 53)])

pygame.draw.rect(screen, (0, 100, 0), (800, 285, 15, 90))
pygame.draw.rect(screen, (0, 100, 0), (800, 195, 15, 80))
pygame.draw.polygon(screen, (0, 100, 0), [(810, 185), (800, 180), (805, 130), (815, 135)])
pygame.draw.polygon(pygame.transform.rotozoom(screen, 10, 1), (0, 100, 0), [(815, 125), (810, 122), (817, 30), (822, 33)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()