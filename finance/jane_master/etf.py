def etf_price(from_exhange, name):
    data = from_exhange

    if data["type"] == "book" and data["symbol"] == name:
        ask, ask_size = min(data["sell"], key=lambda x: x[1])
        bid, bid_size = max(data["buy"], key=lambda x: x[1])
    else:
        return
    return ([ask, ask_size], [bid, bid_size])


def etf_trade(data, goldman, wells, morgan, count):
    etf_bid_theo = 3000 + (2 * goldman[0][1]) + (3 * morgan[0][1]) + (2 * wells[0][1])
    etf_ask_theo = 3000 + (2 * goldman[1][1]) + (3 * morgan[1][1]) + (2 * wells[1][1])

    trades = []

    if data['type'] == 'book' and data['symbol'] == 'XLF':
        asks = data['sell']
        for price, size in asks:
            if price > etf_ask_theo and size >= 10:
                trade_etf_side = {"type": "add", "order_id": count, "symbol": "XLF",
                                  "dir": "BUY", "price": price, "size": size}
                count += 1
                goldman_side = {"type": "add", "order_id": count, "symbol": "GS",
                                "dir": "SELL", "price": goldman[1][0], "size": max(1, size * 2 / 10)}
                count += 1
                wells_side = {"type": "add", "order_id": count, "symbol": "WFC",
                              "dir": "SELL", "price": wells[1][0], "size": max(1, size * 2 / 10)}
                count += 1
                morgan_side = {"type": "add", "order_id": count, "symbol": "MS",
                               "dir": "SELL", "price": morgan[1][0], "size": max(1, size * 3 / 10)}
                count += 1
                bond_side = {"type": "add", "order_id": count, "symbol": "BOND",
                             "dir": "SELL", "price": 1000, "size": max(1, size * 3 / 10)}
                count += 1
                trades.extend([trade_etf_side, morgan_side, wells_side, goldman_side, bond_side])

        bids = data['buy']
        for price, size in bids:
            if price < etf_bid_theo:
                trade_etf_side = {"type": "add", "order_id": count, "symbol": "XLF",
                                  "dir": "SELL", "price": price, "size": size}
                count += 1
                goldman_side = {"type": "add", "order_id": count, "symbol": "GS",
                                "dir": "BUY", "price": goldman[0][0], "size": max(1, size * 2 / 10)}
                count += 1
                wells_side = {"type": "add", "order_id": count, "symbol": "WFC",
                              "dir": "BUY", "price": wells[0][0], "size": max(1, size * 2 / 10)}
                count += 1
                morgan_side = {"type": "add", "order_id": count, "symbol": "MS",
                               "dir": "BUY", "price": morgan[0][0], "size": max(1, size * 3 / 10)}
                count += 1
                bond_side = {"type": "add", "order_id": count, "symbol": "BOND",
                             "dir": "BUY", "price": 1000, "size": max(1, size * 3 / 10)}
                count += 1
                trades.extend([trade_etf_side, morgan_side, wells_side, goldman_side, bond_side])
        return trades
