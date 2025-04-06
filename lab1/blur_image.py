import cv2

class ImageBlurrer:
    @staticmethod
    def blur(image, ksize=(11, 11)):
        return cv2.GaussianBlur(image, ksize, 0)