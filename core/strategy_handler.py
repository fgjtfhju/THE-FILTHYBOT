def execute_strategy(strategy_name, symbol, client):
    # Dynamisk import basert på valgt strategi
    if strategy_name == "range_trading":
        from strategies.range_trading import run
    elif strategy_name == "breakout_trading":
        from strategies.breakout_trading import run
    elif strategy_name == "short_trading":
        from strategies.short_trading import run
    else:
        raise ValueError(f"[Strategy Handler] Ukjent strategi: {strategy_name}")

    # Kjør strategien og hent signal ("buy", "sell", "hold")
    signal = run(symbol, client)

    # Logg signalet for debugformål
    print(f"[Strategy Handler] {strategy_name} returned signal: {signal}")

    return signal
