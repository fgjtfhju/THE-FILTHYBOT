from datetime import datetime

class BreakoutTradingStrategy:
    def __init__(self, symbol, client, is_short=False, leverage=1):
        self.symbol = symbol
        self.client = client
        self.is_short = is_short
        self.leverage = leverage
        self.breakout_level = None
        self.last_price = None

    def analyze_market(self, klines):
        try:
            highs = [float(kline[2]) for kline in klines[-20:]]
            lows = [float(kline[3]) for kline in klines[-20:]]
            self.breakout_level = max(highs) if not self.is_short else min(lows)
            self.last_price = float(klines[-1][4])
            print(f"[{self.symbol}] Breakout level: {self.breakout_level}, Last price: {self.last_price}")
        except Exception as e:
            print(f"[ERROR] analyze_market (breakout) failed: {e}")

    def should_enter_trade(self):
        if self.breakout_level is None or self.last_price is None:
            return False

        if not self.is_short and self.last_price > self.breakout_level:
            print(f"[{self.symbol}] Breakout above resistance. Long entry.")
            return True
        elif self.is_short and self.last_price < self.breakout_level:
            print(f"[{self.symbol}] Breakdown below support. Short entry.")
            return True

        return False

    def execute_trade(self):
        if self.should_enter_trade():
            direction = "short" if self.is_short else "long"
            print(f"[TRADE] Executing {direction} breakout trade on {self.symbol} with {self.leverage}x leverage at {datetime.utcnow()}")
            return True
        return False
