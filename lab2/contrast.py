import cv2
import numpy as np

class ContrastAdjuster:
    @staticmethod
    def adjust_contrast(image, alpha: float):
        return cv2.convertScaleAbs(image, alpha=alpha, beta=0)
