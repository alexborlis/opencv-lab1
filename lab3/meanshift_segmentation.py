from skimage import segmentation, color
from skimage.util import img_as_ubyte
import cv2

class MeanShiftSegmentation:
    @staticmethod
    def apply(image):
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        segments = segmentation.quickshift(img_rgb, kernel_size=3, max_dist=6, ratio=0.5)
        segmented = color.label2rgb(segments, img_rgb, kind='avg')
        return cv2.cvtColor(img_as_ubyte(segmented), cv2.COLOR_RGB2BGR)