import sys
from slice_scene import slice_scene
from slice_interval import slice_interval

def main():
    if len(sys.argv) != 5:
        print("Usage: python frame_slice.py <mode> <video_path> <output_folder> <threshold_or_interval>")
        print("Modes: interval, scene")
        sys.exit(1)

    mode = sys.argv[1]
    video_path = sys.argv[2]
    output_folder = sys.argv[3]
    param = float(sys.argv[4])

    if mode == 'interval':
        slice_interval(video_path, output_folder, int(param))
    elif mode == 'scene':
        slice_scene(video_path, output_folder, param)
    else:
        print("Invalid mode. Choose 'interval' or 'scene'.")
        sys.exit(1)

if __name__ == '__main__':
    main()
