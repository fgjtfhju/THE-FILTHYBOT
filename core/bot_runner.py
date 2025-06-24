import time
import os
from exchange.bitget_api import BitgetAPI
from core.coin_selector import select_best_coin
from core.trade_executor import execute_trade

def run_bot():
    print("🚀 Starter bot med avansert strategi...")

    # Hent API-nøkler fra miljøvariabler i Render
    API_KEY = os.getenv("BITGET_API_KEY")
    API_SECRET = os.getenv("BITGET_API_SECRET")
    API_PASSPHRASE = os.getenv("BITGET_API_PASSPHRASE")

    # Opprett Bitget-klient
    client = BitgetAPI(API_KEY, API_SECRET, API_PASSPHRASE)
    print("✅ Tilkoblet BitgetAPI")

    while True:
        try:
            # Finn beste coin og retning (long/short)
            symbol, direction = select_best_coin()

            # Sett giring dynamisk
            leverage = 4 if direction == "short" else 3

            print(f"🔍 Valgt coin: {symbol} | Retning: {direction} | Giring: {leverage}x")

            # Utfør handelen
            execute_trade(symbol=symbol, client=client, leverage=leverage)

        except Exception as e:
            print(f"[❌ BOT-FEIL] Noe gikk galt i run_bot: {e}")

        # Vent før neste loop
        time.sleep(300)  # 5 minutter
