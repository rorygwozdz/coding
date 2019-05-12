def makeQueue(queue, data, name):
    if data["type"] == "trade" and data["symbol"] == name:
        queue.push((data["price"], data["size"]))


def returnAverage5(queue):
    return sum([queue.pop()[0] for x in range(5)]) / 5
