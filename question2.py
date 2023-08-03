def max_profit(prices):
    if not prices or len(prices) == 1:
        return 0
    max_profit = 0
    min_price = prices[0]
    for price in prices[1:]:
        potential_profit = price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, price)

    return max_profit

prices1 = [7, 1, 5, 3, 6, 4]
print(max_profit(prices1))

prices2 = [7, 6, 4, 3, 1]
print(max_profit(prices2))


