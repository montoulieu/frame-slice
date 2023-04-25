
# Frame-Slice

Frame-Slice is a Python utility for extracting frames from video files based on two different methods: scene change detection and fixed frame intervals. It leverages the OpenCV library to process video files and export frames as images.

## Features

- **Scene Change Detection**: Extract frames when a significant change in the scene is detected, using a configurable threshold.
- **Fixed Frame Intervals**: Extract frames at regular intervals, specified by a frame interval value.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/montoulieu/frame-slice.git
   ```

2. Change to the `frame-slice` directory:

   ```
   cd frame-slice
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   Note: It is recommended to use a virtual environment to prevent conflicts with other installed Python packages.

## Usage

Run the `frame_slice.py` script with the desired mode, video path, output folder, and threshold or frame interval:

- For scene change mode:

  ```
  python frame_slice.py scene <video_path> <output_folder> <threshold>
  ```

- For interval mode:

  ```
  python frame_slice.py interval <video_path> <output_folder> <frame_interval>
  ```

Replace `<video_path>` with the path to the video file, `<output_folder>` with the path to the folder where the extracted frames will be saved, `<threshold>` with the scene change detection threshold, and `<frame_interval>` with the number of frames between extracted frames in interval mode.

## Examples

Using the provided `test.mp4` video in the `/video` folder, you can test the utility by extracting frames to the `/output/test` folder:

- For scene change mode:

  ```
  python frame_slice.py scene video/test.mp4 output/test 30
  ```

- For interval mode:

  ```
  python frame_slice.py interval video/test.mp4 output/test 1000
  ```

## License

This project is licensed under the [MIT License](LICENSE).