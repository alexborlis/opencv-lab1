import cv2

class HistogramEqualizer:
    @staticmethod
    def equalize(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.equalizeHist(gray)
