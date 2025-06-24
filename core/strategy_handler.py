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
