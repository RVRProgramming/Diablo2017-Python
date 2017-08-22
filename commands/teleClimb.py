from wpilib.command.command import Command
from wpilib.smartdashboard import SmartDashboard

from subsystems.winch import winch


class TeleClimb(Command):
    
    def __init__(self):
        super().__init__()
        self.requires(winch)
        winch.ledPower(True)
        from common.oi import oi
        self.oi = oi
    
    def execute(self): 
        winch.climb(self.oi.getWinchSpeed())
        SmartDashboard.putNumber("Winch Throttle", self.oi.getWinchSpeed())

    def isFinished(self): 
        return False
    
    def interrupted(self): 
        winch.climb(0)
        winch.ledPower(False)