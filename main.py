log_trade_result(..
.)funksjon

from datetime import datetime

def log_trade_result(strategy_name, result):
   with open("strategy_results.csv", "a") as f:
      f.write(f"{datetime.utcnow()},{strategy_name},{result}\n")

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.bot_runner import run_bot

if __name__ == "__main__":
   run_bot()
