from trading_algorithms.simulation_algorithm import *

class conseq_simple(Trader):
    """
    This class contains the functions to simulate the second trading strategy in this thesis
    Which works as following:
        - Start with 1 btc (defined in the Trader class)
        - if a prediction is different than the coin in the current portofolio conseq count is set to 1
        - if the next prediction also sugggest trading the coin is bought, conseq count is set back to 0
        - If conseq count is 1 but the algoirthm suggest holdoing  conseq count is set back to 0
    As a result, the algorithm only trades when two consecutive predictions suggest trading
    """

    def __init__(self):
        Trader.__init__(self)#interherit the base functions
        self.current_coin = 0 #start with bitcoin
        self.conseq_count = 0
        self.number_of_trades = 0
        self.sequence_len = []
        self.current_sequence = 0

    # self.last_close_price = 0

    @store_trades
    def iteration(self, close_price, prediction, BTCUSDT, ETHUSDT):
        """
        This function simulates one minute of trading for trading strategy 2
        :param close_price: the ETHBTC exchange rate of this minute
        :param prediction: the prediction from the prediction algorithm for this minute
        :param BTCUSDT: this variable is used by the decorator store trades to store value in Dollars
        :param ETHUSDT: this variable is used by the decorator store trades to store value in Dollars
        """
        if self.current_coin != prediction:
            """
            Prediction suggest trading
            """
            if self.conseq_count == 1: #if the previous prediction also suggested trading
                if prediction == 0:  # buy btc
                    self.buy_btc(close_price)
                    self.current_coin = 0

                else:  # buy eth
                    self.buy_eth(close_price)
                    self.current_coin = 1
                self.number_of_trades += 1
                self.sequence_len.append(self.current_sequence) #store the sequence of how long a coin was hold
                self.current_sequence = 0
            else: #prediction suggested trading but previous prediction did not
                self.conseq_count += 1 #so set conseq count to 1
                self.current_sequence += 1
        else: #algorithm suggest holding
            self.conseq_count = 0 #make sure if conseq count was 1 set it back to 0
            self.current_sequence += 1
