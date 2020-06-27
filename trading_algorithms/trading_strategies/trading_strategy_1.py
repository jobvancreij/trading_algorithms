from trading_algorithms.simulation_algorithm import *


class Simple(Trader):
    """
    This class contains the functions to simulate the first trading strategy in this thesis
    Which works as following:
        - Start with 1 btc (defined in the Trader class)
        - if a prediction is different than the coin in the current portfolio trade
    """

    def __init__(self):
        Trader.__init__(self) #interherit the base functions
        self.current_coin = 0 #start with bitcoin
        self.number_of_trades = 0
        self.sequence_len = []
        self.current_sequence = 0

    @store_trades
    def iteration(self, close_price, prediction, BTCUSDT, ETHUSDT):
        """
        This function simulates one minute of trading for trading strategy 1
        :param close_price: the ETHBTC exchange rate of this minute
        :param prediction: the prediction from the prediction algorithm for this minute
        :param BTCUSDT: this variable is used by the decorator store trades to store value in Dollars
        :param ETHUSDT: this variable is used by the decorator store trades to store value in Dollars
        """
        if self.current_coin != prediction: #prediction is different than the current portfolio
            if prediction == 0:  # buy btc
                self.buy_btc(close_price)
                self.current_coin = 0

            else:  # buy eth
                self.buy_eth(close_price)
                self.current_coin = 1
            self.number_of_trades += 1
            self.sequence_len.append(self.current_sequence)
            self.current_sequence = 0
        else:
            self.current_sequence += 1