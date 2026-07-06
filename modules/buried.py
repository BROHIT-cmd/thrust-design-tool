import math

def design_thrust_block(
    thrust,
    sbc,
    safety_factor
):

    area = (
        thrust
        * safety_factor
        / sbc
    )

    side = math.sqrt(area)

    side = math.ceil(side * 10) / 10

    return {
        "area": round(area, 2),
        "length": side,
        "width": side,
        "depth": 1.2,
        "volume": round(
            side * side * 1.2,
            2
        )
    }
