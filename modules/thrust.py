import math

def pipe_area(diameter_mm):

    d = diameter_mm / 1000

    return math.pi * d**2 / 4


def bend_thrust(
        diameter_mm,
        pressure_bar,
        angle_deg):

    area = pipe_area(diameter_mm)

    pressure = pressure_bar * 100

    thrust = (
        2
        * pressure
        * area
        * math.sin(
            math.radians(angle_deg / 2)
        )
    )

    return thrust


def dead_end_thrust(
        diameter_mm,
        pressure_bar):

    area = pipe_area(diameter_mm)

    pressure = pressure_bar * 100

    return pressure * area
