import pygame
import sys

pygame.init()

size = width, height = 800, 700
speed = [-1, 1]
rpg = (255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('弹弹乐')
png = pygame.image.load('D:/请把我放到D盘根目录.jpg')
position = png.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    position = position.move(speed)
    if position.left < 0 or position.right > width:
        png = pygame.transform.flip(png, True, False)
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    screen.fill(rpg)
    screen.blit(png, position)
    pygame.display.flip()
    pygame.time.delay(10)