#!/usr/bin/python

from Boat import *
from BoatView import *
from HUD import *
from WindGenerator import *
from Water import *

import pygame
import math
from pygame import font
from pygame.locals import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Sailboat Sim')

    font = pygame.font.Font(None, 36)

    water = Water()
    water.update((0,0))
    bo = BoatView()
    h = HUD(font)
    windGen = WindGenerator(h)
    boatController = Boat(bo, h, water, windGen)

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(bo)
    all_sprites_list.add(h)

    clock = pygame.time.Clock()
    milliseconds = 0
    secoundCnt = 0
    keyDelay = 0
    framesCnt = 0
    frames = 0
    keyPressed = []
    x = 0
    y = 0

    while 1:
        #liczenie klatek
        if secoundCnt < 1000:
            framesCnt+=1
        else:
            frames = framesCnt
            secoundCnt= 0
            framesCnt=0
        for event in pygame.event.get():
            if event.type == QUIT:
                    return
            if event.type == KEYDOWN:
                keyPressed.append(event.key)
            if event.type == KEYUP:
                keyPressed.remove(event.key)

        if keyDelay > 20: 
            h.setWindSpeed(windGen.force)
            h.setWindmeterAngle(windGen.angle)
            keyDelay = 0
            boatController.logicUpdate()
            if K_LEFT in keyPressed:
                boatController.turnRudder(-1,2)
            if K_RIGHT in keyPressed:
                boatController.turnRudder(1,2)
            if K_a in keyPressed:
                boatController.rotateBoat(5)
            if K_d in keyPressed:
                boatController.rotateBoat(-5)     
            if K_UP in keyPressed:
                boatController.changeMaxWindAngle(1)
            if K_DOWN in keyPressed:
                boatController.changeMaxWindAngle(-1)
                        
        h.update()
        bo.update()
        windGen.update()
        screen.fill((255,255,255))
        screen.blit(water, (0, 0))
        all_sprites_list.draw(screen)

        text = font.render("FPS: "+str(frames), 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.topleft = (5,5) 
        screen.blit(text, textpos)

        pygame.display.flip()

        milliseconds = clock.tick_busy_loop(60)
        secoundCnt+=milliseconds
        keyDelay+=milliseconds

if __name__ == '__main__': main()
