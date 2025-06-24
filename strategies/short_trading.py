from exchange.bitget_api import place_order

class ShortStrategy:
    def __init__(self, symbol, client, leverage):
        self.symbol = symbol
        self.client = client
        self.leverage = leverage

    def run(self):
        print(f"[SHORT] Kjører short-strategi for {self.symbol}")
       
        try:
            print("[SHORT] Forsøker å plassere short-ordre...")
            order_result = place_order(
                client=self.client,
                symbol=self.symbol,
                direction="short",
                leverage=self.leverage,
                amount=20
            )
            print(f"[SHORT] Ordre resultat: {order_result}")
            return order_result
       
        except Exception as e:
            print(f"[ERROR] Feil under short-ordre: {e}")
            return None
