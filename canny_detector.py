import cv2


class CannyEdgeDetector:
    def __init__(self, image_path: str, low_threshold: int = 100, high_threshold: int = 200):
        self.image_path = image_path
        self.low_threshold = low_threshold
        self.high_threshold = high_threshold

    def process(self):
        img = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError(f"Image not found at: {self.image_path}")

        edges = cv2.Canny(img, self.low_threshold, self.high_threshold)
        return img, edges
