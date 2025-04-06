import cv2

class ImageSaver:
    @staticmethod
    def save_image(path: str, image):
        cv2.imwrite(path, image)