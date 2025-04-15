import cv2
from canny_detector import CannyEdgeDetector

def main():
    image_path = "images/sample.jpg"
    detector = CannyEdgeDetector(image_path)
    original, edges = detector.process()

    cv2.imshow('Original Image', original)
    cv2.imshow('Canny Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
