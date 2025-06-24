from datetime import datetime
import time
import pandas as pd
import random

def range_trading():
    return round(random.uniform(-0.01, 0.03), 4)

def breakout_trading():
    return round(random.uniform(-0.02, 0.05), 4)

def short_strategy():
    return round(random.uniform(-0.03, 0.04), 4)

def log_trade(strategy_name, result):
    with open("strategy_results.csv", "a") as f:
        f.write(f"{datetime.utcnow()},{strategy_name},{result}\n")

def choose_best_strategy():
    try:
        df = pd.read_csv("strategy_results.csv", header=None, names=["timestamp", "strategy", "result"])
        recent = df.tail(50)
        grouped = recent.groupby("strategy")["result"].mean()
        best = grouped.idxmax()
        return best
    except Exception:
        return "range_trading"  # fallback

def run_bot():
    while True:
        strategy = choose_best_strategy()
        if strategy == "range_trading":
            result = range_trading()
        elif strategy == "breakout_trading":
            result = breakout_trading()
        elif strategy == "short_strategy":
            result = short_strategy()
        else:
            result = range_trading()  # fallback

        log_trade(strategy, result)
        print(f"[{datetime.utcnow()}] Strategy: {strategy}, Result: {result}")
        time.sleep(60 * 60)  # én gang i timen
