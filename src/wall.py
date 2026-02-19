import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((50, 50))
        self.image.fill("white")
        self.rect = self.image.get_rect(center = (100, 200))
