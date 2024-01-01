import pygame

from src.backend.cosmic_objects import CosmicObject
from src.backend.rocket import Rocket

from src.frontend.data import Images, CosmicObjects
from src.frontend.components import Button


class Gui:
    def __init__(self, width: int, height: int, fps: int):
        pygame.init()
        pygame.display.set_caption("SolarSystem")

        self.window: pygame.Surface = pygame.display.set_mode((width, height))
        self.font: pygame.font.Font = pygame.font.SysFont("comicsans", 16)

        self.fps: int = fps
        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.cosmic_objects: list[CosmicObject] = []
        self.buttons: list[Button] = []
        self.rocket: Rocket = Rocket(pygame.image.load("images/rocket.png"), CosmicObjects.earth, 3)

        self.init_cosmic_objects()
        self.init_buttons()

    def init_cosmic_objects(self) -> None:
        self.cosmic_objects = [CosmicObjects.sun, CosmicObjects.mercury, CosmicObjects.venus, CosmicObjects.earth,
                               CosmicObjects.moon, CosmicObjects.mars, CosmicObjects.jupiter, CosmicObjects.saturn,
                               CosmicObjects.uranus, CosmicObjects.neptune]

    def init_buttons(self) -> None:
        mercury_button = Button(15, 15, Images.mercury_image, 1, lambda: self.rocket.set_target(CosmicObjects.mercury))
        venus_button = Button(15, 84, Images.venus_image, 1, lambda: self.rocket.set_target(CosmicObjects.venus))
        earth_button = Button(15, 153, Images.earth_image, 1, lambda: self.rocket.set_target(CosmicObjects.earth))
        moon_button = Button(15, 222, Images.moon_image, 1, lambda: self.rocket.set_target(CosmicObjects.moon))
        mars_button = Button(15, 291, Images.mars_image, 1, lambda: self.rocket.set_target(CosmicObjects.mars))
        jupiter_button = Button(15, 360, Images.jupiter_image, 1, lambda: self.rocket.set_target(CosmicObjects.jupiter))
        saturn_button = Button(5, 429, Images.saturn_image, 1, lambda: self.rocket.set_target(CosmicObjects.saturn))
        uranus_button = Button(15, 498, Images.uranus_image, 1, lambda: self.rocket.set_target(CosmicObjects.uranus))
        neptune_button = Button(15, 567, Images.neptune_image, 1, lambda: self.rocket.set_target(CosmicObjects.neptune))

        self.buttons = [mercury_button, venus_button, earth_button, moon_button, mars_button, jupiter_button,
                        saturn_button, uranus_button, neptune_button]

    def setup(self) -> None:
        is_running = True
        while is_running:
            self.clock.tick(self.fps)
            self.window.fill((0, 0, 0))

            for event in pygame.event.get():
                if any((event.type == pygame.QUIT, event.type == pygame.KEYDOWN)) and event.key == pygame.K_ESCAPE:
                    is_running = False

            for button in self.buttons:
                button.draw(self.window)

            for cosmic_object in self.cosmic_objects:
                cosmic_object.update()
                cosmic_object.draw(self.window, self.font)

            self.rocket.update()
            self.rocket.draw(self.window, self.font)

            pygame.display.update()

        pygame.quit()
