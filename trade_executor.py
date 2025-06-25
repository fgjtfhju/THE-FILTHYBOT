from utils.bitget_client import client
from utils.logger import log
import time

def execute_trade(symbol, direction, strategy, leverage):
    try:
        log(f"[TRADE] Starter handel: {symbol}, retning: {direction}, strategi: {strategy}, giring: {leverage}x")

        # Sett markedstype
        margin_mode = "crossed"
        trade_side = "open_long" if direction == "long" else "open_short"

        # Hent tilgjengelig balanse
        account_info = client.mix_get_account("umcbl", symbol)
        usdt_balance = float(account_info['data']['available'])

        if usdt_balance < 10:
            log(f"[AVBRUTT] For lite balanse: {usdt_balance} USDT tilgjengelig")
            return False

        # Beregn ordrevolum – f.eks. bruk 95 % av balansen
        trade_value = usdt_balance * 0.95
        mark_price = float(client.mix_get_market_price("umcbl", symbol)['data']['price'])
        size = round((trade_value * leverage) / mark_price, 3)

        # Sett giring
        client.mix_set_leverage("umcbl", symbol, leverage, leverage, margin_mode)

        # Utfør market order
        order = client.mix_place_order(
            productType="umcbl",
            symbol=symbol,
            marginCoin="USDT",
            size=str(size),
            side="buy" if direction == "long" else "sell",
            orderType="market",
            tradeSide=trade_side,
            price="",  # Ikke nødvendig for market
            marginMode=margin_mode
        )

        if order.get("code") == "00000":
            log(f"✅ Ordre lagt inn: {symbol} {direction} {size} {strategy}")
            return True
        else:
            log(f"❌ Ordre feilet: {order}")
            return False

    except Exception as e:
        log(f"❌ Unntak i execute_trade(): {str(e)}")
        return False
