import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700, 500))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
screen.fill(BLACK)
rect_x = 0
rect_y = 0
rect_change_x = 1
rect_change_y = 1

snow_list = []

for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    # pygame.draw.circle(screen, RED, [x, y], 2)
    snow_list.append([x, y])

# pygame.display.flip()


clock = pygame.time.Clock()
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    # pygame.draw.rect(screen, BLACK, [rect_x, rect_y, 50, 50])
    # rect_x += rect_change_x
    # rect_y += rect_change_y
    # if rect_y > 450 or rect_y < 0:
    #     rect_change_y = -1 * rect_change_y
    # if rect_x > 650 or rect_x < 0:
    #     rect_change_x = rect_change_x * -1

    # pygame.draw.rect(screen, BLACK, [rect_x, rect_y, 50, 50])
    # pygame.draw.rect(screen, RED, [rect_x+10, rect_y+10, 30, 30])
    # for i in range(50):
    #     x = random.randrange(0, 400)
    #     y = random.randrange(0, 400)
    #     pygame.draw.circle(screen, RED, [x, y], 2)

    # pygame.display.flip()

    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1

        if snow_list[i][1] > 400:
            y = random.randrange(-50,-10)
            snow_list[i][1] = y
            x = random.randrange(0,400)
            snow_list[i][0] = x

    pygame.display.flip()
    clock.tick(20)
