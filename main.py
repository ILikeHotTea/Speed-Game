import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 150)
running = True

min_speed = 1
max_speed = 2
score = 0 

class Square(pygame.sprite.Sprite):
    def __init__(self, min_speed, max_speed):
        super().__init__()

        self.min_speed = min_speed
        self.max_speed = max_speed
        self.reset()

    def reset(self):
        self.vx = randint(self.min_speed, self.max_speed) * randint(-1, 2)
        self.vy = randint(self.min_speed, self.max_speed) * randint(-1, 2)

        self.rect = pygame.Rect(310, 310, 100, 100)
        self.velocity = pygame.math.Vector2(self.vx, self.vy)

        self.min_speed += 1
        self.max_speed += 1

    def draw(self):
        pygame.draw.rect(screen, 'blue', self.rect)

    def update(self, score):
        self.rect.move_ip(self.velocity)

        if self.rect.y >= 720 or self.rect.y <= 0 or self.rect.x >= 720 or self.rect.x <= 0:
            self.reset()
            self.min_speed = 1
            self.max_speed = 2
            score = 0

        return score


def display_score(score):
    score_surf = font.render(f'{score}', True, 'black')
    screen.blit(score_surf, (330, 0))
    pygame.display.update()


square = pygame.sprite.GroupSingle()
square.add(Square(min_speed, max_speed))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if square.sprite.rect.collidepoint(event.pos):
                square.sprite.reset()
                score += 1

    screen.fill('white')
    square.sprite.draw()
    score = square.sprite.update(score)
    display_score(score)

    clock.tick(60)
