from wpilib.command.command import Command
from wpilib.driverstation import DriverStation

from selector import Selector


class TestSelector(Command):
    def __init__(self):
        super().__init__()
        self.testSelector = Selector([("row1", "op1", "op2", "op3")], (0,))
        DriverStation.getInstance()
    
    def initialize(self):
        pass
    
    def execute(self):
        self.testSelector.selectorLogic()
    
"""    def isFinished(self):
        return not DriverStation.isDisabled()  """