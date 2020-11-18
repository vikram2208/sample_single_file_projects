import pygame, random, math
# import winsound

from pygame.locals import *

pygame.init()


# define RandomExcept
def RandomExcept(Range_x, Range_y, A):
    x = random.randint(Range_x[0], Range_x[1])
    y = random.randint(Range_y[0], Range_y[1])
    for (i, j) in A:
        while x > i - Snake_b and x < i + Snake_b and y > j - Snake_b and y < j + Snake_b:
            x = random.randint(Range[0], Range[1])
            y = random.randint(Range[0], Range[1])
    return x, y


def Quit():
    pygame.quit()
    quit()


# game over function
def GameOver():
    run = False
    msg = FONT_set.render('GAME OVER', True, RED, BLACK)
    # create a text surface
    textRect = msg.get_rect()
    # set the center of the rectangular object.
    textRect.center = (Display_Actual[0] // 2, Display_Actual[1] // 2)
    win.fill(BLACK)
    win.blit(msg, textRect)
    pygame.display.update()
    pygame.time.delay(3000)
    Quit()


def score(Score):
    fontx = pygame.font.Font('freesansbold.ttf', 30)
    msg = fontx.render('SCORE ' + str(Score), True, WHITE, BLACK)
    textRect = msg.get_rect()
    textRect.center = ((Display_Actual[0] + Display_s[0]) // 2, 100)
    win.blit(msg, textRect)
    pygame.display.update()


# fonts defined
FONT_set = pygame.font.Font('freesansbold.ttf', 80)
# colors defined
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# Display (width x height)
Display_Actual = (900, 700)
Display_s = (700, 700)
win = pygame.display.set_mode(Display_Actual)
pygame.display.set_caption("GREEN SNAKE")
x = 0
y = 0
A = [[0, 0]]
Food_x = 250
Food_y = 250
Food_size = 15
Food_count = 0
Food_eaten = False
Special_Food = False
Snake_b = 15
Snake_l = Snake_b
Score = 0
width = 15
height = 15
vel = 5
run = True
L = False
R = L
U = L
D = L
while run:
    pygame.time.delay(33)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit()
            # setting self eating to death
    dist = Snake_l
    death = 0
    for v in range(5, len(A)):
        dist = math.sqrt((A[0][0] - A[v][0]) ** 2 + (A[0][1] - A[v][1]) ** 2)
        if dist < Snake_l:
            death = 1
            GameOver()
    if death == 1:
        GameOver()
        # Snake growth and movement and body memory
    if Food_eaten == True:
        A.append([0, 0])
        Food_eaten = False
    if len(A) > 1:
        B = A
        for i in range(len(A) - 1):
            B[len(A) - 1 - i] = A[len(A) - 2 - i]
        A = B
        # providing control over snake and setting boundary conditon to "KILL"
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and R == False:
        L = True
        U = False
        D = False
    if keys[pygame.K_RIGHT] and L == False:
        R = True
        U = False
        D = False
    if keys[pygame.K_UP] and D == False:
        L = False
        R = False
        U = True
    if keys[pygame.K_DOWN] and U == False:
        L = False
        R = False
        D = True
    if L == True:
        if not x - vel >= 0:
            GameOver()
        x -= vel
    if R == True:
        if not x + vel + width <= Display_s[0]:
            GameOver()
        x += vel
    if U == True:
        if not y - vel >= 0:
            GameOver()
        y -= vel
    if D == True:
        if not y + vel + height <= Display_s[1]:
            GameOver()
        y += vel
    A[0] = [x, y]
    # eating food and new food creation
    m = Food_x - x
    n = Food_y - y
    Dist_F2S = math.sqrt(m * m + n * n)
    if Dist_F2S <= Food_size:
        if Special_Food == True:
            Score += 5
            if vel < 10:
                vel += 1
        else:
            Score += 1
        Special_Food = False
        if Food_count > 4 and Food_count % 5 == 0:
            Special_Food = True
        Range_x = (Food_size, Display_s[0] - Food_size)
        Range_y = (Food_size, Display_s[1] - Food_size)
        Food_x, Food_y = RandomExcept(Range_x, Range_y, A)
        # winsound.PlaySound("apple.wav", winsound.SND_ASYNC)
        Food_eaten = True
        Food_count += 1
        # providing game picture at 30 fps
    win.fill(BLACK)
    for i in range(len(A)):
        pygame.draw.rect(win, GREEN, (A[i][0], A[i][1], width, height))
    if Special_Food == True:
        pygame.draw.rect(win, BLUE, (Food_x - 2, Food_y - 2, Food_size + 4, Food_size + 4))
    pygame.draw.rect(win, RED, (Food_x, Food_y, Food_size, Food_size))
    pygame.draw.rect(win, WHITE, (Display_s[0] + 1, 0, 2, Display_s[1] + 2))
    pygame.display.flip()
    score(Score)
    # winsound.PlaySound("dead.wav", winsound.SND_ASYNC)
