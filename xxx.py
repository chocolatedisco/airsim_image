import airsim
import cv2
import numpy as np
import os
import setup_path
import time

# connect to the AirSim simulator
client = airsim.CarClient()
client.confirmConnection()

def save_image(client, camera_list, iter):
    for camera in camera_list:
        if not os.path.exists('c:/temp/{}'.format(camera)):
            os.makedirs('c:/temp/{}'.format(camera))
    #client.simGetImagesでやるとよいかも
    for camera in camera_list:
        filename = 'c:/temp/{}/{}'.format(camera, str(iter))
        png_image = client.simGetImage(camera, airsim.ImageType.Scene)
        airsim.write_file(os.path.normpath(filename+".png"),png_image)
    #time.sleep(0.033)

camera_list = ["ff"]

for i in range(30):
    save_image(client,camera_list,i)

#restore to original state
client.reset()
