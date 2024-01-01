import math
import pygame

from src.backend.cosmic_objects import Satellite


class Rocket:
    def __init__(self, image: pygame.Surface, start_point: Satellite, speed: float):
        self.image: pygame.Surface = image
        self.rect: pygame.Rect = self.image.get_rect(center=(start_point.x, start_point.y))

        self.target: Satellite = start_point
        self.direction: float = 0
        self.distance: float = 0

        self.is_landed: bool = False

        self.speed: float = speed

        self.is_clicked: bool = False

    def draw(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        if self.distance > 25 and not self.is_landed:
            x = self.rect.x + window.get_width() / 2
            y = self.rect.y + window.get_height() / 2

            rotated_image = pygame.transform.rotate(self.image, abs(math.degrees(self.direction)))

            rocket = window.blit(rotated_image, (x, y))

            pos = pygame.mouse.get_pos()
            if rocket.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not self.is_clicked:
                self.is_clicked = True
                text = font.render(f"{round(self.distance, 3)}", 1, (255, 255, 255))
                window.blit(text, (x + text.get_width() / 2, y + text.get_height() / 2))
            if self.is_clicked:
                text = font.render(f"{round(self.distance, 3)}", 1, (255, 255, 255))
                window.blit(text, (x + text.get_width() / 2, y + text.get_height() / 2))

            if pygame.mouse.get_pressed()[0] == 1 and not rocket.collidepoint(pos):
                self.is_clicked = False
        else:
            self.is_landed = True

    def set_target(self, target: Satellite) -> None:
        self.target = target
        self.is_landed = False

    def update(self) -> None:
        dx_target = self.target.x - self.rect.x
        dy_target = self.target.y - self.rect.y

        self.distance = math.sqrt(dx_target ** 2 + dy_target ** 2)

        self.direction = math.atan2(dy_target, dx_target)

        self.rect.x = self.rect.x + math.cos(self.direction) * self.speed
        self.rect.y = self.rect.y + math.sin(self.direction) * self.speed
