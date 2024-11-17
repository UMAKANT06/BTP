import os
import cv2
import time


def create_images_from_camera(parent_dir=None, frame_interval=1):
    """
    Capture frames from the camera in real-time at specified intervals and save them as images.
    :param parent_dir: Directory to save the images in
    :param frame_interval: Time interval (in seconds) between capturing frames
    :return: None
    """
    save_dir = parent_dir if parent_dir else "camera_frames"
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)
    else:
        print(f"***** NOTE: Directory '{save_dir}' already exists. New frames will be added. *****")
    
    cap = cv2.VideoCapture(0)  # Open default camera (0)
    frame_number = 0

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    last_frame_time = time.time()

    while True:
        success, frame = cap.read()
        if not success:
            print("Failed to capture frame from camera. Exiting...")
            break

        current_time = time.time()
        if current_time - last_frame_time >= frame_interval:
            # Save the frame as a JPEG file
            cv2.imwrite(os.path.join(save_dir, f"frame_{frame_number}.jpg"), frame)
            frame_number += 1
            last_frame_time = current_time

        cv2.imshow('Camera Feed', frame)  # Display the camera feed (optional)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Save images to the specified directory and capture one frame every 2 seconds
    create_images_from_camera("/home/umakant/Documents/BTP/test/camera_images", frame_interval=2)
