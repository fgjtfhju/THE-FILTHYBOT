from core.strategy_handler import select_strategy

import time
import traceback
from core.strategy_handler import select_strategy
from trade_executor import execute_trade
from coin_selector import select_best_coin
from utils.logger import log
from utils.ai_strategy import choose_best_strategy
from utils.gearing import determine_leverage

# Tid mellom hver syklus (sekunder – 5 minutter)
SLEEP_INTERVAL = 300

def run_bot_cycle():
    try:
        log("🚀 Starter ny handelsrunde...")

        # Velg beste coin og retning (long/short)
        log("[DEBUG] Velger coin og retning...")
        coin, direction = select_best_coin()
        log(f"[DEBUG] Valgt coin: {coin}, retning: {direction}")

        # AI-basert valg av strategi
        log("[DEBUG] Velger strategi...")
        strategy_name = choose_best_strategy()
        log(f"[DEBUG] Valgt strategi: {strategy_name}")

        # Dynamisk gearing basert på risiko
        log("[DEBUG] Bestemmer giring...")
        leverage = determine_leverage(coin, direction)
        log(f"[DEBUG] Bruker giring: {leverage}x")

        # Kjør handel
        log("[DEBUG] Utfører handel nå...")
        success = execute_trade(coin, direction, strategy_name, leverage)

        if success:
            log(f"✅ Handel fullført: {coin} {direction} {strategy_name} {leverage}x")
        else:
            log(f"⚠️  Handel feilet for: {coin} {direction} {strategy_name}")

    except Exception as e:
        log(f"❌ Feil i run_bot_cycle: {str(e)}")
        traceback.print_exc()

def run_bot():
    log("🟢 FILTHYBOT er i gang!")
    while True:
        run_bot_cycle()
        time.sleep(SLEEP_INTERVAL)
