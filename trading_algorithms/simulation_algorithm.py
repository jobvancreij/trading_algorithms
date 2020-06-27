class Trader:
    '''
    Inheritance provides the trading strategies/baseline models with the standard functions needed to simulate trading
    '''
    def __init__(self):
        self.BTC = 1
        self.ETH = 0
        self.trading_fees = 0  # 0.0003#.00075
        self.trade_count = 0
        self.last_exchange_rate = 0
        self.values_over_time_dollars = []
        self.value_over_time_bitcoin = []
        self.value_over_time_ethereum = []

    def current_value_eth(self, exchange_rate):
        """
        Calculate the current portfolio value in terms of ETG
        :param exchange_rate: ETH/BTC exchange rate
        :return: current portofolio value
        """
        if self.BTC != 0:
            return self.BTC / exchange_rate
        elif self.ETH != 0:
            return self.ETH
        raise TypError("Hold no value")

    def current_value_btc(self, exchange_rate):
        """
        Calculate the current portfolio value in terms of BTC
        :param exchange_rate: ETH/BTC exchange rate
        :return: current portofolio value
        """
        if self.BTC != 0:
            return self.BTC
        elif self.ETH != 0:
            return self.ETH * exchange_rate
        raise TypError("Hold no value")

    def value_in_dollars(self, BTCUSDT, ETHUSDT):
        """
        Calculate the current portfolio value in terms of USDT
        :param BTCUSDT: current exchange rate BTC/USDT
        :param ETHUSDT: current exchange rate ETH/USDT
        :return: the current portofio value in USDT
        """
        if self.BTC > 0 and self.ETH == 0: # if portfolio contains btc currently
            return self.BTC * BTCUSDT
        else:
            return self.ETH * ETHUSDT

    def buy_eth(self, exchange_rate):
        """
        Sell ethereum for bitcoin for the current exchange rate
        :param exchange_rate: ETHBTC/exchange rate
        """
        assert self.ETH == 0 #safeguard that ETH is currntly not in portofolio
        transaction_cost = (self.BTC / exchange_rate) * self.trading_fees
        self.ETH = self.BTC / exchange_rate - transaction_cost
        self.BTC = 0

    def buy_btc(self, exchange_rate):
        """
        Sell bitcoin for Ethereum for the current exchange rate

        :param exchange_rate: ETHBTC/exchange rate
        :return:
        """
        assert self.BTC == 0
        self.BTC = self.ETH * exchange_rate - (self.ETH * exchange_rate) * self.trading_fees
        self.ETH = 0

def store_trades(func):
    """
    Function wraps around an iteration in a class that contains a trading strategy, to save the value in
    dollars,eth,btc per minute.
    :param func: the function that contains an iteration trough the trading simulation
    :return: the function that is given as param
    """
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)#run func first
        #args[0] contains the class. add the updates to the list containing values
        args[0].values_over_time_dollars.append(args[0].value_in_dollars(args[3], args[4]))
        args[0].value_over_time_bitcoin.append(args[0].current_value_btc(args[1]))
        args[0].value_over_time_ethereum.append(args[0].current_value_eth(args[1]))
        print(args[0].value_in_dollars(args[3], args[4]))

    return wrapper