import numpy as np
import cv2

input_video = '/Users/saadnaik/Documents/Learning/vitalLenz/input_file.MOV'
output_video = "/Users/saadnaik/Documents/Learning/vitalLenz/ouput_file.mp4"

# Load pre-trained face detection cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read input video file
cap = cv2.VideoCapture(input_video)

# Create VideoWriter object for output video
fourcc = cv2.VideoWriter.fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, 30.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Process each detected face
    for (x, y, w, h) in faces:
        # Extract region of interest (face)
        face_roi = frame[y:y+h, x:x+w]

        # Split face region into RGB channels
        b, g, r = cv2.split(face_roi)

        # Increase red tone sensitivity (example: simple contrast stretching)
        r_enhanced = cv2.equalizeHist(r)

        # Merge enhanced red channel with original face region
        enhanced_face_roi = cv2.merge((b, g, r_enhanced))

        # Replace the original face region with the enhanced version
        frame[y:y+h, x:x+w] = enhanced_face_roi

    # Write processed frame to output video
    out.write(frame)

# Release video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()

print("Running")




