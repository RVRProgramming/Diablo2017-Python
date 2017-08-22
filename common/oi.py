import wpilib
from wpilib.buttons.joystickbutton import JoystickButton


from common import robotMap


class OI():
    
    backwardsButton = False
    backwardsToggle = False
    
    
    def __init__(self):
        self.joystick = wpilib.Joystick(robotMap.JOYSTICK)
        self.gamepad = wpilib.Joystick(robotMap.GAMEPAD)
        self.winchToggle = JoystickButton(self.joystick, robotMap.WINCHTOGGLE)
        from commands import teleClimb
        self.winchToggle.toggleWhenPressed(teleClimb.TeleClimb())
    def getLeftSpeed(self):
        return self.gamepad.getRawAxis(robotMap.LEFTDRIVECONTROL)
        
    def getRightSpeed(self):
        return self.gamepad.getRawAxis(robotMap.RIGHTDRIVECONTROL)

    def backwardsCheck(self):
        if (self.backwardsButton and not self.gamepad.getRawButton(robotMap.REVERSE)):
            self.backwardsButton = False
        elif (not self.backwardsButton and self.gamepad.getRawButton(robotMap.REVERSE)):
            self.backwardsButton = True
            self.backwardsToggle = not self.backwardsToggle

    def getBackwards(self): 
        return self.backwardsToggle
    

    def getSlowDown(self):
        return self.gamepad.getRawButton(robotMap.SLOWDOWN)
    
    def getWinchSpeed(self):
        return self.joystick.getRawAxis(robotMap.WINCH)
    
    def getPOV(self):
        return self.gamepad.getPOV()
    
oi = OI()