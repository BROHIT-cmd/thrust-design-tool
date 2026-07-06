import math

def required_area(
        thrust,
        sbc,
        sf):

    return (
        thrust
        * sf
        / sbc
    )


def block_size(area):

    side = math.sqrt(area)

    return (
        round(side, 2),
        round(side, 2)
    )
