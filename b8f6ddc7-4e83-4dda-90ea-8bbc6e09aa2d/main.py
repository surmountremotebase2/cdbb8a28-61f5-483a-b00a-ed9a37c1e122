from surmount.base_class import Strategy, TargetAllocation
from surmount.data import Asset

class TradingStrategy(Strategy):
    def __init__(self):
        # List of chosen top AI stock tickers.
        self.tickers = ["GOOGL", "AAPL", "MSFT", "NVDA"]
        # Keeping it simple, no additional data required beyond price/volume for now.
        self.data_list = []

    @property
    def interval(self):
        # This strategy doesn't depend on frequent updates, daily data is sufficient.
        return "1day"

    @property
    def assets(self):
        # The assets this strategy will operate on - our list of AI stocks.
        return self.tickers

    @property
    def data(self):
        # Return any additional data required by the strategy - empty in this case.
        return self.data_list

    def run(self, data):
        # Creating a dictionary to set target allocation for each stock.
        # We distribute our investment equally among all the chosen stocks.
        allocation_dict = {ticker: 1.0/len(self.tickers) for ticker in self.tickers}

        # Return the target allocation.
        # The TargetAllocation object encapsulates our desired allocations.
        return TargetAllocation(allocation_dict)