from mindstorms import *
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# Initialize the Remote API client and connect to the simulation
client = RemoteAPIClient()
sim = client.require("sim")

# Get handles for the motors and color sensor
left_motor = Motor(sim, DeviceNames.MOTOR_LEFT_LINE, Direction.CLOCKWISE)
right_motor = Motor(sim, DeviceNames.MOTOR_RIGHT_LINE, Direction.CLOCKWISE)
color_sensor = ImageSensor(sim, DeviceNames.IMAGE_SENSOR_LINE)

# PID controller parameters
Kp = 0.10
Ki = 0.012
Kd = 0.04
defaultSpeed = 3

# Initialize error tracking for PID controller
errorList = [0]

#Checks if the red color is detected by calculating the relative intensity 
#of the red channel compared to the green and blue channels.
def is_red_detected(color_sensor):

    red_ratio_threshold = 1.5
    red, green, blue = color_sensor.rgb()
    print(" Red", red, " Green", green, " Blue", blue)
    red_intensity = red / (green + blue)

    return red_intensity > red_ratio_threshold

#Checks if the blue color is detected by calculating the relative intensity 
#of the blue channel compared to the red and green channels.
def is_blue_detected(color_sensor):

    blue_ratio_threshold = 1.5
    red, green, blue = color_sensor.rgb()
    blue_intensity = blue / (red + green)

    return blue_intensity > blue_ratio_threshold

#Simple line following algorithm using the color sensor.
def follow_line(color_sensor, left_motor, right_motor):

    # Update the sensor image
    color_sensor._update_image()  

    # Get reflection value
    reflection = color_sensor.reflection()  
    
    # Midpoint between black and white
    threshold = 40  

    # Calculate error from the threshold
    error = reflection - threshold

    # Get correction from PID controller
    out = PID_Controller(error)

    # Track error for PID after computing PID to use the current error for the derivative calculation
    errorList.append(error)

    # Adjust motor speeds based on PID output
    left_motor.run(defaultSpeed - out)
    right_motor.run(defaultSpeed + out)

#Computes the PID controller output based on the current error.
def PID_Controller(error):
    
    # Proportional term
    P = P_Controller(error, Kp)

    # Integral term
    I = I_Controller(Ki) 

    # Derivative term
    D = D_Controller(error, Kd)  

    # Combine P, I, and D
    output = P + I + D  

    # Print P, I, D, and error for debugging
    print(f"Error: {error}, P: {P}, I: {I}, D: {D}")

    return output

#Computes the proportional term of the PID controller
def P_Controller(error: float, Kp: float):
    error = error * Kp
    return error

#Computes the integral term of the PID controller
def I_Controller(Ki: float):
    error = sum(errorList) * Ki
    return error

#Computes the derivative term of the PID controller
def D_Controller(error, Kd: float):
    error = (error - errorList[-1]) * Kd if len(errorList) > 1 else 0
    return error

# Starts the CoppeliaSim simulation if not already running
sim.startSimulation()

# Main control loop for following the line
while True:
    try:
        follow_line(color_sensor, left_motor, right_motor)

    except KeyboardInterrupt:
        print("Stopping simulation.")
        sim.stopSimulation()
