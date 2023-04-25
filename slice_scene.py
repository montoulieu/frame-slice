# Import the necessary libraries
import cv2
import os
import sys
import numpy as np

def slice_scene(video_path, output_folder, threshold):
    # Load the video at the specified path
    video = cv2.VideoCapture(video_path)

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Initialize a variable to keep track of the current frame
    frame_number = 0

    # Create the output folder if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the first frame
    ret, prev_frame = video.read()
    
    # Check if the frame was read successfully
    if not ret:
        print("Could not read the first frame")
        sys.exit(1)

    # Convert the frame to grayscale
    prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    # Iterate while the video is opened
    while video.isOpened():
        # Read the next frame
        ret, frame = video.read()
        # Check if the frame was read successfully
        if not ret:
            break

        # Convert the frame to grayscale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Get the absolute difference between the current frame and the previous frame
        frame_diff = cv2.absdiff(frame_gray, prev_frame_gray)

        # Get the mean of the absolute difference
        mean_diff = np.mean(frame_diff)
        # Check if the difference is greater than the threshold
        if mean_diff > threshold:
            # Save the frame
            output_path = os.path.join(output_folder, f'frame_{frame_number:04d}.jpg')
            cv2.imwrite(output_path, frame)
            print(f'Saved frame {frame_number}/{total_frames} to {output_path}')

        # Set the previous frame to the current frame
        prev_frame_gray = frame_gray
        # Increment the frame number
        frame_number += 1

    # Release the video capture object and close all windows
    video.release()
    cv2.destroyAllWindows()