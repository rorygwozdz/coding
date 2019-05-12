import time


def b_trade(data):
    trades = []

    if data['type'] == 'book' and data['symbol'] == 'BOND':
        asks = data['sell']
        for price, size in asks:
            if price < 1000:
                trade = {"type": "add", "order_id": counter, "symbol": "BOND",
                "dir": "BUY", "price": price, "size": size}
             trades.append(trade)

        bids = data['buy']
        for price, size in bids:
            if price > 1000:
                trade = {"type": "add", "order_id": counter, "symbol": "BOND",
             "dir": "SELL", "price": price, "size": size}
            trades.append(trade)
    return trades
