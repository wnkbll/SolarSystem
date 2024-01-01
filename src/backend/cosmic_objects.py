import math
import pygame

from src.backend.type_aliases import Color, Orbit


class CosmicObject:
    def __init__(self, name: str, x: float, y: float, radius: int, color: tuple[int, int, int]):
        self.name: str = name
        self.x: float = x
        self.y: float = y
        self.radius: int = radius
        self.color: Color = color

        self.is_clicked: bool = False

    def draw(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        pass

    def update(self) -> None:
        pass


class Star(CosmicObject):
    def __init__(self, name: str, x: float, y: float, radius: int, color: tuple[int, int, int]):
        super().__init__(name, x, y, radius, color)

    def draw(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        x = self.x + window.get_width() / 2
        y = self.y + window.get_height() / 2

        circle = pygame.draw.circle(window, self.color, (x, y), self.radius)

        pos = pygame.mouse.get_pos()
        if circle.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.is_clicked is False:
                self.is_clicked = True
                text = font.render(f"{self.name}", 1, (255, 255, 255))
                window.blit(text, (x + text.get_width() / 2, y + text.get_height() / 2))
        if self.is_clicked is True:
            text = font.render(f"{self.name}", 1, (255, 255, 255))
            window.blit(text, (x + text.get_width() / 2, y + text.get_height() / 2))

        if pygame.mouse.get_pressed()[0] == 1 and not circle.collidepoint(pos):
            self.is_clicked = False


class Satellite(CosmicObject):
    def __init__(self, name: str, x: float, y: float, radius: int, color: tuple[int, int, int], parent: CosmicObject,
                 distance: float, speed: float, threshold: int = 1000):

        super().__init__(name, x, y, radius, color)

        self.parent: CosmicObject = parent
        self.distance_to_parent: float = distance

        self.i: int = 0
        self.speed: float = speed

        self.orbit: Orbit = []
        self.threshold: int = threshold

    def draw(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        x = self.x + window.get_width() / 2
        y = self.y + window.get_height() / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x = point[0] + window.get_width() / 2
                y = point[1] + window.get_height() / 2

                updated_points.append((x, y))

            pygame.draw.lines(window, self.color, False, updated_points, 2)

            if len(self.orbit) > self.threshold:
                self.orbit.pop(0)

        circle = pygame.draw.circle(window, self.color, (x, y), self.radius)

        pos = pygame.mouse.get_pos()
        if circle.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.is_clicked:
                self.is_clicked = True
                text = font.render(f"{self.name}", 1, (255, 255, 255))
                window.blit(text, (x + text.get_width() / 2, y + text.get_height() / 2))
        if self.is_clicked:
            text = font.render(f"{self.name}", 1, (255, 255, 255))
            window.blit(text, (x + text.get_width() / 2, y + text.get_height() / 2))

        if pygame.mouse.get_pressed()[0] == 1 and not circle.collidepoint(pos):
            self.is_clicked = False

    def update(self) -> None:
        self.x = self.parent.x + math.cos(self.i * math.pi / 180) * self.distance_to_parent
        self.y = self.parent.y + math.sin(self.i * math.pi / 180) * self.distance_to_parent

        self.orbit.append((self.x, self.y))

        self.i += 0.2 * self.speed
