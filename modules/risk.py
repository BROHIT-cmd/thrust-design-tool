def risk_level(fs):

    if fs > 2:
        return "LOW"

    elif fs >= 1.5:
        return "MEDIUM"

    elif fs >= 1:
        return "HIGH"

    return "EXTREME"
