import cv2

class ImageDisplayer:
    @staticmethod
    def show_image(title: str, image):
        cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()