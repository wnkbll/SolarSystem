import pygame

from typing import Callable


class Button:
    def __init__(self, x: int, y: int, image: pygame.Surface, scale: float, callback: Callable, *args: tuple):
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(scale * width), int(scale * height)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.callback = callback
        self.args = args
        self.is_clicked = False

    def draw(self, window: pygame.Surface) -> None:
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.is_clicked is False:
                self.is_clicked = True
                if len(self.args) > 0:
                    self.callback(self.args)
                else:
                    self.callback()

        if pygame.mouse.get_pressed()[0] == 0:
            self.is_clicked = False

        window.blit(self.image, (self.rect.x, self.rect.y))
