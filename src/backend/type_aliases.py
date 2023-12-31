import pygame

from typing import Protocol


class Drawable(Protocol):
    def draw(self, window: pygame.Surface, font: pygame.font.Font):
        pass

    def update(self):
        pass
