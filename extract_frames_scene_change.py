import cv2
import os
import sys
import numpy as np

def extract_frames_scene_change(video_path, output_folder, threshold):
    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number = 0

    os.makedirs(output_folder, exist_ok=True)

    ret, prev_frame = video.read()
    if not ret:
        print("Could not read the first frame")
        sys.exit(1)

    prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_diff = cv2.absdiff(frame_gray, prev_frame_gray)

        mean_diff = np.mean(frame_diff)
        if mean_diff > threshold:
            output_path = os.path.join(output_folder, f'frame_{frame_number:04d}.jpg')
            cv2.imwrite(output_path, frame)
            print(f'Saved frame {frame_number}/{total_frames} to {output_path}')

        prev_frame_gray = frame_gray
        frame_number += 1

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python extract_frames_scene_change.py <video_path> <output_folder> <threshold>")
        sys.exit(1)

    video_path = sys.argv[1]
    output_folder = sys.argv[2]
    threshold = float(sys.argv[3])

    extract_frames_scene_change(video_path, output_folder, threshold)
