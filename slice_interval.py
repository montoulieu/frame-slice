# Import the necessary libraries
import cv2
import os


def slice_interval(video_path, output_folder, frame_interval):
    # Load the video at the specified path
    video = cv2.VideoCapture(video_path)

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Initialize the frame number to zero
    frame_number = 0

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop until there are frames left in the video
    while video.isOpened():
        # Read the next frame from the video
        ret, frame = video.read()

        # If there are no more frames left, exit the loop
        if not ret:
            break

        # If the current frame number is a multiple of the interval,
        # then save the frame to the output folder
        if frame_number % frame_interval == 0:
            output_path = os.path.join(output_folder, f'frame_{frame_number:04d}.jpg')
            cv2.imwrite(output_path, frame)
            print(f'Saved frame {frame_number}/{total_frames} to {output_path}')

        # Increment the frame number
        frame_number += 1

    # Release the video
    video.release()

    # Close all windows
    cv2.destroyAllWindows()
