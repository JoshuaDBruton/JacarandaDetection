import cv2 as cv
from segmentation import Watershed
from clustering import KMeans

class OBIA:
    def __init__(self, image_path=None, visualise=False):
        self.visualise = visualise
        if image_path:
            self.image = cv.imread(image_path)
        else:
            raise ValueError("Please provide an image_path")

    def visualise_image(self):
        cv.imshow('Original', self.image)
        cv.waitKey(0)
        cv.destroyWindow('Original')

    def segment_image(self, algorithm="ws", binary_thresh=False):
        if algorithm == "ws":
            ws = Watershed(self.image[:,:,::-1])
            self.segments, self.border_image = ws.watershed(visualise=self.visualise, binary_thresh=binary_thresh)

    def cluster_image(self, n_clusters, algorithm="km"):
        if algorithm == "km":
            kmeans = KMeans(n_clusters=n_clusters, visualise=self.visualise)
            self.labelled_image = kmeans.fit(self.image, self.segments)

if __name__=="__main__":
    obia = OBIA(image_path = "data/test.jpg", visualise=True)
    obia.segment_image(algorithm="ws", binary_thresh=False)
    obia.cluster_image(n_clusters=2, algorithm="km")
