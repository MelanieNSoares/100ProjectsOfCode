from pygame import *

screenwidth = 900
screenhight = 600
screen = display.set_mode((screenwidth,screenhight))

font.init()
calibriBold35 = font.SysFont("Calibri Bold", 35)

#colors
white = (255,255,255)
BGCOLOR =  (0,220,160)
BLUE = (50,100,230)
RED = (230,50,100)

p1Y = 250
p2Y = 250

paddleWidth = 30
paddleHeight = 100

p1Points, p2Points = 0,0
ballX = 450
ballY = 300
ballDx = 4
ballDy = 4

running = True
myClock = time.Clock()
#main logic for game
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    p1Paddle = Rect(50,p1Y,paddleWidth,paddleHeight)
    p2Paddle = Rect(850,p2Y,paddleWidth,paddleHeight)
    ball = Rect(ballX,ballY,10,10)

    keys = key.get_pressed()
    if(keys[K_w] and p1Y > 0):
        p1Y -= 5
    elif(keys[K_s] and p1Y+paddleHeight < screenhight):
        p1Y += 5

    if(keys[K_UP] and p2Y > 0):
        p2Y -= 5
    elif(keys[K_DOWN] and p2Y+paddleHeight < screenhight):
        p2Y += 5

    ballX += ballDx
    ballY += ballDy

    if(ball.colliderect(p1Paddle)):
        ballDx = abs(ballDx)
    elif (ball.colliderect(p2Paddle)):
        ballDx = abs(ballDx) * -1
    elif(ballY <= 0):
        ballDy = abs(ballDy)
    elif(ballY >= screenhight):
        ballDy = abs(ballDy) * -1
    elif(ballX >= screenwidth or ballX<= 0):
        if ballX >= screenwidth:
            p1Points += 1
        elif ballX <= 0:
            p2Points += 1

        ballX = 450
        ballY = 300
        p1Y = 250
        p2Y = 250



    screen.fill(BGCOLOR) 
    draw.rect(screen,BLUE,p1Paddle)
    draw.rect(screen,RED,p2Paddle)
    draw.rect(screen,white,ball)

    p1PtsTxt = calibriBold35.render('P1 POINTS: ' + str(p1Points),True,BLUE)
    p2PtsTxt = calibriBold35.render('P2 POINTS: '+ str(p2Points), True, RED)

    screen.blit(p1PtsTxt,(130,20))
    screen.blit(p2PtsTxt,(620,20))
    display.flip()
    myClock.tick(60)

quit()