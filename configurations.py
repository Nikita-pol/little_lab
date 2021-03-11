from win32api import GetSystemMetrics
import pygame
import json
import os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)


class Settings:
    with open("settings.json", encoding="utf8") as sett:
        a11 = json.loads(sett.read())
    mode = a11["mode"]
settings = Settings
pygame.init()
screen = pygame.display.set_mode((270, 470))
pygame.display.set_caption("My Crazy Laboratory")
screen.blit(settings.background, (0, 0))


class Images:
    start_btn = pygame.image.load(os.path.join(f'images/buttons/start/1.png')).convert()


images = Images


class Sprites:
    class Button(pygame.sprite.Sprite):
        def __init__(self, coord_x, coord_y, image):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(image, (int((WIDTH * 48 // 100)), int(HEIGHT * 17.5 // 100)))
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.x = coord_x
            self.rect.y = coord_y

    class Scientist(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.frame = 24
            self.image = pygame.image.load(
                os.path.join(f'images/scientist/{str(self.frame)}.png')).convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.position = [(WIDTH * 0.35) // 2, HEIGHT - ((HEIGHT * 0.4) // 2)]
            self.rect.center = (self.position[0], self.position[1])

        def walk(self, direction):
            if direction == "LEFT":
                img = pygame.image.load(os.path.join(f'images/scientist/{str(self.frame)}.png')).convert()
            elif direction == "RIGHT":
                img = pygame.image.load(os.path.join(f'images/scientist/{str(self.frame+24)}.png')).convert()
            else:
                img = None
            self.image = pygame.transform.scale(img, (int((WIDTH * 0.282)), int(HEIGHT * 0.3786)))
            print(int((WIDTH * 0.282)), int(HEIGHT * 0.3786))
            self.image.set_colorkey(WHITE)
            self.position[0] += 5
            self.frame += 1
            if self.frame > 24:
                self.frame = 1
            self.rect.center = (self.position[0], self.position[1])

    class Bottle(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.mode = 53
            self.image = pygame.image.load(
                os.path.join(f'images/bottle/{str(self.mode)}.png')).convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = (500, 300)

        def update(self):
            self.mode += 1
            if self.mode >= 54:
                self.mode = 1
            self.image = pygame.image.load(
                os.path.join(f'images/bottle/{str(self.mode)}.png')).convert()
            self.image.set_colorkey(BLACK)

    player = pygame.sprite.Group()
    scientist = Scientist()
    player.add(scientist)

    menu_elements = pygame.sprite.Group()
    bottle = Bottle()
    start = Button(int(WIDTH * 0.347), int(HEIGHT * 0.26), images.start_btn)
    menu_elements.add(bottle, start)


class Background:
    bg = pygame.image.load(f'images/backgrounds/menu.png')
    menu = pygame.transform.scale(bg, (WIDTH, HEIGHT))


sprites = Sprites
backgrounds = Background
settings = Settings

pygame.quit()
