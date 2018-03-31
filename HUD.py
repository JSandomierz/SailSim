import pygame
import math
from pygame import font
from pygame.locals import *

class HUD(pygame.sprite.Sprite):
    speedometers_sprite = pygame.image.load("img/hud-speed.png")
    compass_sprite = pygame.image.load("img/hud-compass.png")
    compass = pygame.image.load("img/compass.png")
    bars = pygame.image.load("img/bars.png")
    ballSprite = pygame.image.load("img/ball.png")

    def __init__(self, font):
        super().__init__()
        self.sur = pygame.Surface((800,600), SRCALPHA)
        self.font = font
        self.windmeter_angle=0
        self.boat_speed=0
        self.wind_speed=0
        self.rudderBarPercent = 50
        self.sailBarPercent=50
        self.update()

    def setWindmeterAngle(self, angle):
        self.windmeter_angle = angle

    def setRudderBar(self, percent):
        self.rudderBarPercent = percent

    def setSailBar(self, percent):
        self.sailBarPercent = percent

    def setBoatSpeed(self, speed):
        self.boat_speed = speed

    def setWindSpeed(self, speed):
        self.wind_speed = speed

    def update(self):
        self.sur.fill((0,0,0,0))
        speedometers_rect = HUD.speedometers_sprite.get_rect()
        speedometers_rect.bottomleft = (0,self.sur.get_rect().h)
        self.sur.blit(HUD.speedometers_sprite, speedometers_rect)
        compass_rect = HUD.compass_sprite.get_rect()
        compass_rect.bottomright = self.sur.get_rect().size
        self.sur.blit(HUD.compass_sprite, compass_rect)
        
        bars_rect = HUD.bars.get_rect()
        bars_rect.midbottom = (400, 587)
        self.sur.blit(HUD.bars, bars_rect)

        bars_text = self.font.render("ŻAGIEL", 1, (40, 40, 40))
        bars_text_rect = bars_text.get_rect()
        bars_text_rect.centerx = bars_rect.centerx
        bars_text_rect.top = bars_rect.top+10
        self.sur.blit(bars_text, bars_text_rect)
        bars_text = self.font.render("STER", 1, (40, 40, 40))
        bars_text_rect = bars_text.get_rect()
        bars_text_rect.centerx = bars_rect.centerx
        bars_text_rect.top = bars_rect.top+65
        self.sur.blit(bars_text, bars_text_rect)

        ball_rect = HUD.ballSprite.get_rect()
        ball_rect.center = (bars_rect.x+63+self.rudderBarPercent/100*232, bars_rect.bottom-32)
        self.sur.blit(HUD.ballSprite, ball_rect)

        ball_rect = HUD.ballSprite.get_rect()
        ball_rect.center = (bars_rect.x+63+self.sailBarPercent/100*232, bars_rect.bottom-86)
        self.sur.blit(HUD.ballSprite, ball_rect)

        boat_speed_text = self.font.render(str("%.1f" % self.wind_speed), 1, (40, 40, 40))
        boat_speed_text_rect = boat_speed_text.get_rect()
        boat_speed_text_rect.centerx = speedometers_rect.centerx+20
        boat_speed_text_rect.top = speedometers_rect.top+25
        self.sur.blit(boat_speed_text, boat_speed_text_rect)

        wind_speed_text = self.font.render(str("%.1f" % self.boat_speed), 1, (40, 40, 40))
        wind_speed_text_rect = wind_speed_text.get_rect()
        wind_speed_text_rect.centerx = speedometers_rect.centerx+20
        wind_speed_text_rect.top = speedometers_rect.top+80
        self.sur.blit(wind_speed_text, wind_speed_text_rect)

        self.igla = HUD.compass.convert_alpha()
        self.igla = pygame.transform.rotate(self.igla, 360-(self.windmeter_angle-90)%360)
        igla_rect = self.igla.get_rect()
        igla_rect.center = compass_rect.center
        self.sur.blit(self.igla, igla_rect)
        self.image = self.sur
        self.rect = self.image.get_rect()
