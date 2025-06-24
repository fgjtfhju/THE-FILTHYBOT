import random
from datetime import datetime, timedelta
from exchange.bitget_api import BitgetAPI

def select_best_coin():
    client = BitgetAPI(
        api_key=os.getenv("BITGET_API_KEY"),
        api_secret=os.getenv("BITGET_API_SECRET"),
        passphrase=os.getenv("BITGET_API_PASSPHRASE")
    )

    # Liste over aktuelle symboler å analysere
    candidate_symbols = ["SOLUSDT", "DOGEUSDT", "AVAXUSDT", "MATICUSDT", "LINKUSDT"]

    best_symbol = None
    best_score = -99999
    best_direction = "long"

    for symbol in candidate_symbols:
        try:
            klines = client.get_klines(symbol=symbol, interval="1h", limit=24)
            if not klines:
                continue

            closes = [float(k[4]) for k in klines]
            change = (closes[-1] - closes[0]) / closes[0]

            score = change * 100  # enkel momentumscore

            direction = "long" if change > 0 else "short"

            if score > best_score:
                best_score = score
                best_symbol = symbol
                best_direction = direction

        except Exception as e:
            print(f"[Feil under analyse av {symbol}]: {e}")
            continue

    return best_symbol, best_direction
