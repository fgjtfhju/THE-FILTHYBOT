import random
from datetime import datetime

class RangeTradingStrategy:
    def __init__(self, symbol, client, is_short=False, leverage=1):
        self.symbol = symbol
        self.client = client
        self.is_short = is_short
        self.leverage = leverage
        self.range_low = None
        self.range_high = None
        self.last_price = None

    def analyze_market(self, klines):
        try:
            closes = [float(kline[4]) for kline in klines[-20:]]  # siste 20 candles
            self.range_low = min(closes)
            self.range_high = max(closes)
            self.last_price = closes[-1]
            print(f"[{self.symbol}] Range: {self.range_low} - {self.range_high}, Last price: {self.last_price}")
        except Exception as e:
            print(f"[ERROR] analyze_market failed for {self.symbol}: {e}")

    def should_enter_trade(self):
        if not self.range_low or not self.range_high or not self.last_price:
            return False

        mid = (self.range_high + self.range_low) / 2
        if self.last_price < mid:
            print(f"[{self.symbol}] Signal: BUY (Price below mid)")
            return not self.is_short
        else:
            print(f"[{self.symbol}] Signal: SHORT (Price above mid)")
            return self.is_short

    def execute_trade(self):
        if self.should_enter_trade():
            direction = "short" if self.is_short else "long"
            print(f"[TRADE] Executing {direction} trade on {self.symbol} with {self.leverage}x leverage at {datetime.utcnow()}")
            # Her kan faktisk trade-utførelse kobles til klienten
            return True
        return False
