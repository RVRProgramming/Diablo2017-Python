import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.robotdrive import RobotDrive

from common import robotMap


class DriveBase(Subsystem):
    
    def __init__(self):
        super().__init__()
        self.diabloDrive = RobotDrive(wpilib.Spark(robotMap.L1DRIVE), wpilib.Spark(robotMap.L2DRIVE), wpilib.Spark(robotMap.R1DRIVE), wpilib.Spark(robotMap.R2DRIVE))
        self.diabloDrive.frontLeftMotor.enableDeadbandElimination(True)
        self.diabloDrive.frontRightMotor.enableDeadbandElimination(True)
        self.diabloDrive.rearLeftMotor.enableDeadbandElimination(True)
        self.diabloDrive.rearRightMotor.enableDeadbandElimination(True)

    def drive(self, left, right):
        self.diabloDrive.tankDrive(left, right)
        
driveBase = DriveBase()