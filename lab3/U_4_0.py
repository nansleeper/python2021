import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


pygame.draw.polygon(screen, (100, 100, 100), [(0, 0), (400, 0), (400, 400), (0, 400)])
pygame.draw.circle(screen, (255, 255, 0), (200, 200), 100)
pygame.draw.circle(screen, (255, 0, 0), (240, 180), 20)
pygame.draw.circle(screen, (255, 0, 0), (160, 180), 25)
pygame.draw.circle(screen, (0, 0, 0), (240, 180), 10)
pygame.draw.circle(screen, (0, 0, 0), (160, 180), 10)
pygame.draw.polygon(screen, (0, 0, 0), [(190, 160), (90, 110), (95, 100 ), (195, 150)])
pygame.draw.polygon(screen, (0, 0, 0), [(210, 170), (310, 120), (305, 110 ), (205, 160)])
pygame.draw.rect(screen, (0, 0, 0), (150, 250, 100, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
