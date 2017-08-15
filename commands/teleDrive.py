from wpilib.command.command import Command

from common import robotMap
from common.oi import oi
from subsystems.driveBase import driveBase


class TeleDrive(Command):

    def __init__(self):
        super().__init__()
        self.requires(driveBase)
        
    def execute(self):
        leftSpeed = oi.getLeftSpeed()
        rightSpeed = oi.getRightSpeed()
        if oi.getSlowDown():
            leftSpeed *= robotMap.SLOWDOWNSPEED
            rightSpeed *= robotMap.SLOWDOWNSPEED
        if oi.getBackwards():
            driveBase.drive(-rightSpeed, -leftSpeed)
        else:
            driveBase.drive(leftSpeed, rightSpeed)

    def isFinished(self):
        return False

    def interrupted(self):
        driveBase.drive(0, 0)
    