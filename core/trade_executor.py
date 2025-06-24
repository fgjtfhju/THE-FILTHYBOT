from core.strategy_handler import get_current_strategy
from main import log_trade_result

def execute_trade(symbol, client, leverage):
    strategy = get_current_strategy(symbol, client, leverage)
    print(f"[TRADE] Kjører strategi for {symbol} med {leverage}x giring...")

    try:
        result = strategy.run()
        log_trade_result(strategy.__class__.__name__, result)
        log_strategy_result(strategy.__class__.__name__, result)  # ← denne linjen MÅ med
        print(f"[TRADE] Handel fullført med resultat: {result}")
        return True  # ← signaliserer at handelen gikk gjennom

    except Exception as e:
        print(f"[ERROR] Handel feilet: {e}")
        return False  # ← signaliserer at handelen feilet

from datetime import datetime
import csv

def log_strategy_result(strategy_name, result):
    with open("strategy_results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), strategy_name, result])
