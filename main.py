import time
import pandas as pd

def choose_best_strategy():
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

try:
    from bot import run_bot
    print("✅ Import of run_bot successful")
except Exception as e:
    print(f"❌ Import error: {e}")
    raise

if __name__ == "__main__":
    while True:
        try:
            run_bot()
        except Exception as e:
            print(f"❌ Bot execution error: {e}")
        time.sleep(300)  # vent 5 minutter før neste runde
