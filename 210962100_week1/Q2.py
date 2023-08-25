# Import the OpenCV library
import cv2

# Create a VideoCapture object to read a video file ('resources\\videoplayback.mp4')
video_capture = cv2.VideoCapture('resources\\videoplayback.mp4')

# Check if the video file was opened successfully
if not video_capture.isOpened():
    print("Error opening the video file")

# Loop to read frames from the video and display them until the video ends or the user presses 'q'
while video_capture.isOpened():
    # Read a frame from the video. 'ret' will be True if a frame is successfully read.
    # 'frame' will contain the image data of the current frame.
    ret, frame = video_capture.read()

    # Check if a frame was read successfully
    if ret:
        # Display the current frame in a window titled 'Frame'
        cv2.imshow('Frame', frame)

        # Wait for 45 milliseconds for user input. If the user presses any key during this time, it will be captured as 'key'.
        key = cv2.waitKey(45)

        # If the user presses the 'q' key, break out of the loop to stop displaying the frames.
        if key == ord('q'):
            break
    else:
        # If no frame is read (end of video), break out of the loop.
        break

# Release the VideoCapture object to free up resources
video_capture.release()

# Close all OpenCV windows, in this case, the 'Frame' window.
cv2.destroyAllWindows()
