import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class Watershed:
    def __init__(self, image):
        # Getting image information
        self.image = np.array(image)
        self.width = self.image.shape[1]
        self.height = self.image.shape[0]
        self.channels = self.image.shape[2]

        # Convert image to greyscale
        self.grey_image = cv.cvtColor(self.image, cv.COLOR_RGB2GRAY)

    def watershed(self, visualise=False, binary_thresh=True):
        if visualise:
            cv.imshow("Grey scale", self.grey_image)
            cv.waitKey(0)
            cv.destroyWindow("Grey scale")
        # Using otsu, threshold image (sometimes into binary image)
        if binary_thresh:
            ret, thresh = cv.threshold(self.grey_image, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
        else:
            ret, thresh = cv.threshold(self.grey_image, 0, 255, cv.THRESH_OTSU)

        if visualise:
            cv.imshow("Thresholded image", thresh)
            cv.waitKey(0)
            cv.destroyWindow("Thresholded image")

        # Remove noise
        kernel = np.ones((3, 3), np.uint8)
        opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)

        # Find sure background
        sure_bg = cv.dilate(opening, kernel, iterations=3)

        # Find sure foreground
        dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
        ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

        # Find unsure region
        sure_fg = np.uint8(sure_fg)
        unknown = cv.subtract(sure_bg,sure_fg)

        if visualise:
            fig = plt.figure()
            _, ax = plt.subplots(1, 3)
            ax[0].set_title("Sure background")
            ax[0].imshow(sure_bg, cmap="gray")
            ax[1].set_title("Sure foreground")
            ax[1].imshow(sure_fg, cmap="gray")
            ax[2].set_title("Unknown")
            ax[2].imshow(unknown, cmap="gray")
            for a in ax:
                a.axis("off")
            plt.draw()
            plt.waitforbuttonpress(0)
            plt.close()

        # Label markers
        ret, markers = cv.connectedComponents(sure_fg)

        # add 1 so that background is one (unknown will be 0)
        markers = markers+1

        # Make unknown 0
        markers[unknown==255] = 0

        if visualise:
            markersC = cv.applyColorMap(markers.astype(np.uint8), cv.COLORMAP_JET)
            cv.imshow("Markers", markersC)
            cv.waitKey(0)
            cv.destroyWindow("Markers")

        # Finish
        markers = cv.watershed(self.image, markers)

        # Image with borders
        border_image = self.image.copy()
        border_image[markers==-1] = [255, 0, 0]

        if visualise:
            fig = plt.figure()
            _, ax = plt.subplots(1, 2)
            ax[0].set_title("Final markers")
            ax[0].imshow(markers)
            ax[1].set_title("Image with borders")
            ax[1].imshow(border_image)
            for a in ax:
                a.axis("off")
            plt.draw()
            plt.waitforbuttonpress(0)
            plt.close()

        return markers, border_image
