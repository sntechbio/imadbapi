from enum import Enum
import seaborn as sns


class Palette(str, Enum):
    BLUE_PURPLE = 'PRGn'
    GREEN_BLUE = 'BrBG'
    YELLOW_GREEN = 'YlGnBu'
    RED_YELLOW = 'RdYlBu'
    PURPLE_PINK = 'RdPu'
    VIRIDIS = "viridis"
    MAGMA = "magma"