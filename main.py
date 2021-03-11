import pygame
import configurations as config

FPS = 50

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
if config.settings.mode == "little":
    pygame.display.set_caption("My Little Laboratory")
if config.settings.mode == "crazy":
    pygame.display.set_caption("My Crazy Laboratory")
clock = pygame.time.Clock()

running = True
menu = True
game = False

while running:
    while menu:
        clock.tick(FPS)
        screen.blit(config.backgrounds.menu, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    config.sprites.scientist.walk("RIGHT")
                if event.key == pygame.K_a:
                    config.sprites.scientist.walk("LEFT")
        config.sprites.menu_elements.draw(screen)

        pygame.display.flip()

    while game:
        clock.tick(FPS)
        screen.blit(config.backgrounds.menu, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
        config.sprites.player.draw(screen)

pygame.quit()
