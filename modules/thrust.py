import math

def pipe_area(diameter_mm):
    d = diameter_mm / 1000
    return math.pi * d**2 / 4

def bend_thrust(
  **diameter_mm,
    pressure_bar,
  **angle_deg
):
    area = pipe_area**iameter_mm)

    pressure = press**e_bar * 100

    thrust = (
     ** 2
        * pressure
        * a**a
        * math.sin(
           **ath.radians(angle_deg/2)
        **    )

    return thrust
