from datetime import datetime

from pygame import Rect, Surface
import pygame

from src.config import CLOCK_COLOR


class DigitalClock:
    def __init__(self) -> None:
        self.font = pygame.font.SysFont(None, 45)
        self.rect = Rect(40, 30, 200, 80)

    def draw(self, screen: Surface):
        pygame.draw.rect(screen, CLOCK_COLOR, self.rect, width=5, border_radius=20)
        current_time = datetime.now().strftime("%H:%M:%S")
        text_surface = self.font.render(current_time, True, CLOCK_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
