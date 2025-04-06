import cv2

class ImageResizer:
    @staticmethod
    def resize(image, width, height):
        return cv2.resize(image, (width, height))