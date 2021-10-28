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
        self.shift_x = 0

    def update(self):
        if (self.rect.x + self.vx >= 0 and self.rect.x + self.rect.width + self.vx <= width):
            self.rect.x += self.vx + self.shift_x


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(size)

    active_game = False
    game_over = False
    text = pygame.font.SysFont('arial', 36).render('Game Over', True, (255, 255, 255))

    sprites = pygame.sprite.Group()

    ball = Ball(100, 100, 'basketball.png')

    platform = Platform('platform.png')


    sprites.add(ball)
    sprites.add(platform)


    while not active_game:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active_game = True

        while not game_over:


            clock.tick(FPS)

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active_game = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        platform.shift_x = 0
                        platform.vx = -5
                    elif event.key == pygame.K_d:
                        platform.shift_x = 0
                        platform.vx = 5
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        platform.vx = 0
                        platform.shift_x = -3
                    if event.key == pygame.K_d:
                        platform.vx = 0
                        platform.shift_x = 3
                    
            # Logic
            sprites.update()
            if pygame.sprite.collide_rect(ball, platform):
                ball.vy *= -1
            if (ball.rect.y + ball.rect.height >= height):
                game_over = True
            if platform.shift_x > 0:
                platform.shift_x -= 0.01
            if platform.shift_x < 0:
                platform.shift_x += 0.01
            # Draw
            screen.fill(black) 
            sprites.draw(screen)
            # Draw flip and wait
            pygame.display.flip()
        for sprite in sprites:
            sprite.kill()
        screen.fill(black) 
        screen.blit(text, (width//2 - 100, height//2 - 30))
        pygame.display.flip()

    sys.exit()


if __name__ == '__main__':
    main()