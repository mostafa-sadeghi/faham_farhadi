# import pygame
# import random
# pygame.init()

# screen = pygame.display.set_mode((700, 500))
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# screen.fill(WHITE)
# rect_x = 0
# rect_y = 0
# rect_change_x = 1
# rect_change_y = 1

# snow_list = []

# for i in range(50):
#     x = random.randrange(0, 400)
#     y = random.randrange(0, 400)
#     # pygame.draw.circle(screen, RED, [x, y], 2)
#     snow_list.append([x, y])

# pygame.display.flip()


# def draw_tree():
#     pygame.draw.rect(screen, BLACK, [60, 400, 30, 45])
#     pygame.draw.polygon(screen, GREEN, [[150, 400], [75, 250], [0, 400]])
#     pygame.draw.polygon(screen, GREEN, [[140, 350], [75, 230], [10, 350]])
#     pygame.display.flip()


# draw_tree()
# clock = pygame.time.Clock()
# done = True
# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = False

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

    # for i in range(len(snow_list)):
    #     pygame.draw.circle(screen, WHITE, snow_list[i], 2)
    #     snow_list[i][1] += 1

    #     if snow_list[i][1] > 400:
    #         y = random.randrange(-50,-10)
    #         snow_list[i][1] = y
    #         x = random.randrange(0,400)
    #         snow_list[i][0] = x

    # pygame.display.flip()
    # clock.tick(20)



def sum_two_numbers(a,b):
    result = a + b
    return result


x = sum_two_numbers(2,3)
print(x)


# تابع برای تفریق، ضرب و تقسیم