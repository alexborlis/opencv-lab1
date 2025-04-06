import cv2
import os
from lab3.watershed_segmentation import WaterShedSegmentation
from lab3.meanshift_segmentation import MeanShiftSegmentation
from lab3.floodfill_segmentation import FloodFillSegmentation

project_root = os.path.dirname(os.path.dirname(__file__))
image_path = os.path.join(project_root, "images", "sample.jpg")

if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found: {image_path}")

image = cv2.imread(image_path)

# WaterShed
watershed_result = WaterShedSegmentation.apply(image.copy())
cv2.imshow("WaterShed", watershed_result)
cv2.waitKey(1500)

# MeanShift
meanshift_result = MeanShiftSegmentation.apply(image.copy())
cv2.imshow("MeanShift", meanshift_result)
cv2.waitKey(1500)

# FloodFill
floodfill_result = FloodFillSegmentation.apply(image.copy(), seed_point=(50, 50))
cv2.imshow("FloodFill", floodfill_result)
cv2.waitKey(3000)

cv2.destroyAllWindows()