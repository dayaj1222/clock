from datetime import datetime
import math

import pygame

from src.config import CLOCK_COLOR, ArmType


class Arm:
    def __init__(
        self, name: ArmType, length: int, centre: tuple[int, int], thickness: int
    ) -> None:
        self.name = name
        self.length = length
        self.centre = centre
        self.end = (0, 0)
        self.thickness = thickness

    def _calculate(self, time: datetime):
        match self.name:
            case ArmType.SECOND:
                fraction = (time.second) / 60
            case ArmType.MINUTE:
                fraction = (time.minute) / 60 + (time.second) / 3600
            case ArmType.HOUR:
                fraction = (
                    (time.hour % 12) / 12 + (time.minute) / 720 + (time.second) / 43200
                )
        angle = fraction * math.pi * 2 - math.pi / 2
        self.end = (
            int(self.centre[0] + self.length * math.cos(angle)),
            int(self.centre[1] + self.length * math.sin(angle)),
        )

    def draw(self, time: datetime, screen: pygame.Surface):
        self._calculate(time)
        pygame.draw.line(screen, CLOCK_COLOR, self.centre, self.end, self.thickness)
