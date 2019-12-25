import pygame

from model.Cat import Cat

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Racket Cat Adventures')

clock = pygame.time.Clock()
crashed = False
background_image = pygame.image.load('image/background.png')
background_image = pygame.transform.scale(background_image, (display_width, display_height))
cat = Cat(display, 0, 330)


def draw_background():
    display.blit(background_image, (0, 0))


def key_handle_down(key):
    if key == pygame.K_a:
        cat.vx = -5
    elif key == pygame.K_d:
        cat.vx = 5
    elif key == pygame.K_w and cat.y == cat.GROUND_LEVEL:
        cat.jumping = True


def key_handle_up(key):
    if key == pygame.K_d and cat.vx == 5:
        cat.vx = 0
    elif key == pygame.K_a and cat.vx == -5:
        cat.vx = 0
    elif key == pygame.K_w:
        cat.jumping = False


if __name__ == '__main__':
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                key_handle_down(event.key)
            if event.type == pygame.KEYUP:
                key_handle_up(event.key)
        draw_background()
        cat.draw()
        cat.move()
        pygame.display.update()
        clock.tick(100)
    pygame.quit()
    quit()
