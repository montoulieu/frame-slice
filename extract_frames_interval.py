import cv2
import os
import sys

def extract_frames_interval(video_path, output_folder, frame_interval):
    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number = 0

    os.makedirs(output_folder, exist_ok=True)

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        if frame_number % frame_interval == 0:
            output_path = os.path.join(output_folder, f'frame_{frame_number:04d}.jpg')
            cv2.imwrite(output_path, frame)
            print(f'Saved frame {frame_number}/{total_frames} to {output_path}')

        frame_number += 1

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python extract_frames_interval.py <video_path> <output_folder> <frame_interval>")
        sys.exit(1)

    video_path = sys.argv[1]
    output_folder = sys.argv[2]
    frame_interval = int(sys.argv[3])

    extract_frames_interval(video_path, output_folder, frame_interval)
v