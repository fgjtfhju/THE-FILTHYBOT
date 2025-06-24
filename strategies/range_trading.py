from exchange.bitget_api import place_order

class RangeStrategy:
    def __init__(self, symbol, client, leverage):
        self.symbol = symbol
        self.client = client
        self.leverage = leverage

    def run(self):
        print(f"[RANGE] Kjører range trading-strategi for {self.symbol}")
        # Eksempel på range-trading (kan utvides)
        order_result = place_order(
            client=self.client,
            symbol=self.symbol,
            direction="long",
            leverage=self.leverage,
            amount=20  # dollarverdi
        )
        return order_result
