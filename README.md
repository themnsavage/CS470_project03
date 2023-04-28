# CS470_project03

![image](https://user-images.githubusercontent.com/60998598/234996445-2dd3a444-62e7-47af-8d9e-9f6eb4a0fdda.png)


## Description:
This project allow user to solve a NP-complete problem, which is the 0-1 knapsack problem by using a brute force(dynamic programming) and heuristic algorithm(gentic algorithm). Also allowing user to NP reduce(mapping) 3sat to 0-1 knapsack and 0-1 knapsack to traveling sales man. The brute force algorithm will give the 100% correct answer, but can be extremely slow. Where the heuristic algorithm will not always give you the best solution, but will give you a good solution while being exponitially faster than the brute force method.

graph of dynamic programming algorithm:  
![image](https://user-images.githubusercontent.com/60998598/234999877-ba6689ff-2c45-439f-8cec-cb3a623469a8.png)

graph of genetic algorithm:  
![image](https://user-images.githubusercontent.com/60998598/234999764-2456f4af-0eff-45b0-9e3b-cb493882780f.png)  

Observing the two graphs above we can see that the dynamic algorithm is exponitial and the genetic algorithm is linear.

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

`Note`: The genetic algorithm has trouble running against big dataset where the best solution is only using one item from the list of items. This is due to the high possibilty for the genetic algorithm to pick a population of overweighted chromosomes(it is very unlikely for a chromosome to only take one item when there is so many items it can picked from) resulting to the whole population dying.

## 3sat to 0-1 knapsack
To map 3sat to knapsack we first reduce 3sat to subset-sum. Consider a 3CNF formula with variables x1,...,xn and clauses c1,...,cr. For each variable xi, we will have two numbers yi and zi in the list. For each clause cj, we will also have two numbers sj and tj. We define all of these numbers by specifying their base 10 representations. The construction is best explained by an example and a picture.  

If the formula is (x1∨x2∨ -x3)∧(-x1∨x2∨-x3), then the base 10 representations of the numbers will look like this: 

![image](https://user-images.githubusercontent.com/60998598/234988970-a16ea5a1-f1ec-4778-aaf9-e5b057dbefa2.png)  

The number yi corresponds to the positive occurrences of xi in the formula while the number zi corresponds to its negative occurrences. It should be clear how to generalize this construction to an arbitrary 3CNF formula. And the list of numbers can clearly be constructed in polynomial time. We claim that a subset of these numbers adds to exactly k if and only if the formula is satisfiable. A key point is that the sum of the numbers can be done column by column, independently, because carries will never occur. After this then we map subset-sum to knapsack by setting capcity to k from the table. Then creating items with value and weights from subset-sums values(knapsack values and weights will be the same). 

## 0-1 knapsack to traveling salesman:
Step one create a Node for every knapsack element like this:  
![image](https://user-images.githubusercontent.com/60998598/235017473-50385df9-23c1-4928-b2c0-f9cf85f9b1b2.png)

step two add node 0 as home and add node n+1 as the turning point like this:  
![image](https://user-images.githubusercontent.com/60998598/235017625-3c780bb6-d7a7-49b5-aa29-2c61499b5fb4.png)

Step three create forward edges from smaller to bigger nodes with the edge being the weight of the node it is point to like this:  
![image](https://user-images.githubusercontent.com/60998598/235017786-1860bca0-a4cf-4138-9ce4-571dbd596c1f.png)

Step four draw backward edges from bigger to smaller and set these edges weight to zero like this:
![image](https://user-images.githubusercontent.com/60998598/235017961-c77077e0-e28c-4992-b49c-68e3b720683a.png)

get output from traveling salesman and the nodes used before the turning point(n+1 node) will be the knapsack solution:
![image](https://user-images.githubusercontent.com/60998598/235018105-3cb45ec1-bde0-46e9-adac-edc661e8ecb0.png)

## setup:
- have [python3](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installation/) installed
- have python libraries installed by running the `make setup` command in terminal.

## How to use:
- `make run` will ask for inputs to run algorithms from generated data or data from file, then outputs to console solutions from algorithms and run time and accuracy statistics.
- `make analyze` will run algorithms with generated data and then save data in data directory and also graph the two algorithms.
- `make reduction` will reduce the np data you put in the input reduction files(`reduce_3sat_to_knapsack.txt` and `reduce_knapsack_to_traveling_salesman.txt`), then export the reduction np data into the output reduction files(`knapsack_data_from_3sat.txt` and `traveling_salesman_data_from_knapsack.txt`).

## Example ways to use project:
- You can use `make run` to solve an example file you have by entering the command 1 and entering the file path
- You can np reduce 3sat to knapsack by putting 3sat data in the input reduction file reduce_3sat_to_knapsack.txt then running the `make reduction` then you can run the output reduction file knapsack_data_from_3sat.txt, by running the `make run` command and entering the filepath(data/output_reduction_files/knapsack_data_from_3sat.txt).

## How can the project be improve:
Right now the genetic algorithm takes three parameters input from the user which are population size, mutation rate, and generations. Something to do in the future is to implement somthing like Rastrigin's function or some paramter tuning algorithm to automatically generate the three parameters the genectic algorithm uses. Instead of just asking the user to guess the best parameters to use for the genetic algorithm.
