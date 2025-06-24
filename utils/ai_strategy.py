import pandas as pd

def choose_best_strategy():
    try:
        df = pd.read_csv("strategy_results.csv", header=None, names=["timestamp", "strategy", "result"])
        recent = df.tail(50)
        grouped = recent.groupby("strategy")["result"].mean()
        best = grouped.idxmax()
        return best
    except Exception as e:
        print(f"[AI] Klarte ikke analysere strategier, bruker standard. Feil: {e}")
        return "range_trading"
