import os
from dotenv import load_dotenv
from bitget_client import BitgetClient
from strategy import StrategyManager
from logger import log_trade
from portfolio import PortfolioManager

load_dotenv()

API_KEY = os.getenv("BITGET_API_KEY")
API_SECRET = os.getenv("BITGET_API_SECRET")
API_PASSPHRASE = os.getenv("BITGET_API_PASSPHRASE")
USE_SERVER_TIME = True
IS_LIVE = os.getenv("IS_LIVE", "true").lower() == "true"

client = BitgetClient(API_KEY, API_SECRET, API_PASSPHRASE, IS_LIVE, USE_SERVER_TIME)
strategy = StrategyManager(client)
portfolio = PortfolioManager(client)

def run_bot():
    print("🔄 Starter bot...")
    while True:
        try:
            best_coin = strategy.find_best_coin()
            if not best_coin:
                print("🚫 Ingen lovende coin funnet.")
                continue

            trend = strategy.analyze_trend(best_coin)
            signal = strategy.generate_signal(best_coin, trend)

            if signal == "buy":
                qty = portfolio.calculate_position_size(best_coin)
                client.place_order(best_coin, "buy", qty)
                log_trade(best_coin, "buy", qty)
                portfolio.update_after_trade(best_coin, qty)

            elif signal == "sell":
                qty = portfolio.get_current_position(best_coin)
                client.place_order(best_coin, "sell", qty)
                log_trade(best_coin, "sell", qty)
                portfolio.clear_position(best_coin)

        except Exception as e:
            print(f"❗ Feil under kjøring: {e}")

if __name__ == "__main__":
    run_bot()
