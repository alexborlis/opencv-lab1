import cv2
from lab2.grayscale import GrayscaleConverter
from lab2.brightness import BrightnessAdjuster
from lab2.contrast import ContrastAdjuster
from lab2.histogram_equalization import HistogramEqualizer

image_path = "images/sample.jpg"
image = cv2.imread(image_path)

# 1. Градації сірого
gray = GrayscaleConverter.to_grayscale(image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(1500)

# 2. Підвищення яскравості
bright = BrightnessAdjuster.adjust_brightness(image, 50)
cv2.imshow("Brightness +50", bright)
cv2.waitKey(1500)

# 3. Підвищення контрастності
contrast = ContrastAdjuster.adjust_contrast(image, 1.5)
cv2.imshow("Contrast x1.5", contrast)
cv2.waitKey(1500)

# 4. Вирівнювання гістограми
equalized = HistogramEqualizer.equalize(image)
cv2.imshow("Histogram Equalized", equalized)
cv2.waitKey(3000)

cv2.destroyAllWindows()
