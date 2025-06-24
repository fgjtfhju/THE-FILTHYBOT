from datetime import datetime
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.bot_runner import run_bot

def log_trade_result(strategy_name, result):
   with open("strategy_results.csv", "a") as f:
      f.write(f"{datetime.utcnow()},{strategy_name},{result}\n")

def choose_best_strategy():
   try:
      df = pd.read_csv("strategy_results.csv", header=None, names=["timestamp", "strategy", "result"])
      recent = df.tail(50)
      grouped = recent.groupby("strategy")["result"].mean()
      best = grouped.idmax()
      print(f"[AI] Strategy analysis failed: {str(e)}")
      return "range_trading" 

try:
    from bot import run_bot
except Exception as e:
    print(f"Import error: {e]":
    raise
         
import time

if __name__ == "__main__":
   while True:
        run_bot()
      time.sleep(300)
