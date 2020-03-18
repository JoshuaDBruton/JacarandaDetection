import cv2 as cv
from segmentation import Watershed

class OBIA:
    def __init__(self, image_path=None):
        if image_path:
            self.image = cv.imread(image_path)
        else:
            raise ValueError("Please provide an image_path")

    def visualise_image(self):
        cv.imshow('Original', self.image)
        cv.waitKey(0)
        cv.destroyWindow('Original')

    def segment_image(self, algorithm="ws"):
        if algorithm == "ws":
            ws = Watershed(self.image[:,:,::-1])
            ws.watershed(visualise=True, binary_thresh=False)

if __name__=="__main__":
    obia = OBIA(image_path = "data/map.jpg")
    obia.visualise_image()
    obia.segment_image(algorithm="ws")
