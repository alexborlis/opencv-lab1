# main.py
# Запуск кожного прикладу з лабораторної роботи №1 по черзі

from lab1.read_image import ImageReader
from lab1.show_image import ImageDisplayer
from lab1.save_image import ImageSaver
from lab1.pixel_access import PixelAccessor
from lab1.crop_image import ImageCropper
from lab1.resize_image import ImageResizer
from lab1.rotate_image import ImageRotator
from lab1.blur_image import ImageBlurrer
from lab1.draw_shapes import ShapeDrawer
from lab1.add_text import TextAdder

import os
import cv2

image_path = "images/sample.jpg"
save_path = "images/output.jpg"

# 1. Зчитування зображення
print("1. Зчитування зображення")
image = ImageReader.read_image(image_path)

# 2. Відображення зображення
print("2. Відображення зображення")
cv2.imshow("Original", image)
cv2.waitKey(3000)  # авто-закриття через 3 секунди
cv2.destroyAllWindows()

# 3. Збереження зображення
print("3. Збереження зображення")
ImageSaver.save_image(save_path, image)

# 4. Доступ до пікселя
print("4. Доступ до пікселя")
pixel = PixelAccessor.get_pixel(image, 50, 100)
print(f"Піксель [100, 50]: {pixel}")

# 5. Вирізання зображення
print("5. Вирізання зображення")
cropped = ImageCropper.crop(image, 50, 50, 200, 200)
cv2.imshow("Cropped", cropped)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# 6. Зміна розміру
print("6. Зміна розміру")
resized = ImageResizer.resize(image, 300, 300)
cv2.imshow("Resized", resized)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# 7. Поворот зображення
print("7. Поворот зображення")
rotated = ImageRotator.rotate(image, 45)
cv2.imshow("Rotated", rotated)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# 8. Розмивання зображення
print("8. Розмивання зображення")
blurred = ImageBlurrer.blur(image)
cv2.imshow("Blurred", blurred)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# 9. Малювання фігур
print("9. Малювання фігур")
rect_img = ShapeDrawer.draw_rectangle(image, (30, 30), (200, 200), (0, 255, 0), 2)
line_img = ShapeDrawer.draw_line(rect_img, (0, 0), (300, 300), (255, 0, 0), 2)
circle_img = ShapeDrawer.draw_circle(line_img, (150, 150), 50, (0, 0, 255), 2)
cv2.imshow("Shapes", circle_img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# 10. Додавання тексту
print("10. Додавання тексту")
text_img = TextAdder.put_text(image, "OpenCV Lab", (50, 50))
cv2.imshow("Text", text_img)
cv2.waitKey(3000)
cv2.destroyAllWindows()
