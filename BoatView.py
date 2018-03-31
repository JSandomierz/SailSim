import pygame
import math
import copy

class BoatView(pygame.sprite.Sprite):
    image = pygame.image.load("img/boat.png")
    wingSprite = pygame.image.load("img/wing.png")
    rudderSprite = pygame.image.load("img/rudder.png")
    wingColor = (120,120,120)
    def __init__(self):
        super().__init__()
        self.image = BoatView.image
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
        self.rotaton=0
        self.rudderRotation=60
        self.wingRotation=0
        self.update()
    def setBoatRotation(self, angle):
        self.rotaton=angle
    def setWingRotation(self, angle):
        self.wingRotation = angle
    def setRudderRotation(self, angle):
        self.rudderRotation=angle
    def update(self):
        tmpBoat = copy.copy(BoatView.image);
        myRect = tmpBoat.get_rect() 
        rotatedRudder = pygame.transform.rotate(BoatView.rudderSprite, self.rudderRotation-60)
        rectRudder = rotatedRudder.get_rect()
        rectRudder.center = (25, myRect.h/2)
        tmpBoat.blit(rotatedRudder, rectRudder)
        self.image = pygame.transform.rotate(tmpBoat, self.rotaton)
        self.rect = self.image.get_rect(center=self.rect.center)

        rotatedWing = pygame.transform.rotate(BoatView.wingSprite, 360-self.wingRotation)
        rectWing = rotatedWing.get_rect()
        rectWing.center = (self.rect.w/2, self.rect.h/2)

        self.image.blit(rotatedWing, rectWing)

