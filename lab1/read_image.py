import cv2

class ImageReader:
    @staticmethod
    def read_image(path: str, mode: int = cv2.IMREAD_COLOR):
        image = cv2.imread(path, mode)
        if image is None:
            raise FileNotFoundError(f"Image not found at path: {path}")
        return image