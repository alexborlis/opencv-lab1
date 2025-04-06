class ImageCropper:
    @staticmethod
    def crop(image, start_x, start_y, end_x, end_y):
        return image[start_y:end_y, start_x:end_x]