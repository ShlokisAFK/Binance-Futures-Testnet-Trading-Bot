import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("logs/trading_bot.log")
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger