import pygame
import os
import configurations as config

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
        clock.tick(30)
        screen.blit(config.backgrounds.menu, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                if config.sprites.start.rect.x < position[0] < config.sprites.start.rect.x + config.sprites.start.width:
                    if config.sprites.start.rect.y < position[1] < config.sprites.start.rect.y + config.sprites.start.height:
                        menu = False
                        game = True
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if config.sprites.start.rect.x < position[0] < config.sprites.start.rect.x + config.sprites.start.width:
                    if config.sprites.start.rect.y < position[1] < config.sprites.start.rect.y + config.sprites.start.height:
                        config.sprites.start.mouse_in()
                    else:
                        config.sprites.start.image = pygame.image.load(os.path.join(f'images/buttons/start/1.png')).convert()
        config.sprites.menu_elements.draw(screen)
        config.sprites.bottle.update()

        pygame.display.flip()

    while game:
        clock.tick(50)
        # screen.blit(config.backgrounds.menu, (0, 0))
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    config.sprites.scientist.walk("RIGHT")
                if event.key == pygame.K_a:
                    config.sprites.scientist.walk("LEFT")
            if event.type == pygame.KEYUP:
                config.sprites.scientist.image = pygame.image.load(os.path.join(f'images/scientist/0.png')).convert()
        config.sprites.player.draw(screen)

        pygame.display.flip()

pygame.quit()
