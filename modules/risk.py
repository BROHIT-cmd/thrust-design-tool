def risk_rating(fs):

    if fs >= 2:
        return "LOW"

    elif fs >= 1.5:
        return "MEDIUM"

    elif fs >= 1:
        return "HIGH"

    else:
        return "EXTREME"
