import pandas as pd

def select_strategy():
    try:
        df = pd.read_csv("strategy_results.csv", header=None, names=["timestamp", "strategy", "result"])
        recent = df.tail(50)
        grouped = recent.groupby("strategy")["result"].mean()
        best = grouped.idxmax()
        print(f"[AI] Best strategy: {best}")
        return best
    except Exception as e:
        print(f"[AI] Strategy analysis failed: {str(e)}")
        return "range_trading"
        #Trigger redeploy
def execute_strategy(symbol, direction, strategy_name, leverage):
    from core.strategy import range_trading, breakout_trading, short_trading

    if strategy_name == "range_trading":
        return range_trading.run(symbol, direction, leverage)
    elif strategy_name == "breakout_trading":
        return breakout_trading.run(symbol, direction, leverage)
    elif strategy_name == "short_trading":
        return short_trading.run(symbol, direction, leverage)
    else:
        raise ValueError(f"Ukjent strategi: {strategy_name}")
