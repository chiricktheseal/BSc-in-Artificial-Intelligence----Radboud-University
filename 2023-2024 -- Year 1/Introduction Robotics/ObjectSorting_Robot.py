#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:27:53 2024

@author: maria
"""

from hub import light_matrix, motion_sensor, port
import runloop
import color_sensor
import distance_sensor
import motor
import motor_pair
import random
import color

field = 0
field_red_cubes = 0
speed = 150
reflection_threshold = 40


def line_detected():
    global reflection_threshold
    if color_sensor.reflection(port.C) > reflection_threshold:
        return True
    return False
    
def cross_line():
    while line_detected():
        motor_pair.move(motor_pair.PAIR_1, 0, velocity=speed)

def cross_line_allowed():
    global field

    # Robot in field 0 and facing in the direction of field 1 -> cross line and update field
    if (field == 0 and motion_sensor.tilt_angles()[0] < 20 and motion_sensor.tilt_angles()[0] > -20):
        return True
    
    # Robot in field 1 and facing in the direction of field 0 -> cross line and update field
    elif (field == 1 and motion_sensor.tilt_angles()[0] < -1780 or motion_sensor.tilt_angles()[0] > 1780):
        return True
    
    else:
        return False

def update_field():
    global field
    field = abs(field - 1)


def object_in_distance():
    if (distance_sensor.distance(port.A) < 100 and distance_sensor.distance(port.A) > -1): # check the port for the distance sensor
        return True
    return False

def object_collected():
    if (distance_sensor.distance(port.A) < 50 and distance_sensor.distance(port.A) > -1): # check the port for the distance sensor
        return True
    return False


async def needs_sorting():
    global field_red_cubes
    global field

    # Cube is red but not on the red side
    if (color_sensor.color(port.E) is color.RED and field_red_cubes != field):
        return True
    
    # Cube is blue but on the red side
    elif (color_sensor.color(port.E) is color.BLUE and field_red_cubes == field):
        return True
    
    # Cube is on the right side
    else:
        return False

async def go_to_field():
    global field

    current_field = field
    while (field != current_field):
        motor_pair.move(motor_pair.PAIR_1, 0)

async def move_away():
    global speed

    motor_pair.move_for_degrees(motor_pair.PAIR_1, -90, 0)
    random_degrees = random.randint(10, 20)
    motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, random_degrees, speed, -speed)


async def face_goal_field():
    global field

    if (field == 0):
        # if the degrees are smaller than 0, make a counterclockwise turn until it is larger than 0
        if motion_sensor.tilt_angles()[0] < 0:
            while motion_sensor.tilt_angles()[0] < 0:
                motor_pair.move(motor_pair.PAIR_1, -100) # counterclockwise turn
        # if the degrees are larger than 0, make a clockwise turn
        else:
            while motion_sensor.tilt_angles()[0] > 0:
                motor_pair.move(motor_pair.PAIR_1, 100) # clockwise turn
    
    else:
        # if the degrees are smaller than 0, make a clockwise turn until it is positive
        if motion_sensor.tilt_angles()[0] < 0:
            while motion_sensor.tilt_angles()[0] < 0:
                motor_pair.move(motor_pair.PAIR_1, 100) # clockwise turn
        # if the degrees are larger than 0, make a counterclockwise turn until they are smaller than 0
        else:
            while motion_sensor.tilt_angles()[0] > 0:
                motor_pair.move(motor_pair.PAIR_1, -100) # counterclockwise turn


# Layer One: Robot moves in the field
async def move_around():
    global speed

    # Check if an object is seen and if so, trigger new level: drive_to_cubes()
    if object_in_distance(): 
        drive_to_cubes()

    if line_detected():
        print("line detected, yaw at:", motion_sensor.tilt_angles()[0])

        if cross_line_allowed():
            #print(field)
            cross_line()
            update_field()
            #print(field)
        
        # Robot in either field but not facing the other one -> do not cross line but turn clockwise until no line detected
        else:
            #print("in else")
            while line_detected():
                motor_pair.move(motor_pair.PAIR_1, 100)

            # move some additional degrees and make sure no line is crossed when doing this
            counter = 0
            while True:
                #print("in here")
                random_degrees = random.randint(50, 150)
                #print(random_degrees)
                await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, random_degrees, speed, -speed)
                #print(counter)
                counter += 1
                if (not line_detected()):
                    print("no line anymore")
                    break
                else:
                    continue
            
    else:
        motor_pair.move(motor_pair.PAIR_1, 0, velocity=speed)


# Layer Two: Robot drives towards a cube
def drive_to_cubes():
    global speed
    #print("In drive_to_cubes function")
    while object_in_distance():

        if object_collected():
            sort_cubes()
            break

        # check if a line is detected
        if line_detected():

            # if you are allowed to cross the line, cross the line
            if cross_line_allowed():
                cross_line()
                update_field()
            # if you are not allowed to cross the line, break the while loop and return to the move() function
            else:
                break

        # if no line is detected, move forward
        else:
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=speed)


# Layer Three: Sort cubes by color
def sort_cubes():
    global field_red_cubes
    global field
    global speed

    # determine if the cube needs to be sorted
    if needs_sorting():
        runloop.run(face_goal_field()) # turn into the correct direction
        while True:
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=speed)
            # in case a line is detected it is the middle line and can thus be crossed
            if line_detected():
                cross_line()
                update_field()
                motor_pair.move_for_degrees(motor_pair.PAIR_1, 20, 0) # move a little bit further
                runloop.run(move_away()) # deliver cube and move away after that
                break
    else:
        runloop.run(move_away())



async def main():
    # Show the task on the lightmatrix
    await light_matrix.write("OS!")

    # Set up the basis (e.g. reset_yaw)
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)
    print("Start yaw:", motion_sensor.tilt_angles()[0])
    motor_pair.pair(motor_pair.PAIR_1, port.F, port.B) # check if B is the left motor and F is the right one

    while True:
        runloop.run(move_around())
        #print("Yaw:", motion_sensor.tilt_angles()[0])




runloop.run(main())