import cv2

class TextAdder:
    @staticmethod
    def put_text(image, text, org, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(255,255,255), thickness=2):
        return cv2.putText(image.copy(), text, org, font, font_scale, color, thickness, cv2.LINE_AA)