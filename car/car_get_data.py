import airsim
import cv2
import numpy as np
import os
import setup_path
import time

# connect to the AirSim simulator
client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)
car_controls = airsim.CarControls()

    # # go forward
    # car_controls.throttle = 0.5
    # car_controls.steering = 0

    # # Go forward + steer right
    # car_controls.throttle = 0.5
    # car_controls.steering = 1

def save_image(client, camera_list, iter):
    for camera in camera_list:
        if not os.path.exists('c:/temp/{}'.format(camera)):
            os.makedirs('c:/temp/{}'.format(camera))
    #client.simGetImagesでやるとよいかも
    for camera in camera_list:
        filename = 'c:/temp/{}/{}'.format(camera, str(iter))
        png_image = client.simGetImage(camera, airsim.ImageType.Scene)
        airsim.write_file(os.path.normpath(filename+".png"),png_image)
    time.sleep(0.2)

# parking_list = []
camera_list = ["ff","fba","fr","fl","ft","fbo"]
control_list = [[0.5,0]]

for control in control_list:
    car_controls.throttle = control[0]
    car_controls.steering = control[1]
    client.setCarControls(car_controls)
    for i in range(20):
        save_image(client,camera_list,i)
    # time.sleep(10)   # let car drive a bit
    client.reset()

#restore to original state
client.reset()

client.enableApiControl(False)
