from mindstorms import *
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import time

client = RemoteAPIClient()
sim = client.require("sim")

# HANDLES FOR ACTUATORS AND SENSORS
robot = Robot_OS(sim, DeviceNames.ROBOT_OS)

top_image_sensor = ImageSensor(sim, DeviceNames.TOP_IMAGE_SENSOR_OS)
small_image_sensor = ImageSensor(sim, DeviceNames.SMALL_IMAGE_SENSOR_OS)

left_motor = Motor(sim, DeviceNames.MOTOR_LEFT_OS, Direction.CLOCKWISE)
right_motor = Motor(sim, DeviceNames.MOTOR_RIGHT_OS, Direction.CLOCKWISE)

defaultSpeed = 6

# between 0 and 40
sonarThreshold = 0.3

#setting global variables
last_detected_color = None
color_is_detected = False

# FUNCTIONS HERE


def center(image_data, region_size=8):
    start = (image_data.shape[0] - region_size) // 2
    end = start + region_size
    return image_data[start:end, start:end]

def avoid_wall():
    sonar_value = robot.get_sonar_sensor()
    if sonar_value < sonarThreshold:
        object_color = detect_block_color()
        if object_color in ["red", "green", "yellow", "blue"]:
            left_motor.run(defaultSpeed)
            right_motor.run(defaultSpeed)
        else:
            wall_color = detect_wall_color()
            if wall_color in ["wall_dark", "wall_light"]:
                left_motor.run(-1)
                right_motor.run(defaultSpeed)
            else:
                left_motor.run(defaultSpeed)
                right_motor.run(defaultSpeed)
    else:
        left_motor.run(defaultSpeed)
        right_motor.run(defaultSpeed)

# battery monitor
def battery(sensor_data):
    try:
        # b'0.99994973689502'
        battery_level = float(((robot.get_battery())).split("'")[1])
        critical_level = 10

        if battery_level < critical_level:
            #navigate_to_charging_pad(sensor_data)
            print("navigate to charging pad")
    except:
        print("something went wrong whily trying to read battery lvl")

def detect_wall_color():
    global last_detected_color, color_is_detected

    colors_top = {
        "wall_dark": (np.array([130, 130, 153]), 20),
        "wall_light": (np.array([152, 148, 172]), 20)
    }
    
    center_top_image_data = center(top_image_data)
    
    for color_name, (color_value, tolerance) in colors_top.items():
        mask = np.all(np.abs(center_top_image_data - color_value) <= tolerance, axis=-1)
        if np.any(mask):
            if last_detected_color != color_name or not color_is_detected:
                print(f"{color_name} color detected! (top sensor)")
                last_detected_color = color_name
                color_is_detected = True
            return color_name
    
    if color_is_detected:
        print("no color detected (top sensor)")
        color_is_detected = False
    return None

def detect_block_color():
    global last_detected_color, color_is_detected

        # "yellow": (np.array([255, 255, 21]), 20)
        # "blue": (np.array([0, 128, 128]), 20)
        # "red": (np.array([139, 0, 0]), 20)

    colors_small = {
        "light_green": (np.array([0, 153, 0]), 30),
        "dark_green": (np.array([64, 172, 20]), 30),
        "dark_brown": (np.array([104, 44, 12]), 30),
        "light_brown": (np.array([136, 36, 12]), 30)
    }
    
    center_small_image_data = center(small_image_data)
    
    for color_name, (color_value, tolerance) in colors_small.items():
        mask = np.all(np.abs(center_small_image_data - color_value) <= tolerance, axis=-1)
        if np.any(mask):
            if last_detected_color != color_name or not color_is_detected:
                print(f"{color_name} color detected! (small sensor)")
                last_detected_color = color_name
                color_is_detected = True
            return color_name
    
    if color_is_detected:
        print("no color detected (small sensor)")
        color_is_detected = False
    return None

def find_block():

    print("Searching for block...")

    while True:

        block_color = detect_block_color()
        left_motor.run(-defaultSpeed/16)
        right_motor.run(defaultSpeed/16)

        if block_color != None:
            break

    print(f"Block of color {block_color} found! Driving towards it.")
    
    left_motor.run(defaultSpeed)
    right_motor.run(defaultSpeed)

# HELPER FUNCTION
def show_image(image):
    plt.imshow(image)
    plt.show()

# Starts coppeliasim simulation if not done already
sim.startSimulation()

# MAIN CONTROL LOOP
while True:
    try:
        # update top image sensor
        top_image_sensor._update_image()
        top_image_data = top_image_sensor.image

        # update small image sensor
        small_image_sensor._update_image()
        small_image_data = small_image_sensor.image

        # subsumption functions calling
        avoid_wall()
        detect_wall_color()
        detect_block_color()
        #battery(top_image_data)
        find_block()

    except KeyboardInterrupt:
        print("Stopping simulation.")
        sim.stopSimulation()
