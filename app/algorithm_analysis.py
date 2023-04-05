import time
from app.knapsack_algorithms import Knapsack_Algorithms
class Algorithm_Analysis:
    def __init__(self):
        self._algorithm = Knapsack_Algorithms()
        self._test_data = None
        self._solution_data = None
                
    def set_test_data(self, test_data):
        self._test_data = test_data
    
    def get_test_data(self):
        return self._test_data
    
    def run_genetic_algorithm(self, data=None, population_size = 10, mutation_probability = 0.2, generations = 10):
        if data is not None: 
            self._algorithm.set_data(data)
        
        start_time = time.time()
        genetic_solution = self._algorithm.genetic_algorithm(population_size=population_size,mutation_probability=mutation_probability,generations=generations)
        run_time = time.time() - start_time
        
        return {
            "run_time": run_time,
            "capacity": genetic_solution["capacity"],
            "item_used": genetic_solution["item_used"],
            "max_value": genetic_solution["max_value"]
        }
    
    def run_dynamic_programming_algorithm(self, data=None):
        if data is not None: 
            self._algorithm.set_data(data)
        
        start_time = time.time()
        dynamic_solution = self._algorithm.dynamic_programming()
        run_time = time.time() - start_time
        
        return {
            "run_time": run_time,
            "capacity": dynamic_solution["capacity"],
            "item_used": dynamic_solution["item_used"],
            "max_value": dynamic_solution["max_value"]
        }