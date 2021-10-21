import pygame
import sys
import random

size = width, height = 800, 600
black = 0, 0, 0
clock = pygame.time.Clock()
        
FPS = 60

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 5
        self.vy = 5

    def update(self):
        if (self.rect.y + self.rect.height >= height) or (self.rect.y <= 0):
            self.vy *= -1
        if (self.rect.x + self.rect.width >= width) or (self.rect.x <= 0):
            self.vx *= -1
        self.rect.x += self.vx
        self.rect.y += self.vy

class Platform(pygame.sprite.Sprite):
    def __init__(self, path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height - 50
        self.vx = 0

    def update(self):
        if (self.rect.x + self.vx >= 0 and self.rect.x + self.rect.width + self.vx <= width):
            self.rect.x += self.vx


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(size)

    game_over = False

    sprites = pygame.sprite.Group()

    ball = Ball(100, 100, 'basketball.png')

    platform = Platform('platform.png')


    sprites.add(ball)
    sprites.add(platform)


    while not game_over:

        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    platform.vx = -5
                elif event.key == pygame.K_d:
                    platform.vx = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    platform.vx = 0
        # Logic
        sprites.update()
        if pygame.sprite.collide_rect(ball, platform):
            ball.vy *= -1
        # Draw
        screen.fill(black) 
        sprites.draw(screen)
        # Draw flip and wait
        pygame.display.flip()

    sys.exit()


if __name__ == '__main__':
    main()