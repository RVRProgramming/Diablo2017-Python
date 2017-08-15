
import math

from networktables.util import ntproperty
from pyfrc.physics.drivetrains import four_motor_drivetrain
import wpilib


class PhysicsEngine:

  
    def __init__(self, controller):
        self.controller = controller


        self.controller.add_device_gyro_channel('navxmxp_spi_4_angle')
        

    """
        Update pyfrc simulator

        Keyword arguments:
        self -- Global dictionary of everything.
        hal_data -- Data about motors and other components.
        now -- Current time in ms
        tm_diff -- Diff between current time and time when last checked
    """
    def update_sim(self, hal_data, now, tm_diff):
       

        # Simulate the drivetrain
        lf_motor = -hal_data['pwm'][0]['value']/5
        lr_motor = -hal_data['pwm'][1]['value']/5
        rf_motor = -hal_data['pwm'][2]['value']/5
        rr_motor = -hal_data['pwm'][3]['value']/5

        fwd, rcw = four_motor_drivetrain(lr_motor, rr_motor, lf_motor, rf_motor, speed=5)

        self.controller.drive(fwd, rcw, tm_diff)