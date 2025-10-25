import cv2
import numpy as np
import os

def generate_frames(video_name: str):
    output_dir = "video_frames"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    vidcap = cv2.VideoCapture(video_name)

    success, image = vidcap.read()
    frame = 0
    while success:
        frame_filename = os.path.join(output_dir, f"frame_{frame}.png")
        cv2.imwrite(frame_filename, image)
        frame += 1
        success, image = vidcap.read()

    vidcap.release()
    print(f"Extracted {frame} frames to {output_dir}")


def img_to_matrix(image_path: str):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error: image not found! (Path: {image_path})")

    return image

def print_matrix(matrix):
    for i in range(0, len(matrix)):
        line = ""
        for j in range(0, len(matrix[i])):
            if matrix[i][j] > 200:
                line += '\u2588'
            else:
                line += ' '
        print(line)