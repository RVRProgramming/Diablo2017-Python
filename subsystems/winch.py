import pdb

import ctre
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.smartdashboard import SmartDashboard

from common import robotMap
from wpilib.powerdistributionpanel import PowerDistributionPanel


class Winch(Subsystem):
    initInClimb = False
    def __init__(self):
        super().__init__()
        self.winchL = ctre.CANTalon(robotMap.WINCHL)
        self.winchR = ctre.CANTalon(robotMap.WINCHR)
        self.led = wpilib.Relay(robotMap.LED)
        self.pdp = PowerDistributionPanel(0)


    def climb(self, speed):
        if abs(speed) > robotMap.WINCHTHRESHOLD and wpilib.DriverStation.getInstance().isOperatorControl():
            self.winchL.set(speed)
            self.winchR.set(-speed)
        else:
            self.winchL.set(0)
            self.winchR.set(0)
            
        if not self.initInClimb:
            from common.oi import oi
            self.oi = oi
            self.initInClimb = True
        SmartDashboard.putNumber("Winch Throttle", self.oi.getWinchSpeed())
        SmartDashboard.putNumber("Left Motor", self.pdp.getCurrent(14))
        SmartDashboard.putNumber("Right Motor", self.pdp.getCurrent(12))

    def ledPower(self, power):
        if power:
            self.led.set(wpilib.Relay.Value.kForward)
        else:
            self.led.set(wpilib.Relay.Value.kOff)

winch = Winch()