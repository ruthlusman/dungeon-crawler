import pygame
from pygame import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((50, 50))
        self.image.fill("blue")
        self.rect = self.image.get_rect(center = (400, 300))
        self.direction = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.speed = 400

    def movement(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        self.velocity.x = self.direction.x * self.speed
        self.velocity.y = self.direction.y * self.speed

        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

    def update(self, dt):
        self.movement(dt)
