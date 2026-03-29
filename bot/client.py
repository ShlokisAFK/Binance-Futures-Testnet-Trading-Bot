import time
import hmac
import hashlib
import requests
from bot.logging_config import setup_logger

logger = setup_logger()
BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        self.session.headers.update({"X-MBX-APIKEY": self.api_key})

    def _get_server_time(self):
        response = self.session.get(BASE_URL + "/fapi/v1/time")
        return response.json()["serverTime"]

    def _sign(self, params):
        query = "&".join(f"{k}={v}" for k, v in params.items())
        signature = hmac.new(
            self.api_secret.encode(),
            query.encode(),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
            "recvWindow": 5000,
            "timestamp": self._get_server_time(),
        }
        if order_type.upper() == "LIMIT":
            if not price:
                raise ValueError("Price is required for LIMIT orders")
            params["price"] = price
            params["timeInForce"] = "GTC"

        params = self._sign(params)
        logger.debug(f"Request params: {params}")

        try:
            response = self.session.post(BASE_URL + endpoint, params=params)
            logger.debug(f"Raw response: {response.text}")
            print(f"Raw response: {response.text}")
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error: {e}")
            raise