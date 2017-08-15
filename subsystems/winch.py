import ctre
import wpilib
from wpilib.command.subsystem import Subsystem

from common import robotMap


class Winch(Subsystem):

    def __init__(self):
        super().__init__()
        self.winchL = ctre.CANTalon(robotMap.WINCHL)
        self.winchR = ctre.CANTalon(robotMap.WINCHR)
        self.led = wpilib.Relay(robotMap.LED)

    def climb(self, speed):
        if ((speed < -robotMap.WINCHTHRESHOLD or speed > robotMap.WINCHTHRESHOLD) and wpilib.DriverStation.isOperatorControl(self)):
            self.winchL.set(speed)
            self.winchR.set(-speed)
        else:
            self.winchL.set(0)
            self.winchR.set(0)

    def ledPower(self, power):
        if power:
            self.led.set(wpilib.Relay.Value.kForward)
        else:
            self.led.set(wpilib.Relay.Value.kOff)

winch = Winch()