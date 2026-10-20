# stock class example
# class Stock:
#     def __init__(self, symbol, quantity):
#         self.symbol = symbol
#         self.quantity = quantity
#         self.price = 0

#     def current_price(self, last_available_price):
#         self.price = last_available_price
#-----------------------------------------------------
# allocated_stock example
# allocated_stocks = {
#     "META": 0.40,
#     "AAPL": 0.60
# }


class Portfolio:
    def __init__(self, stocks, allocated_stocks):
        self.stocks = stocks
        self.allocated_stocks = allocated_stocks

    # Calculate the current portfolio value.
    def get_total_value(self):
        total_value = 0

        for stock in self.stocks:
            if stock.price <= 0:
                raise ValueError(f"Invalid price for stock {stock.symbol}")
            total_value += stock.quantity * stock.price

        return total_value

    # Calculate the target values based on portfolio current value
    def target_values(self):
        total_value = self.get_total_value()
        target_values = {}

        for symbol, target_allocation in self.allocated_stocks.items():
            target_value = total_value * target_allocation
            target_values[symbol] = target_value

        return target_values

    def rebalance(self):
        target_values = self.target_values()
        adjustment = {}
        # Assumption: all target stocks exist in self.stocks.
        # Stocks not currently held are represented with quantity = 0.
        # Allocations are valid and sum to 100%.
        for stock in self.stocks: 
            stock_total_value = stock.quantity * stock.price
            target_value = target_values.get(stock.symbol, 0)
            difference = target_value - stock_total_value # Compare current allocation against target allocation.
            adjustment[stock.symbol] = difference/stock.price
        
        return adjustment # Return the required buy/sell operations.
