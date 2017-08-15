from commandbased import CommandBasedRobot
import wpilib


class MyRobot(CommandBasedRobot):
        
    def robotInit(self):
        CommandBasedRobot.robotInit(self)
        from commands.groupDriveStraight import GroupDriveStraight
        from commands.teleDrive import TeleDrive
        from common.oi import oi
        self.autonomousCommand = GroupDriveStraight()
        self.teleDrive = TeleDrive()
        self.oi = oi
    def autonomousInit(self):
        CommandBasedRobot.autonomousInit(self)
        self.autonomousCommand.start()
    def autonomousPeriodic(self):
        CommandBasedRobot.autonomousPeriodic(self)
    def teleopInit(self):
        CommandBasedRobot.teleopInit(self)
        self.autonomousCommand.cancel()
        self.teleDrive.start()
    def teleopPeriodic(self):
        CommandBasedRobot.teleopPeriodic(self)
        self.oi.backwardsCheck();
    def testInit(self):
        CommandBasedRobot.testInit(self)
    def testPeriodic(self):
        CommandBasedRobot.testPeriodic(self)

if __name__ == '__main__':
    wpilib.run(MyRobot)