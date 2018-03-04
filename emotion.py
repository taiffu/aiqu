'''
Created on 4.3.2018

@author: Sami<sami@tabloiti.com>
'''
import pygame
import os
from time import sleep

RED = (255,0,0)
TUR = (50,156,198)

SIZEW = 320
SIZEH = 240

EW = 70*1.5
EH = 100*1.5
EPOS = 40
LEYPOS = 50
REYPOS = 160

stoped = False

os.putenv('SDL_FBDEV', '/dev/fb1')
NEUTRAL = 1
LOOKDOWN = 2
LOOKRIGHT = 3
LOOKLEFT = 4

state = NEUTRAL


def texts(score):
   lcd.fill((0,0,0))
   font=pygame.font.Font(None,30)
   scoretext=font.render("FPS:" + str(score), 1,(255,255,255))
   lcd.blit(scoretext, (0, 0))

def neutral():
  state = NEUTRAL
  #left eye
  pygame.draw.ellipse(lcd, TUR, [LEYPOS, EPOS, EW, EH])
  #right eye
  pygame.draw.ellipse(lcd, TUR, [REYPOS, EPOS, EW, EH])
  pygame.display.update()

def lookdown():
  state = LOOKDOWN
  #left eye
  pygame.draw.ellipse(lcd, TUR, [LEYPOS, EPOS+20, EW, EH])
  #right eye
  pygame.draw.ellipse(lcd, TUR, [REYPOS, EPOS+20, EW, EH])
  pygame.display.update()


def lookright():
  state = LOOKRIGHT
  #left eye
  pygame.draw.ellipse(lcd, TUR, [LEYPOS+20, EPOS, EW, EH])
  #right eye
  pygame.draw.ellipse(lcd, TUR, [REYPOS+20, EPOS, EW, EH])
  pygame.display.update()

def lookleft():
  state = LOOKLEFT
  #left eye
  pygame.draw.ellipse(lcd, TUR, [LEYPOS-20, EPOS, EW, EH])
  #right eye
  pygame.draw.ellipse(lcd, TUR, [REYPOS-20, EPOS, EW, EH])
  pygame.display.update()
  

#Main code
pygame.init()
lcd = pygame.display.set_mode((320, 240))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

neutral()

pygame.display.update()
pygame.mouse.set_visible(False)

fps = 0


#MAIN LOOP START HERE
while not stoped:
 fps = fps+1
 if fps >= 60:
	fps = 0;

 texts(fps)
 if state == NEUTRAL:
	neutral()
 if state == LOOKDOWN:
	lookdown()
 if state == LOOKRIGHT: 
	lookright()
 if state == LOOKLEFT:
	lookleft()
 #sleep(2)
 pygame.display.update()
 clock.tick(60)

 for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stoped = True

	if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
		state = LOOKRIGHT
    	   	lookright()
	   if event.key == pygame.K_LEFT:
		state =  LOOKLEFT
                lookleft()
	   if event.key == pygame.K_UP:
		state = NEUTRAL
                neutral()
	   if event.key == pygame.K_DOWN:
		state = LOOKDOWN
                lookdown()
	 

