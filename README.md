# CS470_project03

## Description:
Find solution of np-complete problem in this case 0-1 knapsack problem. Uses two algorithms which are dynamic programming algorithm(brute force) and genetic algorithm(heuristic).

## Brute Force:
The brute force algorithm uses dynamic programming, which builds a nxm table where n is the number of values and where m is the numbers of weights from the 0-1 knapsack data. Using the table we can find the best possible value from table[n-1][m-1], also we can find the items that are used in table from working backwards from starting at table[n-1][m-1].

## setup:
- have [python3](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installation/) installed
- have python libraries installed by running the `make setup` command in terminal.

## How to use:
- `make run` will ask for inputs to run algorithms from generated data or data from file, then outputs to console solutions from algorithms and run time and accuracy statistics.
- `make analyze` will run algorithms with generated data and then save data in data directory and also graph the two algorithms.
- `make reduction` will reduce the np data you put in the input files(`reduce_3sat_to_knapsack.txt` and `reduce_knapsack_to_traveling_salesman.txt`), then export the reduction np data into the output files(`knapsack_data_from_3sat.txt` and `traveling_salesman_data_from_knapsack.txt`).


