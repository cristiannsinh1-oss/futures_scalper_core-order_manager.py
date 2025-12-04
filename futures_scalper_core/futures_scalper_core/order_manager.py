from binance.client import Client
from binance.enums import *
import time

class OrderManager:
    def __init__(self, client: Client, leverage: int = 5):
        self.client = client
        self.leverage = leverage

    def set_leverage(self, symbol: str):
        try:
            self.client.futures_change_leverage(
                symbol=symbol,
                leverage=self.leverage
            )
        except Exception as e:
            print("Error setting leverage:", e)

    def open_order(self, symbol: str, side: str, quantity: float):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                type="MARKET",
                side=side,
                quantity=quantity,
            )
            return order
        except Exception as e:
            print("Error opening order:", e)
            return None

    def close_order(self, symbol: str, side: str, quantity: float):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                type="MARKET",
                side=side,
                quantity=quantity,
            )
            return order
        except Exception as e:
            print("Error closing order:", e)
            return None
