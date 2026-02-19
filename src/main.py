import pygame
from pygame import Vector2
import math
from player import Player
from wall import Wall

class Main:
    def __init__(self):
        pygame.init()
        self.window_w, self.window_h = 800, 600
        self.display = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("dungeon crawler")
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.player = Player(self.all_sprites)
        self.wall = Wall(self.all_sprites, self.walls)

    def collision(self):
        for wall in self.walls:
            if pygame.sprite.collide_rect(wall, self.player):
                player_center = Vector2(self.player.rect.center)
                wall_center = Vector2(wall.rect.center)

                delta = player_center - wall_center

                hs_player = Vector2(25, 25)
                hs_wall = Vector2(25, 25)

                min_dist = Vector2((hs_player.x + hs_wall.x - abs(delta.x)),
                                  (hs_player.y + hs_wall.y - abs(delta.y)))

                if min_dist.x < min_dist.y:
                    self.player.rect.x += math.copysign(min_dist.x, delta.x)
                else:
                    self.player.rect.y += math.copysign(min_dist.y, delta.y)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.dt = self.clock.tick(60) / 1000

            self.display.fill("black")
            self.all_sprites.draw(self.display)
            self.player.update(self.dt)
            self.collision()

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Main()
    game.run()
