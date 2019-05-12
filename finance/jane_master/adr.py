def bz_price(from_exhange):
    data = from_exhange

    if data["type"] == "book" and data["symbol"] == "VALBZ":
        bz_ask, bz_ask_size = min(data["sell"], key=lambda x: x[1])
        bz_bid, bz_bid_size = max(data["buy"], key=lambda x: x[1])
    else:
        return
    return ([bz_ask, bz_ask_size], [bz_bid, bz_bid_size])


def adr_trade(from_exchange, bz_price, count):
    data = from_exchange  # data getting
    trades = []

    if data['type'] == 'book' and data['symbol'] == 'VALE':
        asks = data['sell']
        for price, size in asks:
            if price < bz_price[1][0]:
                trade_e_side = {"type": "add", "order_id": count, "symbol": "VALE",
                                "dir": "BUY", "price": price, "size": size}
                count += 1
                trade_bz_side = {"type": "add", "order_id": count, "symbol": "VALBZ",
                                 "dir": "SELL", "price": bz_price[1][0], "size": bz_price[1][1]}
                count += 1
                trades.extend([trade_e_side, trade_bz_side])

        bids = data['buy']

        for price, size in bids:
            if price > bz_price[0][0]:
                trade_e_side = {"type": "add", "order_id": count, "symbol": "VALE",
                                "dir": "SELL", "price": price, "size": size}
                count += 1
                trade_bz_side = {"type": "add", "order_id": count, "symbol": "VALBZ",
                                 "dir": "BUY", "price": bz_price[0][0], "size": bz_price[0][1]}
                count += 1
                trades.extend([trade_e_side, trade_bz_side])

        return trades


# def adr_flatten(queue, from_exhange, threshold):
#     data = from_exhange  # data getting
#     trades = []
#
#     if data['type'] == 'book' and data['symbol'] == 'VALE':
#         asks = data['sell']
#         for price, size in asks:
#             if price * 10 < current_bz_bid:
#                 trade_e_side = {"type": "add", "order_id": count, "symbol": "VALE",
#                                 "dir": "BUY", "price": price, "size": size}
#                 trade_bz_side = {"type": "add", "order_id": count, "symbol": "VALBZ",
#                                  "dir": "SELL", "price": bz_bid, "size": bz_b_size // 10}  # hit market
#                 trades.append(trade_e_side, trade_bz_side)
#
#         bids = data['buy']
#
#         for price, size in bids:
#             if price * 10 > current_bz_ask:
#                 trade_e_side = {"type": "add", "order_id": count, "symbol": "VALE",
#                                 "dir": "SELL", "price": price, "size": size}
#                 trade_bz_side = {"type": "add", "order_id": count, "symbol": "VALBZ",
#                                  "dir": "BUY", "price": bz_ask, "size": bz_a_size // 10}
#                 trades.append(trade_e_side, trade_bz_side)
#
#     return trades
