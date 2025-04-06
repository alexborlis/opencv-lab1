import cv2
import os
import matplotlib.pyplot as plt
from lab4.thresholding import ThresholdingProcessor

project_root = os.path.dirname(os.path.dirname(__file__))
image_path = os.path.join(project_root, "images", "sample.jpg")

if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found: {image_path}")

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError("Unable to read image")

# Звичайна порогова обробка
thresh_results = ThresholdingProcessor.apply_all_thresholds(image, 127, 255)

# Метод Отсу
otsu_result = ThresholdingProcessor.apply_otsu(image)

# Візуалізація
titles = ['Original'] + list(thresh_results.keys()) + ['OTSU']
images = [image] + list(thresh_results.values()) + [otsu_result]

plt.figure(figsize=(12, 8))
for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()