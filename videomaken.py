#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:19:31 2023

@author: a144895
"""

import cv2
import os

folder_path = "/Users/a144895/Library/Mobile Documents/com~apple~CloudDocs/Developer/python/NatNTC/cWFrames"
output_video_path = "cWVideo.avi"

# a sorted list of all frames in the folder
frames = [f for f in os.listdir(folder_path) if f.endswith('.png')]
frames.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

# Get the dimensions of the first frame
first_frame_path = os.path.join(folder_path, frames[0])
first_frame = cv2.imread(first_frame_path)
height, width, _ = first_frame.shape

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fps = 30  # Frames per second
output_video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Loop over each frame and write it to the video
for frame_name in frames:
    frame_path = os.path.join(folder_path, frame_name)
    try:
        frame = cv2.imread(frame_path)
        output_video.write(frame)
    except Exception as e:
        print(f"Error processing frame {frame_name}: {str(e)}")

# Release the video writer and close the video
output_video.release()
cv2.destroyAllWindows()

print("Video klaar!")
