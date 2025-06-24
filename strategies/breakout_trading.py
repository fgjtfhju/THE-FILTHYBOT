import pandas as pd
import numpy as np

def breakout_trading(df, force_trade=False):
    if df is None or len(df) < 20:
        print("[Breakout] Ikke nok data for analyse")
        return None

    df['rolling_high'] = df['high'].rolling(window=20).max()
    df['rolling_low'] = df['low'].rolling(window=20).min()

    last_close = df['close'].iloc[-1]
    last_high = df['rolling_high'].iloc[-2]
    last_low = df['rolling_low'].iloc[-2]

    if last_close > last_high:
        print("[Breakout] Brudd opp oppdaget – LONG")
        return {'side': 'buy', 'confidence': 0.8}
    elif last_close < last_low:
        print("[Breakout] Brudd ned oppdaget – SHORT")
        return {'side': 'sell', 'confidence': 0.8}
    else:
        print("[Breakout] Ingen brudd – ingen handel")

        # Hvis tvungen testhandel er aktivert
        if force_trade:
            direction = np.random.choice(['buy', 'sell'])
            print(f"[Breakout] Testhandel aktivert – simulerer {direction.upper()}")
            return {'side': direction, 'confidence': 0.5}

        return None

