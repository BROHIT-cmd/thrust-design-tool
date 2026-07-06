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


def design_buried_block(
        thrust_kn,
        sbc,
        safety_factor=1.5):

    required_area = (
        thrust_kn
        * safety_factor
        / sbc
    )

    side = math.sqrt(required_area)

    side = math.ceil(side * 10) / 10

    return {
        "thrust": round(thrust_kn, 2),
        "area": round(required_area, 2),
        "length": side,
        "width": side,
        "depth": 1.2,
        "volume": round(side * side * 1.2, 2)
    }


def design_chamber_support(
        thrust_kn,
        friction_coeff):

    target_fs = 1.5

    for length in [x / 10 for x in range(10, 61)]:

        for width in [x / 10 for x in range(10, 61)]:

            height = 1.0

            volume = (
                length
                * width
                * height
            )

            weight = volume * 24

            resistance = (
                weight
                * friction_coeff
            )

            fs = resistance / thrust_kn

            if fs >= target_fs:

                return {
                    "length": round(length, 2),
                    "width": round(width, 2),
                    "height": round(height, 2),
                    "volume": round(volume, 2),
                    "weight": round(weight, 2),
                    "sliding_fs": round(fs, 2)
                }

    return None
