def determine_leverage(volatility):
    if volatility < 0.01:
        return 4  # lav volatilitet, høyere gearing
    elif volatility < 0.03:
        return 3
    elif volatility < 0.05:
        return 2
    else:
        return 1  # høy volatilitet, lav gearing for å redusere risiko
