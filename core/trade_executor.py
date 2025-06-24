from core.strategy_handler import get_current_strategy
from main import log_trade_result

def execute_trade(symbol, client, leverage):
    strategy = get_current_strategy(symbol, client, leverage)
    try:
        print(f"[TRADE] Kjører strategi for {symbol} med {leverage}x giring...")
        result = strategy.run()
        log_trade_result(strategy.__class__.__name__, result)
        print(f"[TRADE] Handel fullført med resultat: {result}")
    except Exception as e:
        print(f"[ERROR] Handel feilet: {e}")
