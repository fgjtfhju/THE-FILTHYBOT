import requests
import time

def fetch_top_coins(limit=100):
    try:
        url = "https://emea01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fapi.coingecko.com%2Fapi%2Fv3%2Fcoins%2Fmarkets&data=05%7C02%7C%7C63ca1640579a4f308b1c08ddb2ff8dbf%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C638863532850016493%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=wU2TINe%2Bp%2FqMU9gL%2BDyLUP3Pl5FalkUT9SvPkoMMUPY%3D&reserved=0"
        params = {
            "vs_currency": "usdt",
            "order": "volume_desc",
            "per_page": limit,
            "page": 1,
            "sparkline": False
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        coins = response.json()
        return [coin['symbol'].upper() for coin in coins]
    except Exception as e:
        print(f"[Coin Selector] Failed to fetch top coins: {e}")
        return []

def select_best_coin(market_data, strategy_mode="long"):
    try:
        if not market_data:
            return None

        sorted_data = sorted(
            market_data,
            key=lambda x: x["change_pct_24h"],
            reverse=(strategy_mode == "long")
        )
        return sorted_data[0]["symbol"]
    except Exception as e:
        print(f"[Coin Selector] Error selecting best coin: {e}")
        return None

def get_market_data(coins):
    data = []
    for coin in coins:
        try:
            url = f"https://emea01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fapi.coingecko.com%2Fapi%2Fv3%2Fcoins%2F&data=05%7C02%7C%7C63ca1640579a4f308b1c08ddb2ff8dbf%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C638863532850036090%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=zB9iVE7xgYsOa7Fl3B9kzz%2FN2lVrActil6RmHOZFGsw%3D&reserved=0{coin.lower()}"
            res = requests.get(url)
            res.raise_for_status()
            info = res.json()
            pct_change = info.get("market_data", {}).get("price_change_percentage_24h", 0.0)
            data.append({
                "symbol": coin.upper(),
                "change_pct_24h": pct_change
            })
            time.sleep(1.2)  # Rate limiting
        except Exception as e:
            print(f"[Coin Selector] Failed to fetch data for {coin}: {e}")
    return data
