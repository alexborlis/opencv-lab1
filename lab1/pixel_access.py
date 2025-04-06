class PixelAccessor:
    @staticmethod
    def get_pixel(image, x, y):
        return image[y, x]