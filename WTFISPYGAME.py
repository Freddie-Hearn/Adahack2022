import pygame

def initialize(screen, x, y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x, y + 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y + 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 80, y, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x, y + 80, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y + 80, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 80, y + 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 80, y + 80, 40, 40), 3)

def paint(matrix):
    screen = pygame.display.set_mode((400, 520))
    screen.fill((155, 155, 155))
    initialize(screen, 160, 160)
    initialize(screen, 160, 280)
    initialize(screen, 280, 160)
    initialize(screen, 160, 40)
    initialize(screen, 40, 160)
    initialize(screen, 160, 400)
    color_update(matrix, screen)
    pygame.display.update()

blue = 114, 187, 255
white = 230, 230, 255
yellow = 175, 232, 65
red = 178, 71, 61
orange = 255, 129, 66
green = 0, 203, 40

colors = [red, yellow, blue, white, green, orange]

def color_side(color, x, y, z, screen):
    pygame.draw.rect(screen, colors[color[0]], (x+80,y, 34, 34), 0)
    pygame.draw.rect(screen, colors[color[1]], (x+80,y+40, 34, 34), 0)
    pygame.draw.rect(screen, colors[color[2]], (x+80,y+80, 34, 34), 0)
    pygame.draw.rect(screen, colors[color[3]], (x+40,y, 34, 34), 0)
    pygame.draw.rect(screen, colors[color[4]], (x+40,y+40, 34, 34), 0)
    pygame.draw.rect(screen, colors[color[5]], (x+40,y+80, 34, 34), 0)
    pygame.draw.rect(screen, colors[color[6]], (x,y, 34, 34), 0)
    pygame.draw.rect(screen, colors[color[7]], (x,y+40, 34, 34), 0)
    pygame.draw.rect(screen, colors[color[8]], (x,y+80, 34, 34), 0)

def color_update(matrix, screen):
    color_side(matrix[2], 163, 163, 2, screen)
    color_side(matrix[3], 163, 283, 3, screen)
    color_side(matrix[0], 283, 163, 0, screen)
    color_side(matrix[1], 163, 43, 1, screen)
    color_side(matrix[5], 43, 163, 5, screen)
    color_side(matrix[4], 163, 403, 4, screen)
#paint([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5]])
# 0 is red, 1 is yellow (but really its light green), 2 is blue, 3 is white,4 is (dark) green, 5 is orange
#colours = "rywwybyroyoboooobrrgyybrwbggyowrgwybgggwgbwgbbrrwwryoo"
def translate(colours):
    translation = ["r", "y", "b", "w", "g", "o"]
    codes=[]
    for i in range(0,54):
        if i%9==0:
            u=[]
            codes.append(u)
        u.append(translation.index(colours[i]))
    return codes
#paint(translate(colours))
#print(translation.index("o")) prints 5 and so on.
paint(translate(input("Enter the code for the rubik's cube here: ")))
input()