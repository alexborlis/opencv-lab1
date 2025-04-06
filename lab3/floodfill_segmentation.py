import cv2
import numpy as np

class FloodFillSegmentation:
    @staticmethod
    def apply(image, seed_point=(10, 10), new_color=(0, 255, 0)):
        image_copy = image.copy()
        h, w = image.shape[:2]
        mask = np.zeros((h + 2, w + 2), np.uint8)
        cv2.floodFill(image_copy, mask, seed_point, new_color)
        return image_copy