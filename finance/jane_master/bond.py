def b_trade(data, count):
    trades = []
    if data['type'] == 'book' and data['symbol'] == 'BOND':
        asks = data['sell']
        for price, size in asks:
            if price < 1000:
                trade = {"type": "add", "order_id": count, "symbol": "BOND", "dir": "BUY", "price": price, "size": size}
                trades.append(trade)
                count += 1

        bids = data['buy']
        for price, size in bids:
            if price > 1000:
                trade = {"type": "add", "order_id": count, "symbol": "BOND", "dir": "SELL", "price": price, "size": size}
                trades.append(trade)
                count += 1
    return trades
