import math

# Assumed allowable bearing capacities for preliminary sizing
CONCRETE_DATA = {
    "C25/30": {
        "bearing": 500,  # kN/m²
        "fck": 25
    },
    "C30/37": {
        "bearing": 600,  # kN/m²
        "fck": 30
    },
    "C40/50": {
        "bearing": 800,  # kN/m²
        "fck": 40
    }
}


def design_support_block(
    thrust,
    concrete_grade
):
    """
    Preliminary sizing of concrete support block.

    Parameters
    ----------
    thrust : float
        Hydraulic thrust force (kN)

    concrete_grade : str
        C25/30, C30/37 or C40/50

    Returns
    -------
    dict
    """

    allowable_bearing = CONCRETE_DATA[
        concrete_grade
    ]["bearing"]

    required_area = (
        thrust /
        allowable_bearing
    )

    # Square block assumption
    side = math.sqrt(required_area)

    # Round up to nearest 100 mm
    side = math.ceil(side * 10) / 10

    height = 1.0

    volume = (
        side *
        side *
        height
    )

    return {
        "concrete_grade": concrete_grade,
        "allowable_bearing": allowable_bearing,
        "required_area": round(required_area, 2),
        "length": round(side, 2),
        "width": round(side, 2),
        "height": round(height, 2),
        "volume": round(volume, 2)
    }
