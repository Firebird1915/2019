import wpilib
import ctre
import math

class Drive:
    ################################################
    #Handles actual driving and dealing with inputs#
    ################################################

    #The motor wont run unless the controller outputs above this
    DEADZONE = .1
    driveSPEED = .8


    #Required but not used
    def __init__(self):
        pass

    #Drives the robot using a tank drive
    def move(left, right):


        tankDrive(leftSpeed, rightSpeed, squareInputs=True)

        #Sets controller outputs to 0 if they are in the deadzone
    #     if math.fabs(left) < self.DEADZONE:
    #         left = 0
    #
    #     if math.fabs(right) < self.DEADZONE:
    #         right = 0
    #
    # def shift(self, direction):
    #     if (direction == 1):
    #         self.doubleS.set(2)
    #         self.doubleS2.set(2)
    #     else:
    #         self.doubleS.set(1)
    #         self.doubleS2.set(1)

    #Required but not used
    def execute(self):
            pass
