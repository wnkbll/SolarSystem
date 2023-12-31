import pygame

from src.backend.cosmic_objects import Star, Satellite, CosmicObject
from src.backend.rocket import Rocket

from src.frontend.components.button import Button

SUN = (255, 255, 0)
MERCURY = (80, 78, 81)
VENUS = (202, 165, 180)
EARTH = (100, 149, 237)
MOON = (188, 188, 188)
MARS = (188, 39, 50)
JUPITER = (180, 153, 98)
SATURN = (220, 167, 87)
URANUS = (182, 254, 251)
NEPTUNE = (73, 100, 174)


class Gui:
    def __init__(self):
        pygame.init()

        width, height = 1920, 1080
        self.window: pygame.Surface = pygame.display.set_mode((width, height))

        pygame.display.set_caption("SolarSystem")

        self.font: pygame.font.Font = pygame.font.SysFont("comicsans", 16)

        self.fps: int = 60
        self.fps_clock: pygame.time.Clock = pygame.time.Clock()

        self.cosmic_objects: list = [CosmicObject]
        self.buttons: list[Button] = []
        self.rocket = None

        self.init_cosmic_objects()
        self.init_buttons()
        self.init_rocket()

    def init_cosmic_objects(self):
        sun = Star("Sun", 0, 0, 30, SUN)
        mercury = Satellite("Mercury", 50, 0, 5, MERCURY, sun, 50, -5)
        venus = Satellite("Venus", 100, 0, 15, VENUS, sun, 100, 3.5)
        earth = Satellite("Earth", 150, 0, 15, EARTH, sun, 150, -3)
        moon = Satellite("Moon", 180, 0, 4, MOON, earth, 30, -39, 150)
        mars = Satellite("Mars", 230, 0, 7, MARS, sun, 230, -2.4)
        jupiter = Satellite("Jupiter", 300, 0, 25, JUPITER, sun, 350, -1.31, 2000)
        saturn = Satellite("Saturn", 400, 0, 23, SATURN, sun, 450, -0.97, 2000)
        uranus = Satellite("Uranus", 500, 0, 20, URANUS, sun, 550, 0.68, 2800)
        neptune = Satellite("Neptune", 600, 0, 20, NEPTUNE, sun, 650, -0.54, 3500)

        self.cosmic_objects = [sun, mercury, venus, earth, moon, mars, jupiter, saturn, uranus, neptune]

    def init_buttons(self):
        mercury_image = pygame.image.load("images/mercury.png")
        venus_image = pygame.image.load("images/venus.png")
        earth_image = pygame.image.load("images/earth.png")
        moon_image = pygame.image.load("images/moon.png")
        mars_image = pygame.image.load("images/mars.png")
        jupiter_image = pygame.image.load("images/jupiter.png")
        saturn_image = pygame.image.load("images/saturn.png")
        uranus_image = pygame.image.load("images/uranus.png")
        neptune_image = pygame.image.load("images/neptune.png")

        mercury_button = Button(15, 15, mercury_image, 1, lambda: self.rocket.set_target(self.cosmic_objects[1]))
        venus_button = Button(15, 84, venus_image, 1, lambda: self.rocket.set_target(self.cosmic_objects[2]))
        earth_button = Button(15, 153, earth_image, 1, lambda: self.rocket.set_target(self.cosmic_objects[3]))
        moon_button = Button(15, 222, moon_image, 1, lambda: self.rocket.set_target(self.cosmic_objects[4]))
        mars_button = Button(15, 291, mars_image, 1, lambda: self.rocket.set_target(self.cosmic_objects[5]))
        jupiter_button = Button(15, 360, jupiter_image, 1, lambda: self.rocket.set_target(self.cosmic_objects[6]))
        saturn_button = Button(5, 429, saturn_image, 1, lambda: self.rocket.set_target(self.cosmic_objects[7]))
        uranus_button = Button(15, 498, uranus_image, 1, lambda: self.rocket.set_target(self.cosmic_objects[8]))
        neptune_button = Button(15, 567, neptune_image, 1, lambda: self.rocket.set_target(self.cosmic_objects[9]))

        self.buttons = [mercury_button, venus_button, earth_button, moon_button, mars_button, jupiter_button, saturn_button, uranus_button, neptune_button]

    def init_rocket(self):
        rocket_image = pygame.image.load("images/rocket.png")

        self.rocket = Rocket(rocket_image, self.cosmic_objects[3], 3)