import importlib
from strategies.range_trading import RangeTradingStrategy
from strategies.breakout_trading import BreakoutTradingStrategy
from strategies.short_trading import ShortTradingStrategy

strategy_classes = {
    "range_trading": RangeTradingStrategy,
    "breakout_trading": BreakoutTradingStrategy,
    "short_trading": ShortTradingStrategy
}

def get_strategy_by_name(name):
    strategy_class = strategy_classes.get(name)
    if strategy_class is None:
        raise ValueError(f"Ukjent strategi: {name}")
    return strategy_class()
