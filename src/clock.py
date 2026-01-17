from datetime import datetime
import pygame

from src.config import RADIUS, HEIGHT, WIDTH, ArmType, CLOCK_COLOR
from src.arm import Arm
from src.digital_clock import DigitalClock


class Clock:
    def __init__(self) -> None:
        self.time = datetime.now()
        self.centre = (int(WIDTH / 2), int(HEIGHT / 2))
        self.second_arm = Arm(
            name=ArmType.SECOND, length=RADIUS - 10, centre=self.centre, thickness=10
        )
        self.minute_arm = Arm(
            name=ArmType.MINUTE, length=RADIUS - 30, centre=self.centre, thickness=12
        )
        self.hour_arm = Arm(
            name=ArmType.HOUR, length=RADIUS - 80, centre=self.centre, thickness=20
        )
        self.dig_clock = DigitalClock()

    def update(self, screen):
        pygame.draw.circle(screen, CLOCK_COLOR, self.centre, RADIUS, width=3)

        self.second_arm.draw(self.time, screen)
        self.minute_arm.draw(self.time, screen)
        self.hour_arm.draw(self.time, screen)
        self.time = datetime.now()

        self.dig_clock.draw(screen)
