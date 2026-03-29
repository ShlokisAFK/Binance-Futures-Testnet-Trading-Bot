# Binance Futures Testnet Trading Bot

A Python CLI application to place Market and Limit orders on Binance Futures Testnet (USDT-M) with structured logging, input validation, and clean error handling.

---

## Features

- Place **Market** and **Limit** orders via CLI
- Supports both **BUY** and **SELL** sides
- Order confirmation prompt before execution
- Structured logging to file (`logs/trading_bot.log`)
- Clean error messages for invalid input and API errors
- Secure API keys never hardcoded, loaded from local config

## Project Structure

```
trading_bot/
  bot/
    __init__.py
    client.py         # Binance API client (auth, signing, HTTP)
    orders.py         # Order placement logic
    validators.py     # Input validation
    logging_config.py # Shared logger setup
  cli.py              # CLI entry point
  config.example.py   # Template for API credentials
  requirements.txt
```

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/ShlokisAFK/Binance-Futures-Testnet-Trading-Bot
cd Binance-Futures-Testnet-Trading-Bot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up API credentials**
```bash
cp config.example.py config.py
```
Open `config.py` and add your Binance Futures Testnet API key and secret.
Get credentials at: https://testnet.binancefuture.com

## Usage

**Market Order**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

**Limit Order**
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 65000
```

**Sell Order**
```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.002
```

## Example Output

```
Order Request Summary:
  Symbol:     BTCUSDT
  Side:       BUY
  Type:       MARKET
  Quantity:   0.002

Confirm order? (yes/no): yes

Order placed successfully!
  Order ID:   13001404384
  Status:     NEW
  Executed:   0.000
  Avg Price:  0.00
```

## Assumptions

- Testnet only uses https://testnet.binancefuture.com
- Minimum order notional is $100 (Binance requirement) use quantity ≥ 0.002 for BTCUSDT
- Server time is fetched from Binance directly to avoid local clock sync issues
- Log file is created automatically at `logs/trading_bot.log`