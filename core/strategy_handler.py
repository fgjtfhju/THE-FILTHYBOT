from strategies.range_trading import RangeTradingStrategy
from strategies.breakout_trading import BreakoutTradingStrategy
from strategies.short_trading import ShortTradingStrategy
from main import choose_best_strategy

def load_strategy(name, symbol, client, leverage):
    if name == "range_trading":
        return RangeTradingStrategy(symbol, client, leverage)
    elif name == "breakout_trading":
        return BreakoutTradingStrategy(symbol, client, leverage)
    elif name == "short_trading":
        return ShortTradingStrategy(symbol, client, leverage)
    else:
        raise ValueError(f"Ukjent strategi: {name}")

def get_current_strategy(symbol, client, leverage=2):
    name = choose_best_strategy()
    print(f"[STRATEGY] Valgt strategi: {name}")
    return load_strategy(name, symbol, client, leverage)
