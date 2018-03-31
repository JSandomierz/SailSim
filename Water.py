import pygame
 
class Water(pygame.surface.Surface):
    sprite = pygame.image.load("img/new_water.jpg")
    def __init__(self):
        super().__init__((800,600))
    def update(self, pos):
        self.fill((0,0,0,0))
        water_rect = Water.sprite.get_rect()
        water_rect.topleft = (-800-(pos[0])%800,-600-(pos[1])%600)
        self.blit(Water.sprite, water_rect)
