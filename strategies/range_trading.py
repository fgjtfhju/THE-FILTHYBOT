from exchange.bitget_api import place_order

class RangeStrategy:
    def __init__(self, symbol, client, leverage):
        self.symbol = symbol
        self.client = client
        self.leverage = leverage

    def run(self):
        print(f"[RANGE] Kjører range-strategi for {self.symbol}")
       
        try:
            print("[RANGE] Forsøker å plassere ordre...")
            order_result = place_order(
                client=self.client,
                symbol=self.symbol,
                direction="long",
                leverage=self.leverage,
                amount=20
            )
            print(f"[RANGE] Ordre resultat: {order_result}")
            return order_result
       
        except Exception as e:
            print(f"[ERROR] Feil under range-ordre: {e}")
            return None
