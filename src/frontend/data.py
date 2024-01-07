import pygame

from src.backend.cosmic_objects import Star, Satellite


class Colors:
    sun = (255, 255, 0)
    mercury = (80, 78, 81)
    venus = (202, 165, 180)
    earth = (100, 149, 237)
    moon = (188, 188, 188)
    mars = (188, 39, 50)
    jupiter = (180, 153, 98)
    saturn = (220, 167, 87)
    uranus = (182, 254, 251)
    neptune = (73, 100, 174)


class CosmicObjects:
    sun = Star("Sun", 0, 0, 30, Colors.sun)
    mercury = Satellite("Mercury", 50, 0, 5, Colors.mercury, sun, 50, -5)
    venus = Satellite("Venus", 100, 0, 15, Colors.venus, sun, 100, 3.5)
    earth = Satellite("Earth", 150, 0, 15, Colors.earth, sun, 150, -3)
    moon = Satellite("Moon", 180, 0, 4, Colors.moon, earth, 30, -39, 150)
    mars = Satellite("Mars", 230, 0, 7, Colors.mars, sun, 230, -2.4)
    jupiter = Satellite("Jupiter", 300, 0, 25, Colors.jupiter, sun, 350, -1.31, 2000)
    saturn = Satellite("Saturn", 400, 0, 23, Colors.saturn, sun, 450, -0.97, 2000)
    uranus = Satellite("Uranus", 500, 0, 20, Colors.uranus, sun, 550, 0.68, 2800)
    neptune = Satellite("Neptune", 600, 0, 20, Colors.neptune, sun, 650, -0.54, 3500)


class Images:
    mercury_image = pygame.image.load("../images/mercury.png")
    venus_image = pygame.image.load("../images/venus.png")
    earth_image = pygame.image.load("../images/earth.png")
    moon_image = pygame.image.load("../images/moon.png")
    mars_image = pygame.image.load("../images/mars.png")
    jupiter_image = pygame.image.load("../images/jupiter.png")
    saturn_image = pygame.image.load("../images/saturn.png")
    uranus_image = pygame.image.load("../images/uranus.png")
    neptune_image = pygame.image.load("../images/neptune.png")
