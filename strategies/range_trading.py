from exchange.bitget_api import place_order

class RangeStrategy:
    def __init__(self, symbol, client, leverage):
        self.symbol = symbol
        self.client = client
        self.leverage = leverage

    def run(self):
        print(f"[RANGE] Kjører range-strategi for {self.symbol}")
        order_result = place_order(
            client=self.client,
            symbol=self.symbol,
            direction="long",
            leverage=self.leverage,
            amount=20  # dollarverdi per handel
        )
        return order_result
