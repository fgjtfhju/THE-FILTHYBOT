# src/core/bot_runner.py

from core.trade_executor import execute_trade
from utils.client_factory import create_bitget_client

def run_bot():
    print("=== Starter bot ===")
    client = create_bitget_client()

    # Midlertidig test-coins – juster etter ønsket symbol
    symbols = ["DOGEUSDT", "SOLUSDT"]

    for symbol in symbols:
        leverage = 3  # eller hent fra .env eller strategi
        print(f"[BOT] Starter trading for {symbol} med {leverage}x giring")
        execute_trade(symbol, client, leverage)
