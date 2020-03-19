import numpy as np
from sklearn.cluster import KMeans as km
import cv2 as cv

class KMeans:
    def __init__(self, n_clusters=2, visualise=False):
        self.n_clusters = n_clusters
        self.visualise = visualise

    def fit(self, original_image, segmented_image):
        self.original_image = original_image
        self.segmented_image = segmented_image
        self.groups = np.unique(self.segmented_image[self.segmented_image!=-1])
        self.flat_segments = np.reshape(self.segmented_image, (-1))
        self.flat_image = np.reshape(self.original_image, (-1, 3))

        # Extracting objects from image
        objects = []
        for group in self.groups:
            object = self.flat_image[self.flat_segments==group]
            objects.append(object)

        # Constructing features from objects
        features = np.zeros((len(objects), 3))
        for i, object in enumerate(objects):
            max = np.max(object)
            min = np.min(object)
            mean = np.mean(object)
            features[i] = [max, min, mean]

        self.group_counts = np.array(self.n_clusters)

        kmeans = km(n_clusters=self.n_clusters, random_state=0).fit(features)
        labels = kmeans.labels_

        labelled_image = np.zeros(self.flat_segments.shape[0])

        for i, group in enumerate(self.groups):
            labelled_image[self.flat_segments==group]=labels[i]

        labelled_image = np.reshape(labelled_image, self.segmented_image.shape)

        if self.visualise:
            cv.imshow("Clustered image", labelled_image)
            cv.waitKey(0)
            cv.destroyWindow("Clustered image")

        return labelled_image
