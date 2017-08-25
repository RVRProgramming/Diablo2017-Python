from commandbased import CommandBasedRobot
import wpilib

from customSelectors.testSelector1 import TestSelector


class MyRobot(CommandBasedRobot):
        
    def robotInit(self):
        CommandBasedRobot.robotInit(self)
        from commands.groupDriveStraight import GroupDriveStraight
        from commands.teleDrive import TeleDrive
        from common.oi import oi
        self.autonomousCommand = GroupDriveStraight()
        self.teleDrive = TeleDrive()
        self.oi = oi
        self.testSelector = TestSelector()
    def disabledInit(self):
        pass
    def autonomousInit(self):
        super().autonomousInit()
        self.autonomousCommand.start()
    def autonomousPeriodic(self):
        super().autonomousPeriodic()
    def teleopInit(self):
        super().teleopInit()
        self.autonomousCommand.cancel()
        self.teleDrive.start()
        self.testSelector.start()
    def teleopPeriodic(self):
        super().teleopPeriodic()
        self.oi.backwardsCheck()
    def testInit(self):
        super().testInit()
    def testPeriodic(self):
        super().testPeriodic()

if __name__ == '__main__':
    wpilib.run(MyRobot)