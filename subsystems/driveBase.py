import ctre
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.robotdrive import RobotDrive

from common import robotMap


class DriveBase(Subsystem):
    
    def __init__(self):
        super().__init__()
        self.diabloDrive = RobotDrive(ctre.CANTalon(1), ctre.CANTalon(3), ctre.CANTalon(4), ctre.CANTalon(2))

    def drive(self, left, right):
        self.diabloDrive.tankDrive(-left, -right, squaredInputs=False)
        
driveBase = DriveBase()