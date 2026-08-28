import sim
import matplotlib.pyplot as plt
from mindstorms import Motor, Direction, ColorSensor
import numpy as np


sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

#I= sumErr * Ki
#D = (error-lasterror)*Kd
Kp = 0.6
Ki = 0
Kd = 0.3
defaultSpeed = 3
ErrorData = [0]
ErrorTime = [0]


def show_image(image):
    plt.imshow(image)
    plt.show()


def is_red_detected(color_sensor):
    """
    Calculates the relative intensity of the red channel compared to
    other channels
    """
    red_ratio_threshold = 1.5   
    red, green, blue = color_sensor.rgb()
    print(" Red", red, " Green" , green," Blue" , blue)
    red_intensity = red / (green + blue)

    return red_intensity > red_ratio_threshold


def is_blue_detected(color_sensor):
    """
       Calculates the relative intensity of the blue channel compared to
       other channels
       """
    blue_ratio_threshold = 1.5
    red, green, blue = color_sensor.rgb()
    blue_intensity = blue / (red + green)

    return blue_intensity > blue_ratio_threshold


def follow_line(color_sensor, left_motor, right_motor):
    """
    A very simple line follower that should be improved.
    """
    color_sensor.image = color_sensor._get_image_sensor()
    reflection = color_sensor.reflection()
    threshold = 40  # Midpoint between black and white
    turnThreshold = 24
    BL, BR, TL, TR = splitSensor(color_sensor.image)
    global currentError; 
    currentError = (BL + BR + TL + TR)/100
    # print("BL: " , BL)
    # print("BR: " , BR)
    # print("TL: " , TL)
    # print("TR: " , TR)
    print(currentError)
    if BL < turnThreshold and BR < turnThreshold and TL < turnThreshold and TR < turnThreshold:
        left_motor.run(3)
        right_motor.run(3)
        ErrorData.append(currentError)
        ErrorTime.append(ErrorTime[-1] + 1)

    else:
        if TR > turnThreshold:
            if TR > TL:
                Error = PID_Controller(currentError)
                print("PID: " , Error)
                left_motor.run(-1 * Error)
                right_motor.run(3 * Error)

                ErrorData.append(Error)
                ErrorTime.append(ErrorTime[-1] + 1)
            #else:

        elif TL > turnThreshold:
            if TL > TR:
                Error = PID_Controller(currentError)
                print("PID: ", Error)
                left_motor.run(3 * Error)
                right_motor.run(-1 * Error)

                ErrorData.append(Error)
                ErrorTime.append(ErrorTime[-1] + 1)

            #else:
    

def PID_Controller(Error):
    P = P_Controller(Error, Kp)
    print("P: " ,P)
    #I = I_Controller(ErrorI, Ki)
    D = D_Controller(Error, Kd)
    controlOutput = P + D 
    return controlOutput

def P_Controller(ErrorInput : float, Kp : float ):
    if Kp > 2 or Kp < 0:
        raise "Invalid Gain, Gain has to be set between 0 and 2 (float)"
    newError = ErrorInput *Kp
    return newError

def I_Controller(ErrorInput , Ki : float):
    if Ki > 2 or Ki < 0:
        raise "Invalid Gain, Gain has to be set between 0 and 2 (float)"
    #I_output = Ki * intgrl(curErr * dt)
    ErrorInput = ErrorInput[-6 : -1]
    print("INTEGRAL ARRAY: " ,ErrorInput)
    #ErrorInput = np.array(ErrorInput)
    NewError = np.trapz(ErrorInput, x=None, dx=1.0, axis=-1)
    #NewError = NewError * Ki
    print("I: ",NewError)
    return NewError

def D_Controller(ErrorInput , Kd : float):
    if Kd > 2 or Kd < 0:
        raise "Invalid Gain, Gain has to be set between 0 and 2 (float)"
    newError = (ErrorInput - ErrorData[-1]) * Kd
    return newError

def splitSensor(ImageArr):
    Left_Bottom = []
    Left_Top = []
    Right_Bottom = []
    Right_Top = []
    for i in range(ImageArr.shape[1]):
        #print(Arr) #left part of sensor is bottom half of image array
        
        CurArr = ImageArr[i]
        
        
        Right_Sensor_Bottom = CurArr[0:7][0:3]
        Left_Sensor_Bottom = CurArr[8:16][0:3]

        Right_Sensor_Top = CurArr[0:7][4:8]
        Left_Sensor_Top = CurArr[8:16][4:8]

        Avg_RGB_Left_Bottom = Left_Sensor_Bottom.mean()
        Avg_RGB_Right_Bottom = Right_Sensor_Bottom.mean()
        Avg_RGB_Left_Top = Left_Sensor_Top.mean()
        Avg_RGB_Right_Top = Right_Sensor_Top.mean()

        Left_Bottom.append(Avg_RGB_Left_Bottom)
        Right_Bottom.append(Avg_RGB_Right_Bottom)
        Left_Top.append(Avg_RGB_Left_Top)
        Right_Top.append(Avg_RGB_Right_Top)
    
    Avg_RGB_Left_Bottom = sum(Left_Bottom)/len(Left_Bottom)
    Avg_RGB_Right_Bottom = sum(Right_Bottom)/len(Right_Bottom)

    Avg_RGB_Left_Top = sum(Left_Top)/len(Left_Top)
    Avg_RGB_Right_Top = sum(Right_Top)/len(Right_Top)

    return Avg_RGB_Left_Bottom, Avg_RGB_Right_Bottom, Avg_RGB_Left_Top, Avg_RGB_Right_Top
    

# MAIN CONTROL LOOP
if clientID != -1:

    print('Connected')

    left_motor = Motor(motor_port='A', direction=Direction.CLOCKWISE, clientID=clientID)
    right_motor = Motor(motor_port='B', direction=Direction.CLOCKWISE, clientID=clientID)
    color_sensor = ColorSensor(clientID=clientID)

    while True:
       
        try:
             follow_line(color_sensor,left_motor,right_motor)

        except TypeError:
            print("min: " , min(ErrorData))
            print("max: " , max(ErrorData))
            # plt.plot(ErrorTime , ErrorData )
            # plt.ylabel("Error amount")
            # plt.xlabel("Time (s)")
            # plt.show()
            break
else:
    print('Failed connecting to remote API server')
print('Program ended')

# MAIN CONTROL LOOP