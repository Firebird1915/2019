#Required libraries for the code to run
import wpilib
import ctre
import math
import magicbot
import logging
#Dashboard functionality
from wpilib.smartdashboard import SmartDashboard
from wpilib.drive import DifferentialDrive

# #Components go here
from components.drive import Drive
from components.lift import Lift
#from components.collection import Collection
FollowLeader =  ctre.basemotorcontroller.InvertType.FollowMaster

class Bob(magicbot.MagicRobot):

    # lift = Lift
    # collection = Collection

    def createObjects(self):

        drive = Drive
        lift = Lift
        #collection = Collection

        self.compressor = wpilib.Compressor()

        #Establishing Dashboard
        self.HUD = wpilib.SmartDashboard

        self.limitSwitchIn = wpilib.DigitalInput(0)


        #Left motors
        self.motor_1_LLeader = ctre.WPI_TalonSRX(8)
        self.motor_2_LFollower = ctre.WPI_TalonSRX(9)
        self.motor_3_LFollower = ctre.WPI_TalonSRX(10)

        self.motor_2_LFollower.follow(self.motor_1_LLeader)
        self.motor_3_LFollower.follow(self.motor_1_LLeader)

        #Right motors
        self.motor_1_RLeader = ctre.WPI_TalonSRX(2)
        self.motor_2_RFollower = ctre.WPI_TalonSRX(3)
        self.motor_3_RFollower = ctre.WPI_TalonSRX(4)

        self.motor_2_RFollower.follow(self.motor_1_RLeader)
        self.motor_3_RFollower.follow(self.motor_1_RLeader)

        #Set direction for motors
        self.motor_1_LLeader.setInverted(False)
        self.motor_1_RLeader.setInverted(True)

        self.motor_2_LFollower.setInverted(FollowLeader)
        self.motor_3_LFollower.setInverted(FollowLeader)

        self.motor_2_RFollower.setInverted(FollowLeader)
        self.motor_3_RFollower.setInverted(FollowLeader)

        #Lift motors
        self.lift_motor1 = ctre.WPI_TalonSRX(1)
        self.lift_motor2 = ctre.WPI_TalonSRX(7)

        #Collection motors
        self.collection_motor = ctre.WPI_TalonSRX(11)

        #Climbing
        self.climbing_motor1 = ctre.WPI_TalonSRX(5)
        self.climbing_motor2 = ctre.WPI_TalonSRX(12)
        self.climbing_motor3 = ctre.WPI_TalonSRX(13)

        #Compressors
        self.compressor_motor = ctre.WPI_TalonSRX(14)

        #DoubleSolenoids
        self.doubleS = wpilib.DoubleSolenoid(0,1)
        self.doubleS2 = wpilib.DoubleSolenoid(2,3)

        #Controllers
        self.controller = wpilib.Joystick(0)
        self.stick2 = wpilib.Joystick(1)

        self.drive = DifferentialDrive(self.motor_1_LLeader, self.motor_1_RLeader)
def teleopPeriodic(self):

        self.drive.tankDrive(controller.getRawAxis(1), controller.getRawAxis(2))

    # #Tells the motor to move based on a sensor input or button
    #     if self.stick2.getRawButon(7):
    #         self.collection_motor.start()
    #     else:
    #          self.collection_motor.stop()
    #     # elif self.LimitSwitchIn.get():
    #     #     self.collection_motor.stop()
    #     if(self.stick2.getRawButton(6) == 1):
    #         self.collection_motor.start(-1)


        # #Values to dashboard for testing
        # self.HUD.putNumber("Left Value:", ((int)(self.stick.getRawAxis(1) * 100)) / 100.0)
        # self.HUD.putNumber("Right Value:", ((int)(self.stick.getRawAxis(5) * 100)) / 100.0)


if __name__ == "__main__" :
    wpilib.run(Bob)
