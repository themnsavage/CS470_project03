import random
import copy
import sys


class Knapsack_Algorithms:
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
        self._data = data

    # heuristic algorithm
    def get_genetic_result(self):
        return copy.deepcopy(self._genetic_result)

    def genetic_algorithm(
        self, population_size=10, mutation_probability=0.2, generations=10
    ):
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
        length_of_chromosome = len(self._data["weights"])
        return[random.choices([0,1] ,k=length_of_chromosome) for _ in range(size)]

    def _calculate_fitness(self, chromosome):
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
        return random.choices(
            population=population,
            weights=[self._calculate_fitness(chromosome) for chromosome in population],
            k=2,
        )

    def _crossover(self, parent_one, parent_two):
        item_count = len(self._data["weights"])
        crossover_point = random.randint(0, item_count - 1)
        child_one = parent_one[0:crossover_point] + parent_two[crossover_point:]
        child_two = parent_two[0:crossover_point] + parent_one[crossover_point:]

        return child_one, child_two

    def _mutate(self, chromosome):
        item_count = len(self._data["weights"])

        mutation_point = random.randint(0, item_count - 1)
        chromosome[mutation_point] = 1 if chromosome[mutation_point] == 0 else 0

        return chromosome

    def _get_best(self, population):
        fitness_values = []

        for chromosome in population:
            fitness_values.append(self._calculate_fitness(chromosome))

        max_value = max(fitness_values)
        max_index = fitness_values.index(max_value)
        return population[max_index]

    # brute force
    def get_dynamic_result(self):
        return copy.deepcopy(self._dynamic_result)

    def dynamic_programming(self):
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
