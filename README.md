# CS470_project03

## Description:
Find solution of np-complete problem in this case 0-1 knapsack problem. Uses two algorithms which are dynamic programming algorithm(brute force) and genetic algorithm(heuristic).

## 0-1 knapsack problem:
The 0-1 knapsack problem is a np problem where you are given a list of items(with values and weights) and a capacity which is the maximum weight you can carry but cannot go over. The goal is to used the list of items to get the highest possible value without going over the given capacity(Note: you must take a whole item, you cannot take a item partially, hence the 0-1 part in 0-1 knapsack problem).

## Brute Force:
The brute force algorithm uses dynamic programming, which builds a nxm table where n is the number of values and where m is the numbers of weights from the 0-1 knapsack data. Using the table we can find the best possible value from table[n-1][m-1], also we can find the items that are used in table from working backwards from starting at table[n-1][m-1].

## Heuristic:
The Heuristic algorithms is a genetic algorithm that creates an populations of chromosomes which are arrays with the size of the numbers of items in the 0-1 knapsack problem, also containing 0's and 1's where 0 means item was not used and 1 means item was used(bit vector). The genetic algorithm then calculates the fitness values by seeing if the chromosome is over weight(fitness would be 0) and caculate total values of items the chromosome uses. After calculating fitness values of chromosomes then the algorithm will then allow crossovers of chromosomes(two parent chromosomes to create a child chromosome) to happen to create new chromosomes(children chromosomes). The new chromosome also have the chance of having mutations(randomily changing one of the values in the bitvector to 0 or 1). This process will repeat until a given number of generations have passed, then picking the chromosome with the highest fitness value. This algorithms is model by evolution where the strongest survives and mate and the weakest dies and doesn't get to mate.

## setup:
- have [python3](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installation/) installed
- have python libraries installed by running the `make setup` command in terminal.

## How to use:
- `make run` will ask for inputs to run algorithms from generated data or data from file, then outputs to console solutions from algorithms and run time and accuracy statistics.
- `make analyze` will run algorithms with generated data and then save data in data directory and also graph the two algorithms.
- `make reduction` will reduce the np data you put in the input files(`reduce_3sat_to_knapsack.txt` and `reduce_knapsack_to_traveling_salesman.txt`), then export the reduction np data into the output files(`knapsack_data_from_3sat.txt` and `traveling_salesman_data_from_knapsack.txt`).


