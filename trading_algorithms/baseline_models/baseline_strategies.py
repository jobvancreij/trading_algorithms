# trading standard strategies basline
import random
from trading_algorithms.simulation_algorithm import *


class Pseudo_random(Trader):
    """
    This class contains the functions to simulate random baseline strategy in this thesis
    Which works as following:
        - Start with 1 btc (defined in the Trader class)
        - make a random prediction with the distribution of the dataset
        - Follow similar pattern of trading strategy 1
    """


    def __init__(self):
        Trader.__init__(self)#interherit the base functions
        self.current_coin = 0 #start with btc
        self.number_of_trades = 0
        self.sequence_len = []
        self.current_sequence = 0

    @store_trades
    def iteration(self, close_price, prediction, BTCUSDT, ETHUSDT):
        """
        This function simulates one minute of trading for pseudo_random
        :param close_price: the ETHBTC exchange rate of this minute
        :param prediction: the prediction from the prediction algorithm for this minute
        :param BTCUSDT: this variable is used by the decorator store trades to store value in Dollars
        :param ETHUSDT: this variable is used by the decorator store trades to store value in Dollars
        """

        if random.randint(0, 100) > 52: #data distribution
            prediction = 0
        else:
            prediction = 1
        #remaining is similar pattern as trading strategy 1
        if self.current_coin != prediction:
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

        # self.value_over_time.append(self.value_in_dollars(BTCUSDT,ETHUSDT))
        # print(self.value_in_dollars(BTCUSDT,ETHUSDT))


class Optimistic(Trader):
    """
    This class contains the functions to simulate the first trading strategy in this thesis
    Which works as following:
        - Start with 1 btc (defined in the Trader class)
        - follow same pattern as trading strategy 1 by determining the prediction variable based on the difference
          between current price and previous price.
        - If the previous exchange rate is higher, add prediction as 1. Since this suggest that bitcoin should be
          bought which is preferable according to the optmistic algorithme when their is an price increase.
          Works other way around for ethereum
    """

    def __init__(self):
        Trader.__init__(self)#interherit the base functions
        self.current_coin = 0
        self.number_of_trades = 0
        self.sequence_len = []
        self.current_sequence = 0
        self.previous_price = 0

    @store_trades
    def iteration(self, close_price, prediction, BTCUSDT, ETHUSDT):
        """
        This function simulates one minute of trading for Optimistic
        :param close_price: the ETHBTC exchange rate of this minute
        :param prediction: the prediction from the prediction algorithm for this minute
        :param BTCUSDT: this variable is used by the decorator store trades to store value in Dollars
        :param ETHUSDT: this variable is used by the decorator store trades to store value in Dollars
        """
        if close_price > self.previous_price:
            prediction = 1

        else:
            prediction = 0

        if self.current_coin != prediction:
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
        self.previous_price = close_price

        # self.value_over_time.append(self.value_in_dollars(BTCUSDT,ETHUSDT))
        # print(self.value_in_dollars(BTCUSDT,ETHUSDT))


# class CrossOver(Trader):
#     """
#     This class contains the functions to simulate the first trading strategy in this thesis
#     Which works as following:
#         - Start with 1 btc (defined in the Trader class)
#         - if a prediction is different than the coin in the current portfolio trade
#     """
#
#     def __init__(self, window_size):
#         Trader.__init__(self)#interherit the base functions
#         self.last_x_prices = []
#         self.current_coin = 0
#         self.window_size = window_size
#         self.number_of_trades = 0
#
#     @store_trades
#     def iteration(self, close_price, prediction, BTCUSDT, ETHUSDT):
#         """
#         This function simulates one minute of trading for CrossOver
#         :param close_price: the ETHBTC exchange rate of this minute
#         :param prediction: the prediction from the prediction algorithm for this minute
#         :param BTCUSDT: this variable is used by the decorator store trades to store value in Dollars
#         :param ETHUSDT: this variable is used by the decorator store trades to store value in Dollars
#         """
#         self.last_x_prices.insert(0, close_price)
#         if len(self.last_x_prices) > self.window_size:
#             self.last_x_prices.pop()
#         if close_price <= np.mean(self.last_x_prices) and self.current_coin == 0:
#             self.buy_eth(close_price)
#             self.current_coin = 1
#             self.number_of_trades += 1
#
#         elif close_price > np.mean(self.last_x_prices) and self.current_coin == 1:
#             self.buy_btc(close_price)
#             self.current_coin = 0
#             self.number_of_trades += 1
#
#         else:
#             pass
#         # self.value_over_time.append(self.value_in_dollars(BTCUSDT,ETHUSDT))
#         # print(self.value_in_dollars(BTCUSDT,ETHUSDT))


# class MA(Trader):
#     """
#     This class contains the functions to simulate the first trading strategy in this thesis
#     Which works as following:
#         - Start with 1 btc (defined in the Trader class)
#         - if a prediction is different than the coin in the current portfolio trade
#     """
#
#     def __init__(self):
#         Trader.__init__(self)#interherit the base functions
#         self.last_20_prices = []
#         self.last_50_prices = []
#         self.current_coin = 0
#         self.number_of_trades = 0
#
#     @store_trades
#     def iteration(self, close_price, prediction, BTCUSDT, ETHUSDT):
#         self.last_20_prices.insert(0, close_price)
#         self.last_50_prices.insert(0, close_price)
#         if len(self.last_20_prices) > 10:
#             self.last_20_prices.pop()
#         if len(self.last_50_prices) > 20:
#             self.last_50_prices.pop()
#
#         if np.mean(self.last_20_prices) < np.mean(self.last_50_prices) and self.current_coin == 0:
#             self.buy_eth(close_price)
#             self.current_coin = 1
#             self.number_of_trades += 1
#
#         elif np.mean(self.last_20_prices) >= np.mean(self.last_50_prices) and self.current_coin == 1:
#             self.buy_btc(close_price)
#             self.current_coin = 0
#             self.number_of_trades += 1
#
#         else:
#             pass  # print('nada')
#         # self.value_over_time.append(self.value_in_dollars(BTCUSDT,ETHUSDT))
#         # print(self.value_in_dollars(BTCUSDT,ETHUSDT))