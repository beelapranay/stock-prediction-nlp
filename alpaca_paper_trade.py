"""Alpaca paper trading integration for PPO agent."""

import os
from typing import Optional

import alpaca_trade_api as tradeapi


class AlpacaPaperTrader:
    """Simple wrapper around the Alpaca trade API."""

    def __init__(self, api_key: Optional[str] = None, api_secret: Optional[str] = None,
                 base_url: str = "https://paper-api.alpaca.markets") -> None:
        self.api_key = api_key or os.getenv("ALPACA_API_KEY")
        self.api_secret = api_secret or os.getenv("ALPACA_API_SECRET")
        if not self.api_key or not self.api_secret:
            raise ValueError("Alpaca credentials not provided")
        self.api = tradeapi.REST(self.api_key, self.api_secret, base_url, api_version="v2")

    def place_order(self, symbol: str, qty: int, side: str, order_type: str = "market",
                    time_in_force: str = "gtc"):
        """Submit an order and log basic info."""
        try:
            order = self.api.submit_order(
                symbol=symbol,
                qty=qty,
                side=side,
                type=order_type,
                time_in_force=time_in_force,
            )
            print(f"submitted {side} order for {qty} {symbol}")
            return order
        except Exception as exc:
            print(f"order failed: {exc}")
            return None


# Example usage: when the agent predicts a long signal
if __name__ == "__main__":
    trader = AlpacaPaperTrader()
    # Example order: buy 1 share of NVDA
    trader.place_order("NVDA", qty=1, side="buy")
