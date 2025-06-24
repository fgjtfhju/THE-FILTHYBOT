import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.bot_runner import run_bot

def main():
    print("🧠 INIT: Starter bot med avansert strategi…")
    run_bot()

if __name__ == "__main__":
    main()
