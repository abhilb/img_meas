from pathlib import Path
import numpy as np
from enum import Enum

import cv2

class Transition(Enum):
    BLACK_TO_WHITE = 0,
    WHITE_TO_BLACK = 1

class LineDetectorParams(NamedTuple):
    threshold: int
    transition: Transition



def find_hline(img, )



