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
    pygame.draw.rect(screen, (255, 255, 255), (x, y + 120, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y + 120, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 80, y + 120, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 120, y , 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 120, y + 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 120, y + 80, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 120, y + 120, 40, 40), 3)

def paint(matrix):
    screen = pygame.display.set_mode((560, 720))
    screen.fill((155, 155, 155))
    initialize(screen, 200, 200)
    initialize(screen, 200, 360)
    initialize(screen, 360, 200)
    initialize(screen, 200, 40)
    initialize(screen, 40, 200)
    initialize(screen, 200, 520)
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
    a=160
    for i in range(0,16):
        if i%4==0:
            a=a-40
            b=0
        else:
            b=b+40
        pygame.draw.rect(screen, colors[color[i]], (x+a, y+b, 34, 34), 0)

def color_update(matrix, screen):
    color_side(matrix[2], 203, 203, 2, screen)
    color_side(matrix[3], 203, 363, 3, screen)
    color_side(matrix[0], 363, 203, 0, screen)
    color_side(matrix[1], 203, 43, 1, screen)
    color_side(matrix[5], 43, 203, 5, screen)
    color_side(matrix[4], 203, 523, 4, screen)
#paint([[0]*16, [1]*16, [2]*16, [3]*16, [4]*16, [5]*16])
# 0 is red, 1 is yellow (but really its light green), 2 is blue, 3 is white,4 is (dark) green, 5 is orange
colours = "rywwybyroyoboooobrrgyybrwbggyowrgwybgggwgbwgbbrrwwryoorywwybyroyoboooobrrgyybrwbggyowrgwybgggwgb"
def translate(colours):
    translation = ["r", "y", "b", "w", "g", "o"]
    codes=[]
    for i in range(0,16*6):
        if i%16==0:
            u=[]
            codes.append(u)
        u.append(translation.index(colours[i]))
    return codes
paint(translate(colours))
#print(translation.index("o")) prints 5 and so on.
#paint(translate(input("Enter the code for the rubik's cube here: ")))
input()