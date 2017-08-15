import time

from wpilib.command.command import Command

from subsystems.driveBase import driveBase


class AutoDriveStraight(Command):
    driveTime = 0

    def __init__(self, driveTime):
        super().__init__()
        self.requires(driveBase)
        self.driveTime = driveTime

    def initialize(self):
        self.startTime = time.time()
    def  execute(self):
        driveBase.drive(0.75, 0.75)

    def isFinished(self): 
        return time.time() - self.startTime > (self.driveTime/1000)
    def end(self):
        driveBase.drive(0, 0)
