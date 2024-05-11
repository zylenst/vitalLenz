import cv2

def enhance_video(input_file, output_file):
    # Open the input video file
    cap = cv2.VideoCapture(input_file)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

     # Process each frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # TODO: Enhance RGB values to emphasize changes in facial coloration
        
        # Write the enhanced frame to the output video
        out.write(frame)

    # Release the video capture and writer objects
    cap.release()
    out.release()

if __name__ == "__main__":
    input_file = ("Enter input file path: ").strip()
    output_file = ("Enter output file path: ").strip()

    #execution
    enhance_video(input_file, output_file)


