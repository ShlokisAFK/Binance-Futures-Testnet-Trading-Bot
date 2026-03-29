VALID_SIDES = ["BUY", "SELL"]
VALID_TYPES = ["MARKET", "LIMIT"]

def validate_inputs(symbol, side, order_type, quantity, price):
    if not symbol:
        raise ValueError("Symbol cannot be empty")
    if side.upper() not in VALID_SIDES:
        raise ValueError(f"Invalid side '{side}'. Choose BUY or SELL.")
    if order_type.upper() not in VALID_TYPES:
        raise ValueError(f"Invalid order type '{order_type}'. Choose MARKET or LIMIT.")
    if float(quantity) <= 0:
        raise ValueError(f"Quantity must be greater than 0. Got: {quantity}")