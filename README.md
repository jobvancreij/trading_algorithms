# Trading algorithms

This library contains the simulation of baseline models and trading strategies used in the thesis
"Algorithmic trading of Ethereum/Bitcoin coinpair with deep learning and big data". <br> 

The baseline models can be found in the folder baseline models --> file baseline strategies <br> 
The trading stategies can be found in the folder trading_strategies --> file trading strategie 1 or 
trading strategie 2 <br> 

Both the trading strategies and baseline models rely on the class defined in the simulation algorithm.
With inheritance the class functions are inherited by the other classes. This allows to only define the base
for simulation once, since all those functions have to be used in all the trading algorithms. <br> 



All trading algorithms/baseline models follow a same code pattern
```python
from trading_algorithms.trading_strategies.trading_strategy_1 import Simple
predictions = [] #list with predictions 
rates = [] ##list with exchange rates ETHBTC 
BTCUSDT = []#list with exchange rates BTCUSDT 
ETHUSDT = []#list with exchange rates ETHUSDT 
trading_algorithm = Simple() 
for i in range(len(predictions)): 
    trading_algorithm.iteration(rates.values[i],predictions[i],BTCUSDT[i],ETHUSDT[i])

```
