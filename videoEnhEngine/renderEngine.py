import cv2
import numpy as np
from scipy.signal import butter, filtfilt
import IO
import pylab
from lib.processors_noopenmdao import findFaceGetPulse  # Import required class from lib module

# Function to amplify temporal variations with enhanced color visualization
# def amplify_temporal_variations(frame, factor):
#     # Apply temporal filtering (butterworth bandpass filter)
#     # Modify these parameters as needed
#     lowcut = 0.8
#     highcut = 1.9
#     fps = 30.0
#     nyquist = 0.5 * fps
#     low = lowcut / nyquist
#     high = highcut / nyquist

#     # Use scipy.signal.butter for temporal filtering
#     b, a = butter(2, [low, high], btype='band')
#     filtered_frame = filtfilt(b, a, frame, axis=0)

#     # Amplify temporal variations
#     amplified_frame = frame + factor * filtered_frame

#     # Clip values to valid range (0-255)
#     amplified_frame = np.clip(amplified_frame, 0, 255)

#     # Enhance color saturation for visualization
#     amplified_frame = cv2.convertScaleAbs(amplified_frame, alpha=1.5, beta=0)

#     # Apply dynamic color mapping for better visualization
#     amplified_frame = cv2.applyColorMap(amplified_frame, cv2.COLORMAP_JET)

#     return amplified_frame

if __name__ == "__main__":
    # Read input video file
    cap = cv2.VideoCapture(IO.inputFile)

    # Get input video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create VideoWriter object for output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(IO.outputFile, fourcc, fps, (width, height))

    # Amplification factor (adjust as needed)
    factor = 20

    # Initialize the frame processor
    processor = findFaceGetPulse(bpm_limits=[50, 160], data_spike_limit=2500, face_detector_smoothness=10)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame using the frame processor with enhanced visualization
        processed_frame = amplify_temporal_variations(frame, factor)

        # Write processed frame to output video
        out.write(processed_frame)

    # Release video capture and writer objects
    cap.release()
    out.release()
    cv2.destroyAllWindows()
