from datetime import datetime

class ShortTradingStrategy:
    def __init__(self, symbol, client, leverage=2):
        self.symbol = symbol
        self.client = client
        self.leverage = leverage
        self.average_high = None
        self.last_price = None

    def analyze_market(self, klines):
        try:
            highs = [float(k[2]) for k in klines[-20:]]
            self.average_high = sum(highs) / len(highs)
            self.last_price = float(klines[-1][4])
            print(f"[{self.symbol}] Avg high: {self.average_high}, Last price: {self.last_price}")
        except Exception as e:
            print(f"[ERROR] analyze_market (short) failed: {e}")

    def should_enter_trade(self):
        if self.average_high is None or self.last_price is None:
            return False

        if self.last_price < self.average_high * 0.98:
            print(f"[{self.symbol}] Price dropped below threshold. Entering short.")
            return True

        return False

    def execute_trade(self):
        if self.should_enter_trade():
            print(f"[TRADE] Executing short trade on {self.symbol} with {self.leverage}x leverage at {datetime.utcnow()}")
            return True
        return False
