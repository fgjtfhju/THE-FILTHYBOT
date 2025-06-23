import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.bot_runner import run_bot

if __name__ == "__main__":
   run_bot()
