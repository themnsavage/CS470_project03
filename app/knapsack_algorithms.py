import random
import copy
import sys


class Knapsack_Algorithms:
    """
    Description: algorithms used to solve 0-1 knapsack problem
    """

    def __init__(self, data=None):
        if data == None:
            data = {
                "capacity": None,
                "weights": None,
                "values": None,
                "solution": {"capacity": None, "items_used": None, "max_value": None},
            }
        else:
            self._data = data

        self._genetic_result = {"capacity": None, "items_used": None, "max_value": None}
        self._dynamic_result = {"capacity": None, "items_used": None, "max_value": None}

    def set_data(self, data=None):
        """
        Description: setter function
        Args:
            data (dictionary): set data for algorithms to run against
        """
        self._data = data

    # heuristic algorithm
    def get_genetic_result(self):
        """
        Description: getter function
        Returns:
            dictionary: genetic algorithm solution
        """
        return copy.deepcopy(self._genetic_result)

    def genetic_algorithm(
        self, population_size=10, mutation_probability=0.2, generations=10
    ):
        """
        Description: runs genetic algorithm
        Args:
            population_size (int): number of chromosome in generation
            mutation_probability (float): the probability for a child chromosome to have a mutation
            generations (int): the number of generation that will be run/looped

        Returns:
            dictionary: genetic algorithm solution
        """
        print("Running Genetic Algorithm:")
        population = self._generate_population(population_size)

        for _ in range(generations):
            print(f"\t--generation({_})")
            population = sorted(
                population, key=lambda chromosome: self._calculate_fitness(chromosome)
            )
            next_generation = population[0:2]  # save top two chromosome

            for j in range(int(len(population) / 2) - 1):
                parent_one, parent_two = self._select_chromosomes(population)
                child_one, child_two = self._crossover(parent_one, parent_two)
                if random.uniform(0, 1) < mutation_probability:
                    child_one = self._mutate(child_one)
                if random.uniform(0, 1) < mutation_probability:
                    child_two = self._mutate(child_two)
                next_generation += [child_one, child_two]

            population = [child_one, child_two] + population[2:]

        best = self._get_best(population)

        total_weight = 0
        total_value = 0
        for index in range(len(best)):
            if best[index]:
                total_weight += self._data["weights"][index]
                total_value += self._data["values"][index]

        self._genetic_result["capacity"] = total_weight
        self._genetic_result["max_value"] = total_value
        self._genetic_result["items_used"] = best

        return self.get_genetic_result()

    def _generate_population(self, size):
        """
        Description: generate initial population
        Args:
            size (int): the size of the population generated

        Returns:
            list: list of chromosome
        """
        chromosome_size = len(self._data["weights"])
        population = []
        for _ in range(size):
            chromosome = [0] * chromosome_size
            random_indexes = random.sample(range(chromosome_size), chromosome_size)
            current_weight = 0
            print(f"\t--Creating chromosome{_}--")
            for random_index in random_indexes:
                current_weight += self._data["weights"][random_index]
                chromosome[random_index] = 1

                if current_weight > self._data["capacity"]:
                    chromosome[random_index] = 0
                    break

            population.append(chromosome)

        return population

    def _calculate_fitness(self, chromosome):
        """
        Description: calculate fitness of chromosome
        Args:
            chromosome (list/bit-vector): the chromosome to calculate fitness on

        Returns:
            int: fitness value of given chromosome
        """
        total_weight = 0
        total_value = 0
        # calculate chromosome weight and value
        for index in range(len(chromosome)):
            if chromosome[index] == 1:
                total_weight += self._data["weights"][index]
                total_value += self._data["values"][index]

        if (
            total_weight > self._data["capacity"]
        ):  # chromosome is overweight so set to zero
            return 0
        else:
            return total_value

    def _select_chromosomes(self, population):
        """
        Description: select chromosome from population(better fitness = higher chance to select)
        Args:
            population (list): list of chromosome

        Returns:
            list/bit-vector: chromosome that was selected from population
        """
        return random.choices(
            population=population,
            weights=[self._calculate_fitness(chromosome) for chromosome in population],
            k=2,
        )

    def _crossover(self, parent_one, parent_two):
        """
        Description: create two new chromosome(children) from two given chromosomes(parents)
        Args:
            parent_one (list/bit-vector): chromosome use to crossover
            parent_two (list/bit-vector): chromosome use to crossover

        Returns:
            lists/bit-vectors: return two new chromosome(children chromosome)
        """
        item_count = len(self._data["weights"])
        crossover_point = random.randint(0, item_count - 1)
        child_one = parent_one[0:crossover_point] + parent_two[crossover_point:]
        child_two = parent_two[0:crossover_point] + parent_one[crossover_point:]

        return child_one, child_two

    def _mutate(self, chromosome):
        """
        Description: randomly reverse bit-vector value(0 or 1)
        Args:
            chromosome (list/bit-vector): given chromosome to do mutation on

        Returns:
            list/bit-vector: chromosome with mutation
        """
        item_count = len(self._data["weights"])

        mutation_point = random.randint(0, item_count - 1)
        chromosome[mutation_point] = 1 if chromosome[mutation_point] == 0 else 0

        return chromosome

    def _get_best(self, population):
        """
        Description: get the best chromosome from population based of fitness values
        Args:
            population (list): list of chromosome to search through

        Returns:
            list/bit-vector: chromosome with highest fitness value
        """
        fitness_values = []

        for chromosome in population:
            fitness_values.append(self._calculate_fitness(chromosome))

        max_value = max(fitness_values)
        max_index = fitness_values.index(max_value)
        return population[max_index]

    # brute force
    def get_dynamic_result(self):
        """
        Description: getter function
        Returns:
            dictionary: dynamic programming algorithm solution
        """
        return copy.deepcopy(self._dynamic_result)

    def dynamic_programming(self):
        """
        Description: run dynamic programming algorithm
        Returns:
            dictionary: dynamic programming solution
        """
        print("Running Dynamic Programming Algorithm:")
        table = [
            [0 for w in range(self._data["capacity"] + 1)]
            for i in range(len(self._data["weights"]) + 1)
        ]

        print("\t--Building Table--")
        for i in range(len(self._data["weights"]) + 1):
            for w in range(self._data["capacity"] + 1):
                if i == 0 or w == 0:
                    table[i][w] = 0
                elif self._data["weights"][i - 1] <= w:
                    table[i][w] = max(
                        self._data["values"][i - 1]
                        + table[i - 1][w - self._data["weights"][i - 1]],
                        table[i - 1][w],
                    )
                else:
                    table[i][w] = table[i - 1][w]

        print("\t--Getting Total Value from Table--")
        result = table[len(self._data["weights"])][self._data["capacity"]]
        self._dynamic_result["max_value"] = result

        print("\t--Working Backwards to get Items used and Total Weight--")
        total_weight = 0
        items_used = [0 for i in range(len(self._data["weights"]))]
        w = self._data["capacity"]
        for i in range(len(self._data["weights"]), 0, -1):
            if result <= 0:
                break

            if result == table[i - 1][w]:
                continue
            else:
                total_weight += self._data["weights"][i - 1]
                items_used[i - 1] = 1
                result -= self._data["values"][i - 1]
                w -= self._data["weights"][i - 1]

        self._dynamic_result["capacity"] = total_weight
        self._dynamic_result["items_used"] = items_used

        return self.get_dynamic_result()
