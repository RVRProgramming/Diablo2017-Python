from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

from commands.autoDriveStraight import AutoDriveStraight


class GroupDriveStraight(CommandGroup):

    def __init__(self):
        super().__init__()
        self.addSequential(AutoDriveStraight(1300))
        self.addSequential(WaitCommand(2.5))
        self.addSequential(AutoDriveStraight(350))