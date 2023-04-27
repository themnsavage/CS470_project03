# CS470_project03

## Description:
Find solution of np-complete problem in this case 0-1 knapsack problem. Uses two algorithms which are dynamic programming algorithm(brute force) and genetic algorithm(heuristic).

## setup:
- have [python3](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installation/) installed
- have python libraries installed by running the `make setup` command in terminal.

## How to use:
- `make run` will ask for inputs to run algorithms from generated data or data from file, then outputs to console solutions from algorithms and run time and accuracy statistics.
- `make analyze` will run algorithms with generated data and then save data in data directory and also graph the two algorithms.
- `make reduction` will reduce the data you put in the input files `reduce_3sat_to_knapsack.txt` and `reduce_knapsack_to_traveling_salesman.txt`, then export the reduction data into the output files `knapsack_data_from_3sat.txt` and `traveling_salesman_data_from_knapsack.txt`.


