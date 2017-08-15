import pprint

from commandbased import CommandBasedRobot
from hal_impl.data import hal_data
import wpilib


class MyRobot(CommandBasedRobot):
        
    def robotInit(self):
        from commands.groupDriveStraight import GroupDriveStraight
        from commands.teleDrive import TeleDrive
        from common.oi import oi
        self.autonomousCommand = GroupDriveStraight()
        self.teleDrive = TeleDrive()
        self.oi = oi
        
        pprint.pprint(hal_data)
    def autonomousInit(self):
        self.autonomousCommand.start()
    def autonomousPeriodic(self):
        pass
    def teleopInit(self):
        self.autonomousCommand.cancel()
        self.teleDrive.start()
    def teleopPeriodic(self):
        self.oi.backwardsCheck();
    def testInit(self):
        pass
    def testPeriodic(self):
        pass

if __name__ == '__main__':
    wpilib.run(MyRobot)