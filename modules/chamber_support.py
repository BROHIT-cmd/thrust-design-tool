import math


def support_block_design(
    thrust_kn,
    allowable_bearing=500,
    block_height=1.0
):
    """
    thrust_kn = hydraulic thrust (kN)

    allowable_bearing = allowable concrete/slab
    bearing pressure (kN/m²)

    block_height = assumed block height (m)
    """

    required_area = thrust_kn / allowable_bearing

    side = math.sqrt(required_area)

    side = math.ceil(side * 10) / 10

    volume = side * side * block_height

    return {
        "thrust": round(thrust_kn, 2),
        "required_area": round(required_area, 2),
        "length": round(side, 2),
        "width": round(side, 2),
        "height": round(block_height, 2),
        "volume": round(volume, 2)
    }
