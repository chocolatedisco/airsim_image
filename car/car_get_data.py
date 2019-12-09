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

parking_list = [
    {
    "X": 100,
    "Y": 100,
    "Z": 100,
    "Pitch": 0,
    "Roll": 0,
    "Yaw": 180
    }
]
camera_list = []
control_list = [[0.5,0],[0.5,1]]

for parking in parking_list:
    print(parking_list)
    client.moveToPosition(100, 100, 100, 5, max_wait_seconds = 60, drivetrain = 0, yaw_mode = airsim.YawMode(), lookahead = -1, adaptive_lookahead = 1)
    # client.simSetVehiclePose(parking, True, vehicle_name = 'PhysXCar')
    time.sleep(300)
    # for control in control_list:
    #     get_data(parking, control)

#restore to original state
client.reset()

client.enableApiControl(False)
