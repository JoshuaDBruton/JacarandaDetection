# JacarandaDetection

This repository aims to implement some traditional approaches to object-based image analysis (OBIA) to detect Jacaranda trees (a genus not indigenous to South Africa) in Johannesburg, South Africa. The purpose of this is to construct a basic foundation on which I may improve upon over the course of my MSc. Computer Science degree at the University of the Witwatersrand.

## Dataset
I will be using a single satellite image obtained from Google Earth Pro (now free) as a test-bed:
![satellite-image](https://raw.githubusercontent.com/JoshuaDBruton/JacarandaDetection/master/static/map.jpg)

This satellite image covers an area of approximately 20km<sup>2</sup> in Johannesburg, spanning from Emmarentia dam (centre-left) to Rosebank Mall (top-right). The image is 4800x2886 pixels (the maximum Google Earth allows). The image was captured on the morning of the 18th of November 2017. This is an effective date given that Jacarandas typically exhibit their noticeable purple bloomage from mid-October to mid-November. The image follows the DigitalGlobe-Standard and has a pixel resolution of atleast 0.6m; which is appropriate for use in OBIA.
