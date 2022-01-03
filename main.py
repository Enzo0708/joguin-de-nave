import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
VEL = 5
BULLET_VEL = 7
MAX_BULLET = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 60, 42
BORDER = pygame.Rect((WIDTH/2 - 5), 0, 10, HEIGHT)


YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')),
                                          (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spaceship_red.png')),
                                          (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # left
        yellow.x += -VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height + 15 < HEIGHT:  # down
        yellow.y += VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width - 20 < (WIDTH/2 - 5):  # right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y + VEL - 8 > 0:  # up
        yellow.y += -VEL


def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # left
        red.x += -VEL
    if keys_pressed[pygame.K_0] and red.y + VEL + red.height + 15 < HEIGHT:  # down
        red.y += VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width - 20 < WIDTH:  # right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y + VEL - 8 > 0:  # up
        red.y += -VEL


def handle_bullets(yellow_bullets, red_bullets, red, yellow):
    

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT and len(yellow_bullets) < MAX_BULLET:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RALT and len(red_bullets) < MAX_BULLET:
                    bullet = pygame.Rect(red.x, red.y + red.height / 2 - 2, 10, 5)
                    red_bullets.append(bullet)

        print(red_bullets, yellow_bullets)

        keys_pressed = pygame.key.get_pressed()

        yellow_movement(keys_pressed, yellow)

        red_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
