'''
Save frames of videos as images and create masks
'''
import glob
import os

import cv2


def create_images_from_video(video_file_path, parent_dir=None):
    """
    Creates and saves images from the video file in the dir with the name of the video file in the parent dir
    :param video_file_path: Path to video file
    :param parent_dir: dir to save the images in
    :return:
    """
    save_dir = parent_dir if parent_dir else video_file_path.split('/')[-2]
    file_name = video_file_path.split('/')[-1].split('.')[0]
    save_path = os.path.join(save_dir, file_name)
    if os.path.isdir(save_path):
        print("***** NOTE:Looks like a saved image dir already exists for:", file_name, "in dir:", save_dir, "*****")
        print("EXITING")
        return
    os.mkdir(save_path)
    video_cap = cv2.VideoCapture(video_file_path)
    frame_number = 0
    while True:
        success, image = video_cap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(save_path, "{}_{:d}.jpg".format(file_name, frame_number)),
                    image)  # save frame as JPEG file
        frame_number += 1


def create_images_for_videos_in_dir(dir_path, save_dir_path):
    """
    Function to create images in save dir path from video files in dir path
    :param dir_path: Path to dir with the video files
    :param save_dir_path: Path to save
    :return:
    """
    if not os.path.isdir(save_dir_path):
        os.mkdir(save_dir_path)
    video_files = glob.glob(os.path.join(dir_path, "*.mp4")) + glob.glob(os.path.join(dir_path, "*.avi"))
    for video_file in video_files:
        create_images_from_video(video_file, save_dir_path)


if __name__ == "__main__":
    create_images_for_videos_in_dir("/home/umakant/Documents/BTP/test/videos",
                                    "/home/umakant/Documents/BTP/test/images")
