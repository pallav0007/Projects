import pygame as py
import random
import math
py.init()
screen=py.display.set_mode((800,600))
py.display.set_caption("falling blocks")
icon=py.image.load(r"images\bullet.png")
py.display.set_icon(icon)
background=py.image.load("images\honey.jpg")
running=True
score_var=0
font=py.font.Font('freesansbold.ttf',32)
overfont=py.font.Font('freesansbold.ttf',64)
playerimg=py.image.load("images\shin.png")
enemyimg=py.image.load("images\enemy45.png")
playerX=450
playerY=500
enemy=[]
enemyX=[]
enemyY=[]
change=0.5
#x=int(input("enemy:"))
enemyX=random.sample(range(20,650),9)
enemyY=random.sample(range(80,200),9)
setting=[]

for i in range(0,9):
    new=[enemyimg,enemyX[i],enemyY[i]]
    enemy.append(new)



def player(x,y):
    screen.blit(playerimg,(x,y))

def enemydisplay(lis):
    for i in lis:
        screen.blit(i[0],(i[1],i[2]))
def enemymove(lis,score_var):
    for i in lis:
        if i[2]>550:
            i[2]=random.randint(30,200)
            i[1]=random.randint(8,550)
            score_var+=1

        i[2]+=change

def show_score(x,y,score_var):
    score=font.render(("score:"+str(score_var)),True,(0,0,0))
    screen.blit(score,(x,y))

def collision(a,b,c,d):
    distance = math.sqrt(math.pow((a-c), 2) + math.pow((b-d), 2))
    if distance<20:
        return True
def game_over():
    overtext = overfont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(overtext, (200,250))


while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    #screen.blit(enemyimg,(400,100))


    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
        if event.type==py.KEYDOWN:
            if event.key==py.K_LEFT:
                playerX-=10

            if event.key==py.K_RIGHT:
                playerX+=10

        if event.type==py.KEYUP:
            if event.key==py.K_LEFT:
                playerX-=10

            if event.key==py.K_RIGHT:
                playerX+=10

    if playerX<=8:
        playerX=8
    if playerX>700:
        playerX=700
    for i in range(0,len(enemy)):
        if collision(playerX,playerY,enemy[i][1],enemy[i][2]):
            game_over()
            running=False
    player(playerX, playerY)
    enemymove(enemy,score_var)
    enemydisplay(enemy)
    show_score(0, 0,score_var)
    py.display.update()