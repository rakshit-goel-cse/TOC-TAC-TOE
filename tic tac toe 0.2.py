import pygame,sys
from pygame.locals import *



#1 initialization
i=1
j=1

p1=True
pygame.init()
screen=pygame.display.set_mode((240,240))
pygame.display.set_caption("tic tac toe")


#2 data setting
body=pygame.image.load("data/body.png")
body=pygame.transform.scale(body,(240,240))
cross=pygame.image.load("data/cross.png")
cross=pygame.transform.scale(cross,(60,60))
zero=pygame.image.load("data/circle.png")
zero=pygame.transform.scale(zero,(60,60))
win1=pygame.image.load("data/win1.png")
win1=pygame.transform.scale(win1,(240,240))
win2=pygame.image.load("data/win2.png")
win2=pygame.transform.scale(win2,(240,240))
drawim=pygame.image.load("data/draw.png")
drawim=pygame.transform.scale(drawim,(240,240))
select=pygame.image.load("data/select.png")
select=pygame.transform.scale(select,(80,80))
unselect=pygame.image.load("data/unselect.png")
unselect=pygame.transform.scale(unselect,(80,80))

victory=pygame.mixer.Sound("data/victory.wav")
draw=pygame.mixer.Sound('data/draw.wav')
click=pygame.mixer.Sound('data/click.wav')

pos=((0,0,86,165),(0,0,85,155)) # zero and i for row , 1 and j for column

screen.fill(1)




#3 Functions

def ex():

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #sys.exit()
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN :
                if event.key==pygame.K_ESCAPE:
                    #start()
                    #sys.exit()
                    pygame.quit()
                    quit()
                if event.key==pygame.K_KP_ENTER or event.key==pygame.K_RETURN :
                    start()
            if event.type==pygame.MOUSEBUTTONDOWN:
                start()

def win():
    global p1
    pygame.mixer.Sound.play(victory)
    pygame.mixer.music.stop()

    if(p1):
        screen.blit(win1,(0,0))
    else:
        screen.blit(win2,(0,0))
    pygame.display.update()
    ex()


def drawfu():
    screen.blit(drawim,(0,0))
    pygame.display.update()
    pygame.mixer.Sound.play(draw)
    pygame.mixer.music.stop()
    ex()

def same():
    global i,j
    if(game[i][j]==0):
        return (True)
    else:
        
        return False

def check():
    for i in range(1,4):
        if(game[i][1]==game[i][2]==game[i][3]!=0):
            win()

    for j in range(1,4):
        if (game[1][j] == game[2][j]== game[3][j]!=0):
            win()
    if (game[1][1] == game[2][2] == game[3][3] !=0):
        win()
    if(game[1][3]==game[2][2]==game[3][1]!=0):
        win()
    for i in range(1,4):
        for j in range(1,4):
            if(game[i][j]==0):
                return()
    drawfu()

def player():
    global p1,i,j
    #p1
    if(p1 and same()):
        game[i][j]=1
        pygame.mixer.Sound.play(click)
        screen.blit(cross,(pos[0][i],pos[1][j]))
        pygame.display.update()
        check()
        p1=False


    #p2
    elif(not(p1) and same() ):
        game[i][j]=2
        pygame.mixer.Sound.play(click)
        screen.blit(zero,(pos[0][i],pos[1][j]))
        pygame.display.update()
        check()
        p1=True





def index(p):
    global i,j
    if(p[0]<80):
        i=1
    elif(p[0]<150):
        i=2
    elif(p[0]>150):
        i=3

    if (p[1] < 80):
        j = 1
    elif (p[1] < 152):
        j = 2
    elif (p[1] > 152):
        j = 3


#4

def start():
    pygame.mixer.Sound.stop(victory)
    pygame.mixer.Sound.stop(draw)
    pygame.mixer.Sound.play(click)
    pygame.mixer.music.load('data/back.mp3')
    pygame.mixer.music.play(-1)
    x,y=0,0
    global game
    screen.blit(body, (0, 0))
    pygame.display.update()
    game = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
		
            if event.type == pygame.MOUSEBUTTONDOWN:
                player()
                #pygame.mixer.Sound.play(click)

        position = pygame.mouse.get_pos()

        index(position)
        screen.blit(unselect,(pos[0][x],pos[1][y]))
        screen.blit(select, (pos[0][i], pos[1][j]))
        pygame.display.update()
        x,y=i,j

start()

