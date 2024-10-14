import pygame, sys
from  PIL import  Image,ImageGrab
from numpy import asarray
pygame.init()
window=pygame.display.set_mode((1200,400))
track=pygame.image.load('track_5.jpg')
car=pygame.image.load('Lambi.png')
car=pygame.transform.scale(car,(30,60))
intro = pygame.image.load('intro.png')
pause = pygame.image.load('pause.png')
resume = pygame.image.load('resume.png')
lambox=155
lamboy=300
focal_dis=25
sensor_x_offset=0
sensor_y_offset=0
direction='up'
drive=True
clock=pygame.time.Clock()
import time
flag = True
while flag:
    window.blit(intro, (0,0))
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
        xpos,ypos=event.pos
        if xpos > 865 and xpos < 1090 and ypos > 73 and ypos < 150:
            break

    pygame.display.update()

def pr(window):
    pygame.draw.rect(window,(47, 171, 109),(0, 0, 75, 75), 0)
    window.blit(pause, (0, 0))
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                xpos,ypos=event.pos
                if xpos<80 and ypos<80:
                    return
def takescreenshot():
    im=ImageGrab.grab().convert('L')
    data=im.load()
    print(asarray(im))

    for i in range(160,180):
        for j in range(300,350):
            data[i,j]=0
    im.show()

while drive:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            drive=False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            xpos,ypos=event.pos
            if xpos < 80 and ypos < 80:
                pr(window)
    clock.tick(60)
    cam_x= lambox + sensor_x_offset + 15
    cam_y= lamboy + sensor_y_offset + 15
    up_px=window.get_at((cam_x,cam_y-focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y+focal_dis))[0]
    right_px = window.get_at((cam_x+focal_dis, cam_y))[0]

    # print(up_px,right_px,down_px)
    #change direction
    if direction=='up' and  up_px!=255 and right_px==255:
        direction='right'
        sensor_x_offset=30
        car=pygame.transform.rotate(car,-90)
    elif direction=='right' and right_px!=255 and down_px==255:
        direction='down'
        lambox= lambox + 30
        sensor_x_offset=0
        sensor_y_offset=30
        car=pygame.transform.rotate(car,-90)
    elif direction=='down' and down_px!=255 and right_px==255:
        direction='right'
        lamboy= lamboy + 30
        sensor_x_offset=30
        sensor_y_offset=0
        car=pygame.transform.rotate(car,90)
    elif direction=='right' and right_px!=255 and up_px==255:
        direction='up'
        lambox= lambox + 30
        sensor_x_offset=0
        car=pygame.transform.rotate(car,90)
    #drive
    if direction=='up' and up_px==255:
        lamboy= lamboy - 2
    elif direction=='right' and right_px==255:
        lambox= lambox + 2
    elif direction=='down' and down_px==255:
        lamboy= lamboy + 2

    window.blit(track,(0,0))
    window.blit(car, (lambox, lamboy))
    window.blit(resume, (0,0))
    pygame.draw.circle(window, (0,255,0),(cam_x,cam_y),5,5)
    pygame.display.update()
    pygame.image.save(window,'screenshot.jpeg')
    img=Image.open('screenshot.jpeg')
    data = img.load()

    #img.show()
#    time.sleep(5)
    if direction=="up":
        for i in range(lambox + 5, lambox + 20):
            for j in range(lamboy - 10, lamboy - 50, -1):
                #if data[i, j]==0:
                 #sys.exit()
                 data[i,j]=0



    if direction=="right":
        for i in range(lambox + 60, lambox + 90):
            for j in range(lamboy, lamboy + 50):
                if data[i, j]==0:
                    sys.exit()
    if lambox==441 and lamboy==238:
        img.show()






