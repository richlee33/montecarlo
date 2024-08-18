
# montecarlo
I wrote this Monte Carlo experiment to calculate the probabily of a retirement account reaching $1 Million.

At a high level, this is done by generating randomized annual returns. 
For each year before retirement, The balance is multiplied by the return percentage and added (or subtracted for a negative annual return) to make the new balance.

The experiment is run 500 times and finally, the percentage of runs where the end balance exceeds $1 Million is shown.

##Data and Assumptions
The annual return of the S&P 500 index from 1927 until now can be found at [macrotrends.net](https://www.macrotrends.net/2526/sp-500-historical-annual-returns).

Using this data, the average annual return is 7.9% with a standard deviation of 19.

These values are fed into the `numpy.random.normal` method to generate random return values with a Normal distribution.
Better random annual returns can be had with a distribution model that more accurately fits historical S&P 500 returns.

Always remember: Past performance is no guarantee of future results.

## To Run
Modern version of [python3](https://www.python.org/downloads/), ie. 3.8 or newer.

## Installation
Set up environment:
```sh
$ git clone <repo url>
$ cd montecarlo
$ python3 -m venv .
$ source bin/activate
$ pip install -r requirements.txt
```

## Run
```sh
$ python main.py
```

### Sample Output:
```
====== End Balance Table 500 Runs ======
     start_balance  contribution  end_balance  average_return
0             1000        250000     530956.0        4.860000
1             1000        250000    5340032.0       12.386531
2             1000        250000    4630970.0        9.062449
3             1000        250000     998079.0        4.510000
4             1000        250000     826731.0        7.439388
..             ...           ...          ...             ...
495           1000        250000    1861456.0        9.094082
496           1000        250000    5137429.0       12.177347
497           1000        250000     748437.0        6.220408
498           1000        250000    1839859.0        7.693673
499           1000        250000    2431553.0        7.890612

[500 rows x 4 columns]
====== End Balance Summary Table 500 Runs ======
       start_balance  contribution  end_balance  average_return
count          500.0         500.0        500.0           500.0
mean          1000.0      250000.0    2701162.0             8.0
std              0.0           0.0    3918757.0             3.0
min           1000.0      250000.0     152394.0             1.0
25%           1000.0      250000.0     824622.0             6.0
50%           1000.0      250000.0    1552246.0             8.0
75%           1000.0      250000.0    3082941.0            10.0
max           1000.0      250000.0   48320946.0            16.0
============================================================
Success rate of end balance greater than 1000000: 0.692
```
### Sample End Balance Distribution:
![Sample Plot](docs/Figure_1.png)


## Features
### Simulation variables
Edit the desired values
```shell script
age = 16
start_balance = 1000
retire_age = 65
annual_contribution = 5000
end_balance_goal = 1000000
```

### View plots for annual return distribution and balance each year
For each rep, the annual return percentage distribution plot can be shown by changing the `view_annual_return_plot` value.
Default `False`

Similarly, the balance of the account can be shown in a line plot by changing the `view_annual_balance_plot`.
This is useful to get a visual of the balance over time.  Default `False`

NOTE: These `num_reps` value should be lowered to `10` or less otherwise each repetition will require manually closing the plot for the experiment to conclude.
```shell script
view_annual_return_plot = True
view_annual_balance_plot = True
```
#### Sample Annual Return Distribution:
![Sample Plot](docs/annual_ret_dist.png)

#### Sample Balance Over Time:
![Sample Plot](docs/end_balance_graph.png)

### Output summary table and plots to disk
Useful if running the experiment in a script, that way the plots and summary table can be examined asynchronously.  The files save to the `results` directory.  Default `False`.
```shell script
output_files = True
```