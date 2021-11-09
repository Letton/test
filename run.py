import pygame
import sys
size = width, height = 500, 500
black = 0, 0, 0
clock = pygame.time.Clock()
        
FPS = 60

def detect_collision(dx, dy, ball, rect):
    if ball.vx > 0:
        delta_x = ball.rect.right - rect.left
    else:
        delta_x = rect.right - ball.rect.left
    if ball.vy > 0:
        delta_y = ball.rect.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.rect.top

    if abs(delta_x - delta_y) < 10:
        ball.vx, ball.vy = -ball.vx, -ball.vy
    elif delta_x > delta_y:
         ball.vy = - ball.vy
    elif delta_y > delta_x:
        ball.vx = -ball.vy
    return dx, dy

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        pygame.draw.circle(self.image, (255, 255, 0), (5, 5), 5)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 2
        self.vy = 2

    def update(self):
        if (self.rect.y + self.rect.height >= height) or (self.rect.y <= 0):
            self.vy *= -1
        if (self.rect.x + self.rect.width >= width) or (self.rect.x <= 0):
            self.vx *= -1
        self.rect.x += self.vx
        self.rect.y += self.vy

class Platform(pygame.sprite.Sprite):
    def __init__(self, w, h, vx):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height - self.rect.height // 2
        self.vx = vx

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([100, 50])
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(size)

    active_game = False
    game_over = False
    text = pygame.font.SysFont('arial', 36).render('Game Over', True, (255, 255, 255))

    #sprites = pygame.sprite.Group()

    #ball = Ball(300, 500)

    platform = Platform(100, 25, 1)


    #sprites.add(ball)
    #sprites.add(platform)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and platform.rect.left > 0:
            platform.rect.x -= platform.vx
            print(1)
        if key[pygame.K_d] and platform.rect.right < width:
            platform.rect.x += platform.vx

        screen.fill(black)
        screen.blit(platform.image, platform.rect)
        pygame.display.flip()


    # for i in range(7):
    #     for j in range(5):
    #         block = Block(i * 100 + 17 * i, j * 50 + 10 * j)
    #         sprites.add(block)

    # while not active_game:
        
    #     for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 active_game = True

    #     while not game_over:


    #         clock.tick(FPS)

    #         # Events
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 active_game = True
    #             elif event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_a:
    #                     platform.shift_x = 0
    #                     platform.vx = -2.5
    #                 elif event.key == pygame.K_d:
    #                     platform.shift_x = 0
    #                     platform.vx = 2.5
    #             elif event.type == pygame.KEYUP:
    #                 if event.key == pygame.K_a:
    #                     platform.vx = 0
    #                     platform.shift_x = -2.5
    #                 if event.key == pygame.K_d:
    #                     platform.vx = 0
    #                     platform.shift_x = 2.5
                    
    #         # Logic
    #         sprites.update()
    #         if pygame.sprite.collide_rect(ball, platform):
    #             ball.vy *= -1
    #         for sprite in sprites:
    #             if (sprite.__class__.__name__ == 'Block'):
    #                 if (pygame.sprite.collide_rect(ball, sprite)):
    #                     detect_collision(ball.vx, ball.vy, ball, sprite.rect)
    #                     sprite.kill()
    #         if (ball.rect.y + ball.rect.height >= height):
    #             game_over = True
    #         if platform.shift_x > 0:
    #             platform.shift_x -= 0.01
    #         if platform.shift_x < 0:
    #             platform.shift_x += 0.01
    #         # Draw
    #         screen.fill(black) 
    #         sprites.draw(screen)
    #         # Draw flip and wait
    #         pygame.display.flip()
    #     for sprite in sprites:
    #         sprite.kill()
    #     screen.fill(black) 
    #     screen.blit(text, (width//2 - 100, height//2 - 30))
    #     pygame.display.flip()

    # sys.exit()


if __name__ == '__main__':
    main()