from bot.logging_config import setup_logger
logger = setup_logger()

def place_order(client, symbol, side, order_type, quantity, price=None):
    logger.info(f"Placing {order_type} {side} order | {symbol} | qty: {quantity}" +
                (f" | price: {price}" if price else ""))
    try:
        result = client.place_order(symbol, side, order_type, quantity, price)
        logger.info(f"Order placed successfully | ID: {result.get('orderId')} | "
                   f"Status: {result.get('status')} | "
                   f"Executed: {result.get('executedQty')} | "
                   f"Avg Price: {result.get('avgPrice', 'N/A')}")
        return result
    except Exception as e:
        logger.error(f"Order failed: {e}")
        raise