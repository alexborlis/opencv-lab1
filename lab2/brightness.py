import cv2
import numpy as np

class BrightnessAdjuster:
    @staticmethod
    def adjust_brightness(image, value: int):
        return cv2.convertScaleAbs(image, alpha=1, beta=value)
