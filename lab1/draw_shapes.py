import cv2

class ShapeDrawer:
    @staticmethod
    def draw_rectangle(image, start, end, color, thickness):
        return cv2.rectangle(image.copy(), start, end, color, thickness)

    @staticmethod
    def draw_line(image, pt1, pt2, color, thickness):
        return cv2.line(image.copy(), pt1, pt2, color, thickness)

    @staticmethod
    def draw_circle(image, center, radius, color, thickness):
        return cv2.circle(image.copy(), center, radius, color, thickness)