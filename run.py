import pygame
import sys
size = width, height = 700, 600
black = 0, 0, 0
clock = pygame.time.Clock()   
colors = [(94, 189, 62), (255, 185, 0), (247, 130, 0), (226, 56, 56), (151, 57, 153), (0, 156, 223)]
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
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = speed
        self.vy = speed
    
    def update(self):
        if self.rect.centerx < self.rect.width or self.rect.centerx > width - self.rect.width:
            self.vx = -self.vx
        if self.rect.centery < self.rect.height:
            self.vy = -self.vy
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
    def __init__(self, i, j, color):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.Surface([100, 40])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = i
        self.rect.y = j

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(size)

    game_over = False

    sprites = pygame.sprite.Group()

    ball = Ball(300, 400, 4)

    platform = Platform(100, 25, 6)

    game_over = False
    
    for i in range(7):
        for j in range(6):
            block = Block(i * 100, j * 40, colors[j])
            sprites.add(block)

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_a] and platform.rect.left > 0:
                platform.rect.x -= platform.vx
            if key[pygame.K_d] and platform.rect.right < width:
                platform.rect.x += platform.vx
            if (ball.rect.bottom > height) or (len(sprites) <= 0):
                game_over = True
            if (ball.rect.colliderect(platform.rect)):
                if (ball.vx > 0):
                    dx = ball.rect.right - platform.rect.left
                else:
                    dx = platform.rect.right - ball.rect.left
                if (ball.vy > 0):
                    dy = ball.rect.bottom - platform.rect.top
                else:
                    dy = platform.rect.bottom - ball.rect.top
                if (abs(dx - dy) < 3):
                    ball.vy = -ball.vy
                    ball.vx = -ball.vx
                elif dx > dy:
                    ball.vy = -ball.vy
                elif dy > dx:
                    ball.vx = -ball.vx
            for sprite in sprites:
                if (pygame.sprite.collide_rect(ball, sprite)):
                    if (ball.vx > 0):
                        dx = ball.rect.right - sprite.rect.left
                    else:
                        dx = sprite.rect.right - ball.rect.left
                    if (ball.vy > 0):
                        dy = ball.rect.bottom - sprite.rect.top
                    else:
                        dy = sprite.rect.bottom - ball.rect.top
                    if (abs(dx - dy) < 3):
                        ball.vy = -ball.vy
                        ball.vx = -ball.vx
                    elif dx > dy:
                        ball.vy = -ball.vy
                    elif dy > dx:
                        ball.vx = -ball.vx
                    platform.image.fill(sprite.color)
                    ball.image.fill(sprite.color)
                    global FPS
                    FPS += 1
                    sprite.kill()
            
            ball.update()
            screen.fill(black)
            screen.blit(platform.image, platform.rect)
            screen.blit(ball.image, ball.rect)
            sprites.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)
        if (len(sprites) > 0):
            text = pygame.font.SysFont('arial', 36).render('Game Over', True, (255, 255, 255))
        else:
            text = pygame.font.SysFont('arial', 36).render('You Win!', True, (255, 255, 255))
        screen.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))
        pygame.display.flip()

if __name__ == '__main__':
    main()