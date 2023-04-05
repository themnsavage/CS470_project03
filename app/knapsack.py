import random
import copy
class Knapsack:
    def __init__(self, data):
        self._data = data
        self._genetic_result = {
            "total_weight": None,
            "total_value": None,
            "items_used": None
        } 
    
    #heuristic algorithm
    def get_genetic_result(self):
        return copy.deepcopy(self._genetic_result)
    
    def genetic_algorithm(self, max_weight = 10, population_size = 10, mutation_probability = 0.2, generations = 10):
        population = self._generate_population(population_size)
        
        for _ in range(generations):
            parent_one, parent_two = self._select_chromosomes(population)
            child_one, child_two = self._crossover(parent_one, parent_two)
            
            if random.uniform(0, 1) < mutation_probability:
                child_one = self._mutate(child_one)
            if random.uniform(0, 1) < mutation_probability:
                child_two = self._mutate(child_two)
            
            population = [child_one, child_two] + population[2:]
        
        best = self._get_best(population)
        
        total_weight = 0
        total_value = 0
        for index in range(len(best)):
            if best[index]:
                total_weight += self._data["weights"][index]
                total_value += self._data["values"][index]
        
        self._genetic_result["total_weight"] = total_weight
        self._genetic_result["total_value"] = total_value
        self._genetic_result["items_used"] = best
        
        return self.get_genetic_result()
    
    def _generate_population(self, size):
        population = []
        item_count = len(self._data["weights"])
        for _ in range(size):
            genes = [0, 1]
            chromosome = []
            for _ in range(item_count):
                chromosome.append(random.choice(genes))
            population.append(chromosome)
        return population
    
    def _calculate_fitness(self, chromosome):
        total_weight = 0
        total_value = 0
        #calculate chromosome weight and value
        for index in range(len(chromosome)):
            if chromosome[index] == 1: 
                total_weight += self._data["weights"][index]
                total_value += self._data["values"][index]
        
        if total_weight > self._data["capacity"]: #chromosome is overweight so set to zero
            return 0
        else:
            return total_value

    def _select_chromosomes(self, population):
        fitness_values = []
        #calculate fitness for all chromosomes
        for chromosomes in population:
            fitness_values.append(self._calculate_fitness(chromosomes))
        #calculate ration using lambda function
        fitness_values = [float(index)/sum(fitness_values) for index in fitness_values]
        #choose two random parents
        parent_one = random.choices(population, weights=fitness_values, k=1)[0]
        parent_two = random.choices(population, weights=fitness_values, k=1)[0]
        
        return parent_one, parent_two
    
    def _crossover(self, parent_one, parent_two):
        item_count = len(self._data["weights"])
        crossover_point = random.randint(0, item_count-1)
        child_one = parent_one[0:crossover_point]+parent_two[crossover_point:]
        child_two = parent_two[0:crossover_point]+parent_one[crossover_point:]
        
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

    #brute force
    def dynamic_programming(self):
        pass