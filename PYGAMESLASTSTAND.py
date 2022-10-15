import pygame
import random





def initialize(screen, x, y,n):
    a=40*n
    for i in range(0,n*n):
        if i%n==0:
            a=a-40
            b=0
        else:
            b=b+40
        pygame.draw.rect(screen,(255,255,255), (x+a, y+b, 34, 34), 3)

def paint(matrix,n):
    screen = pygame.display.set_mode((n*120 + 80, n*160 + 80))
    screen.fill((155, 155, 155))
    initialize(screen, 40*(n+1), 40*(n+1),n)
    initialize(screen, 40*(n+1), 40*(2*n+1),n)
    initialize(screen, 40*(2*n+1), 40*(n+1),n)
    initialize(screen, 40*(n+1), 40,n)
    initialize(screen, 40, 40*(n+1),n)
    initialize(screen, 40*(n+1), 40*(3*n+1),n)
    color_update(matrix, screen,n)
    pygame.display.update()

blue = 114, 187, 255
white = 230, 230, 255
yellow = 175, 232, 65
red = 178, 71, 61
orange = 255, 129, 66
green = 0, 203, 40

colors = [red, yellow, blue, white, green, orange]

def color_side(color, x, y, screen,n):
    a=40*n
    for i in range(0,(n*n)):
        if i%n==0:
            a=a-40
            b=0
        else:
            b=b+40
        pygame.draw.rect(screen, colors[color[i]], (x+a, y+b, 34, 34), 0)

def color_update(matrix, screen,n):
    color_side(matrix[2], 40*(n+1)+3, 40*(n+1)+3, screen,n)
    color_side(matrix[3], 40*(n+1)+3, 40*(2*n+1)+3, screen,n)
    color_side(matrix[0], 40*(2*n+1)+3, 40*(n+1)+3, screen,n)
    color_side(matrix[1], 40*(n+1)+3, 43, screen,n)
    color_side(matrix[5], 43, 40*(n+1)+3, screen,n)
    color_side(matrix[4], 40*(n+1)+3, 40*(3*n+1)+3, screen,n)
#paint([[0]*(n*n), [1]*(n*n), [2]*(n*n), [3]*(n*n), [4]*(n*n), [5]*(n*n)],n)
# 0 is red, 1 is yellow (but really its light green), 2 is blue, 3 is white,4 is (dark) green, 5 is orange
def translate(colours,n):
    translation = ["r", "y", "b", "w", "g", "o"]
    codes=[]
    for i in range(0,n*6):
        if i%(n*n)==0:
            u=[]
            codes.append(u)
        u.append(translation.index(colours[i]))
    return codes
#paint(translate(colours),n)

n=int(input("Enter the size of the rubiks cube as an integer (e.g. 3): "))


#Attempt to randomise cube.
codes=[]
for i in range(0,(n*n)*6):
    if i % (n * n) == 0:
        u = []
        codes.append(u)
    u.append(random.randint(0,5))

#print(translation.index("o")) prints 5 and so on.
#paint(translate(input("Enter the code for the rubik's cube here: ")))


#paint([[0]*(n*n), [1]*(n*n), [2]*(n*n), [3]*(n*n), [4]*(n*n), [5]*(n*n)],n)
paint(codes,n)

#paint(codes,n) generates random rubiks cube
#paint ([0]*n*n... gives the filled in squares.

#This input just measn it goes away only on your next input.
input()