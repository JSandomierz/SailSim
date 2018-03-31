from random import uniform
import math
import pygame
class WindGenerator:
    agressiveness = 0.01 #agresywność
    def __init__(self, hud):
        self.hud = hud
        self.force = uniform(5, 15) #startowa prędkość wiatru
        self.angle = uniform(0, 359.9) 
        self.dx = self.force*math.cos(math.radians(self.angle))
        self.dy = self.force*math.sin(math.radians(self.angle))
        self.dx_a = uniform(-WindGenerator.agressiveness, WindGenerator.agressiveness) 
        self.dy_a = uniform(-WindGenerator.agressiveness, WindGenerator.agressiveness) 
        self.updateTime = pygame.time.get_ticks()
        self.changeTime = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.updateTime >= 200:
            self.dx+=self.dx_a
            self.dy+=self.dy_a
            self.force = math.sqrt(math.pow(self.dx,2)+math.pow(self.dy,2))
            self.angle = math.degrees(math.atan2(self.dy, self.dx))
            self.hud.setWindmeterAngle(self.angle)
            self.hud.setWindSpeed(self.force)
        if now - self.changeTime >= 10000:
            self.changeTime = now
            self.dx_a = uniform(-WindGenerator.agressiveness, WindGenerator.agressiveness) 
            self.dy_a = uniform(-WindGenerator.agressiveness, WindGenerator.agressiveness) 

