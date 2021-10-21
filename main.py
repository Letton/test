import pygame
import sys
import random

size = width, height = 800, 600
black = 0, 0, 0

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(size)
    sprite = Sprite(5, 5, 'basketball.png')
    sprite.render()
    class Game_Object():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Ball(Game_Object):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.shift_x = 5
            self.shift_y = 5
            self.textured_object = pygame.image.load('basketball.png')
            self.rect = self.textured_object.get_rect()
            self.rect.x = x
            self.rect.y = y

        def logic(self):
            if (self.rect.y + self.rect.height >= height) or (self.rect.y <= 0):
                self.shift_y *= -1
            if (self.rect.x + self.rect.width >= width) or (self.rect.x <= 0):
                self.shift_x *= -1
            self.rect.x += self.shift_x
            self.rect.y += self.shift_y
        
        def draw(self):
            screen.blit(self.textured_object, self.rect)

    game_over = False
    shift_x = 1
    shift_y = 1
    current_shift = 0
    rect_x = 0
    flag = False
    ball = Ball(width // 2, height // 2)


    while not game_over:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    current_shift = -1
                elif event.key == pygame.K_d:
                    current_shift = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    current_shift = 0
        # Logic
        ball.logic()
        # Draw
        screen.fill(black) 
        ball.draw()
        # Draw flip and wait
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    main()