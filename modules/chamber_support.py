import math

CONCRETE_DATA = {
    "C25/30": {
        "bearing": 500
    },
    "C30/37": {
        "bearing": 600
    },
    "C40/50": {
        "bearing": 800
    }
}

def design_support_block(
    thrust,
    concrete_grade
):

    allowable = (
        CONCRETE_DATA[
            concrete_grade
        ]["bearing"]
    )

    required_area = (
        thrust
        / allowable
    )

    side = math.sqrt(
        required_area
    )

    side = math.ceil(
        side * 10
    ) / 10

    return {
        "area": round(
            required_area,
            2
        ),
        "length": side,
        "width": side,
        "height": 1.0,
        "volume": round(
            side
            * side
            * 1.0,
            2
        )
    }
