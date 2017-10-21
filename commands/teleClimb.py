from wpilib.command.command import Command

from subsystems.winch import winch


class TeleClimb(Command):
    initDuringExec = False
    
    def __init__(self):
        super().__init__()
        self.requires(winch)
        winch.ledPower(True)
    
    def execute(self): 
        if not self.initDuringExec:
            from common.oi import oi
            self.oi = oi
            self.initDuringExec = True
        winch.climb(self.oi.getWinchSpeed())
        winch.ledPower(True)

    def isFinished(self): 
        return False
    
    def interrupted(self): 
        winch.climb(0)
        winch.ledPower(False)