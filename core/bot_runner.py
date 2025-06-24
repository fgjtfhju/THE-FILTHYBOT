import time
from exchange.bitget_api import BitgetAPI
from core.coin_selector import select_best_coin
from core.trade_executor import execute_trade

API_KEY = "DIN_API_KEY"
API_SECRET = "DIN_SECRET"
API_PASSPHRASE = "DIN_PASSPHRASE"

def run_bot():
    print("🚀 Starter bot med avansert strategi...")

    client = BitgetAPI(API_KEY, API_SECRET, API_PASSPHRASE)
    print("✅ Tilkoblet BitgetAPI")

    while True:
        try:
            # Finn beste coin og anbefalt retning
            symbol, direction = select_best_coin()

            # Velg ønsket giring basert på strategi
            leverage = 4 if direction == "short" else 3

            print(f"🔍 Valgt coin: {symbol} | Retning: {direction} | Giring: {leverage}x")

            # Utfør handel
            execute_trade(symbol=symbol, client=client, leverage=leverage)

        except Exception as e:
            print(f"[❌ BOT-FEIL] Noe gikk galt i run_bot: {e}")

        time.sleep(300) 
