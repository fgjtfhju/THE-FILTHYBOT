from exchange.bitget_api import place_order

class BreakoutStrategy:
    def __init__(self, symbol, client, leverage):
        self.symbol = symbol
        self.client = client
        self.leverage = leverage

    def run(self):
        print(f"[BREAKOUT] Kjører breakout-strategi for {self.symbol}")
        # Eksempel på breakout-logikk (kan utvides)
        order_result = place_order(
            client=self.client,
            symbol=self.symbol,
            direction="long",
            leverage=self.leverage,
            amount=20  # dollarverdi
        )
        return order_result

