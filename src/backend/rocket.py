import math
import pygame

from src.backend.cosmic_objects import Satellite


class Rocket:
    def __init__(self, image: pygame.Surface, start_point: Satellite, speed: float):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_point.x, start_point.y)

        self.target = start_point
        self.direction = 0
        self.distance = 0

        self.speed = speed

        self.is_clicked = False

    def draw(self, window: pygame.Surface, font: pygame.font.Font):
        if self.distance > 15:
            x = self.rect.x + window.get_width() / 2
            y = self.rect.y + window.get_height() / 2

            rotated_image = pygame.transform.rotate(self.image, 1.2 * abs(self.direction) * 180 / math.pi)

            rocket = window.blit(rotated_image, (x, y))

            pos = pygame.mouse.get_pos()
            if rocket.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.is_clicked is False:
                    self.is_clicked = True
                    text = font.render(f"{round(self.distance, 3)}", 1, (255, 255, 255))
                    window.blit(text, (x + text.get_width() / 2, y + text.get_height() / 2))
            if self.is_clicked is True:
                text = font.render(f"{round(self.distance, 3)}", 1, (255, 255, 255))
                window.blit(text, (x + text.get_width() / 2, y + text.get_height() / 2))

            if pygame.mouse.get_pressed()[0] == 1 and not rocket.collidepoint(pos):
                self.is_clicked = False

    def set_target(self, target: Satellite):
        self.target = target

    def update(self):
        dx_target = self.target.x - self.rect.x
        dy_target = self.target.y - self.rect.y

        self.distance = math.sqrt(dx_target ** 2 + dy_target ** 2)

        self.direction = math.atan2(dy_target, dx_target)

        self.rect.x = self.rect.x + math.cos(self.direction) * self.speed
        self.rect.y = self.rect.y + math.sin(self.direction) * self.speed
