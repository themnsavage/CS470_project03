# CS470_project03

## Description:
Find solution of np-complete problem in this case 0-1 knapsack problem. Using two algorithms which are dynamic programming algorithm(brute force) and genetic algorithm(heuristic). NP reduction to map problem to and from 0-1 knapsack problem.

## 0-1 knapsack problem:
![image](https://user-images.githubusercontent.com/60998598/234992912-b87e4310-10c3-4747-b3e8-2d315a1e6c9a.png)  

The 0-1 knapsack problem is a np problem where you are given a list of items(with values and weights) and a capacity which is the maximum weight you can carry but cannot go over. The goal is to used the list of items to get the highest possible value without going over the given capacity(Note: you must take a whole item, you cannot take a item partially, hence the 0-1 part in 0-1 knapsack problem).

## Brute Force:
The brute force algorithm uses dynamic programming, which builds a nxm table where n is the number of values and where m is the numbers of weights from the 0-1 knapsack data. Using the table we can find the best possible value from table[n-1][m-1], also we can find the items that are used in table from working backwards from starting at table[n-1][m-1].  

dynamic programming table:  
![image](https://user-images.githubusercontent.com/60998598/234991360-cc01b9ac-2907-417c-9b55-b84493d330ae.png)


## Heuristic:
The Heuristic algorithms is a genetic algorithm that creates an populations of chromosomes which are arrays with the size of the numbers of items in the 0-1 knapsack problem, also containing 0's and 1's where 0 means item was not used and 1 means item was used(bit vector). The genetic algorithm then calculates the fitness values by seeing if the chromosome is over weight(fitness would be 0) and caculate total values of items the chromosome uses. After calculating fitness values of chromosomes then the algorithm will then allow crossovers of chromosomes(two parent chromosomes to create a child chromosome) to happen to create new chromosomes(children chromosomes). The new chromosome also have the chance of having mutations(randomily changing one of the values in the bitvector to 0 or 1). This process will repeat until a given number of generations have passed, then picking the chromosome with the highest fitness value. This algorithms is model by evolution where the strongest survives and mate and the weakest dies and doesn't get to mate.

genetic algorith population, chromosome, gene, crossover:  
![image](https://user-images.githubusercontent.com/60998598/234992289-e7063a6e-7369-440e-904f-decd8d6886e7.png)

## 3sat to knapsack
To map 3sat to knapsack we first reduce 3sat to subset-sum. Consider a 3CNF formula with variables x1,...,xn and clauses c1,...,cr. For each variable xi, we will have two numbers yi and zi in the list. For each clause cj, we will also have two numbers sj and tj. We define all of these numbers by specifying their base 10 representations. The construction is best explained by an example and a picture.  

If the formula is (x1∨x2∨ -x3)∧(-x1∨x2∨-x3), then the base 10 representations of the numbers will look like this: 
![image](https://user-images.githubusercontent.com/60998598/234988970-a16ea5a1-f1ec-4778-aaf9-e5b057dbefa2.png)  

The number yi corresponds to the positive occurrences of xi in the formula while the number zi corresponds to its negative occurrences. It should be clear how to generalize this construction to an arbitrary 3CNF formula. And the list of numbers can clearly be constructed in polynomial time. We claim that a subset of these numbers adds to exactly k if and only if the formula is satisfiable. A key point is that the sum of the numbers can be done column by column, independently, because carries will never occur. After this then we map subset-sum to knapsack by setting capcity to k from the table. Then creating items with value and weights from subset-sums values(knapsack values and weights will be the same). 

## setup:
- have [python3](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installation/) installed
- have python libraries installed by running the `make setup` command in terminal.

## How to use:
- `make run` will ask for inputs to run algorithms from generated data or data from file, then outputs to console solutions from algorithms and run time and accuracy statistics.
- `make analyze` will run algorithms with generated data and then save data in data directory and also graph the two algorithms.
- `make reduction` will reduce the np data you put in the input files(`reduce_3sat_to_knapsack.txt` and `reduce_knapsack_to_traveling_salesman.txt`), then export the reduction np data into the output files(`knapsack_data_from_3sat.txt` and `traveling_salesman_data_from_knapsack.txt`).


