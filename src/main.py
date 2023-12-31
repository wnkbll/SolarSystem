import pygame

from src.frontend.init_gui import Gui


def main():
    gui = Gui()

    is_running = True
    while is_running:
        gui.fps_clock.tick(gui.fps)
        gui.window.fill((0, 0, 0))

        for event in pygame.event.get():
            if any((event.type == pygame.QUIT, event.type == pygame.KEYDOWN)) and event.key == pygame.K_ESCAPE:
                is_running = False

        for button in gui.buttons:
            button.draw(gui.window)

        for cosmic_object in gui.cosmic_objects:
            cosmic_object.update()
            cosmic_object.draw(gui.window, gui.font)

        gui.rocket.update()
        gui.rocket.draw(gui.window, gui.font)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
