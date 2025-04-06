import cv2

class ThresholdingProcessor:
    @staticmethod
    def apply_all_thresholds(image, thresh_val=127, max_val=255):
        _, binary = cv2.threshold(image, thresh_val, max_val, cv2.THRESH_BINARY)
        _, binary_inv = cv2.threshold(image, thresh_val, max_val, cv2.THRESH_BINARY_INV)
        _, trunc = cv2.threshold(image, thresh_val, max_val, cv2.THRESH_TRUNC)
        _, tozero = cv2.threshold(image, thresh_val, max_val, cv2.THRESH_TOZERO)
        _, tozero_inv = cv2.threshold(image, thresh_val, max_val, cv2.THRESH_TOZERO_INV)
        return {
            'THRESH_BINARY': binary,
            'THRESH_BINARY_INV': binary_inv,
            'THRESH_TRUNC': trunc,
            'THRESH_TOZERO': tozero,
            'THRESH_TOZERO_INV': tozero_inv
        }

    @staticmethod
    def apply_otsu(image):
        _, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return otsu