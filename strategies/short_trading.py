from exchange.bitget_api import place_order

class ShortStrategy:
    def __init__(self, symbol, client, leverage):
        self.symbol = symbol
        self.client = client
        self.leverage = leverage

    def run(self):
        print(f"[SHORT] Kjører short-strategi for {self.symbol}")
        # Eksempel på short-trading
        order_result = place_order(
            client=self.client,
            symbol=self.symbol,
            direction="short",
            leverage=self.leverage,
            amount=20  # dollarverdi
        )
        return order_result
