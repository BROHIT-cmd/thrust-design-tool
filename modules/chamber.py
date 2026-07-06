def concrete_volume(
        length,
        width,
        height):

    return length * width * height


def concrete_weight(volume):

    return volume * 24


def sliding_fs(
        thrust,
        weight,
        mu):

    resistance = weight * mu

    return resistance / thrust
