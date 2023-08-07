def maxProfit(prices: list[int]):
    min_price = prices[0]
    max_price = prices[0]
    high_sell = max_price - min_price

    for curr in prices:
        if curr < min_price:
            min_price = curr
            max_price = curr
        elif curr > max_price:
            max_price = curr

        if (max_price-min_price) > high_sell:
            high_sell = (max_price - min_price)

    return high_sell


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
prices = [2, 4, 1]
print(maxProfit(prices))

"""
three pointers 
- max
- min
- curr

assign max = min

loop:
    if curr < min:
        min = curr
        max = curr (max is assigned as curr since we need to sell in the "future" or index greater than current min)
    if curr > max:
        max = curr



"""
