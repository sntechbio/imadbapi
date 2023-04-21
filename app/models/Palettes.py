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
    PLASMA = "plasma"
    INFERNO = "inferno"
    CIVIDIS = "cividis"
    COOLWARM = "coolwarm"
    YLGNBU = "YlGnBu"
    BUPU = "BuPu"
    GNB = "GnBu"
    ORRD = "OrRd"
    PUBU = "PuBu"
    PUBUGN = "PuBuGn"
    PURD = "PuRd"
    RDPU = "RdPu"
    YLGN = "YlGn"
