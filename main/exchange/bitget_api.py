# main/exchange/bitget_api.py

import time
import hmac
import hashlib
import base64
import requests
import json
import os

BASE_URL = "https://emea01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fapi.bitget.com%2F&data=05%7C02%7C%7C09fc9040eec74f93e40c08ddb322934a%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C638863683303598789%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=15XkQ%2B4PFNcyFO2caMznN9vxK9O9lQ7V1GpYDEg%2F0pU%3D&reserved=0"

class BitgetAPI:
    def __init__(self, api_key, api_secret, passphrase):
        self.api_key = api_key
        self.api_secret = api_secret
        self.passphrase = passphrase

    def _get_headers(self, method, request_path, body=''):
        timestamp = str(int(time.time() * 1000))
        prehash = f"{timestamp}{method.upper()}{request_path}{body}"
        signature = hmac.new(
            self.api_secret.encode('utf-8'),
            prehash.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

        return {
            "ACCESS-KEY": self.api_key,
            "ACCESS-SIGN": signature,
            "ACCESS-TIMESTAMP": timestamp,
            "ACCESS-PASSPHRASE": self.passphrase,
            "Content-Type": "application/json"
        }

    def place_order(self, symbol, side, size, leverage):
        print(f"[BITGET] Plasserer ordre: {side} {size} {symbol} med {leverage}x gearing")

        endpoint = "/api/mix/v1/order/placeOrder"
        url = BASE_URL + endpoint

        body = {
            "symbol": symbol,
            "marginCoin": "USDT",
            "orderType": "market",
            "side": side,
            "size": str(size),
            "leverage": str(leverage),
            "marketCode": "USDT",
            "tradeSide": side,
            "productType": "USDT-FUTURES"
        }

        headers = self._get_headers("POST", endpoint, json.dumps(body))

        try:
            response = requests.post(url, headers=headers, data=json.dumps(body))
            data = response.json()
            print(f"[BITGET] Ordresvar: {data}")
            return data
        except Exception as e:
            print(f"[ERROR] Feil ved ordre: {e}")
            return None
