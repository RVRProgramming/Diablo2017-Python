import pprint

from commandbased import CommandBasedRobot
from hal_impl.data import hal_data
import wpilib

from commands.groupDriveStraight import GroupDriveStraight
from commands.teleDrive import TeleDrive
from common.oi import oi


class MyRobot(CommandBasedRobot):
    
    def robotInit(self):
        self.teleDrive = TeleDrive()
        self.autonomousCommand = GroupDriveStraight()
        pprint.pprint(hal_data)
    def autonomousInit(self):
        self.autonomousCommand.start()
    def autonomousPeriodic(self):
        pass
    def teleopInit(self):
        self.autonomousCommand.cancel()
        self.teleDrive.start()
    def teleopPeriodic(self):
        oi.backwardsCheck();
    def testInit(self):
        pass
    def testPeriodic(self):
        pass

if __name__ == '__main__':
    wpilib.run(MyRobot)