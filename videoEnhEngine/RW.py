import cv2
import IO
import numpy as np
from lib.processors_noopenmdao import findFaceGetPulse

# Takes in video
videoIn = cv2.VideoCapture(IO.inputFile)


# Writes Video
videoOut = cv2.VideoWriter(IO.outputFile, cv2.VideoWriter.fourcc(*'mp4v'), int(videoIn.get(cv2.CAP_PROP_FPS)), (int(videoIn.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT))))
