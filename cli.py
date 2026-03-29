import argparse
import os
from bot.client import BinanceClient
from bot.validators import validate_inputs
from bot.orders import place_order
from bot.logging_config import setup_logger
from config import API_KEY, API_SECRET
api_key = API_KEY
api_secret = API_SECRET
logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol",     required=True,  help="e.g. BTCUSDT")
    parser.add_argument("--side",       required=True,  help="BUY or SELL")
    parser.add_argument("--type",       required=True,  dest="order_type", help="MARKET or LIMIT")
    parser.add_argument("--quantity",   required=True,  help="Order quantity")
    parser.add_argument("--price",      required=False, help="Price (required for LIMIT)")
    args = parser.parse_args()

    if not api_key or not api_secret:
        print("ERROR: Set BINANCE_API_KEY and BINANCE_API_SECRET environment variables")
        return

    try:
        validate_inputs(args.symbol, args.side, args.order_type, args.quantity, args.price)
    except ValueError as e:
        print(f"Validation error: {e}")
        return

    print(f"\nOrder Request Summary:")
    print(f"  Symbol:     {args.symbol.upper()}")
    print(f"  Side:       {args.side.upper()}")
    print(f"  Type:       {args.order_type.upper()}")
    print(f"  Quantity:   {args.quantity}")
    if args.price:
        print(f"  Price:      {args.price}")
    confirm = input("\nConfirm order? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Order cancelled.")
        return
    client = BinanceClient(api_key, api_secret)
    try:
        result = place_order(client, args.symbol, args.side, args.order_type, args.quantity, args.price)
        print(f"\nOrder placed successfully!")
        print(f"  Order ID:   {result.get('orderId')}")
        print(f"  Status:     {result.get('status')}")
        print(f"  Executed:   {result.get('executedQty')}")
        print(f"  Avg Price:  {result.get('avgPrice', 'N/A')}")
    except Exception as e:
        print(f"\nOrder failed: {e}")

if __name__ == "__main__":
    main()


