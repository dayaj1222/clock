from enum import Enum, auto


RADIUS = 300

HEIGHT = 800
WIDTH = 1200
FPS = 60

CLOCK_COLOR = "WHITE"


class ArmType(Enum):
    HOUR = auto()
    MINUTE = auto()
    SECOND = auto()
