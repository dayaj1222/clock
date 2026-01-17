import pygame

from src.clock import Clock
from src.config import FPS, HEIGHT, WIDTH


def main():

    pygame.init()
    pygame.display.set_caption("Clock")

    running = True

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    myclock = Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(FPS)
        screen.fill("BLACK")
        myclock.update(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
