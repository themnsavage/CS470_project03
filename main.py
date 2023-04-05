from app.data_extractor import Data_Extractor
from app.data_generator import Data_Generator
from app.knapsack_algorithms import Knapsack_Algorithms

def main():
    generator = Data_Generator()
    generator.generate_single_data_set(max_items=1000)
    
    algorithms = Knapsack_Algorithms(generator.get_data())
    print("Genetic Result:")
    print(algorithms.genetic_algorithm(population_size=50, generations=50, mutation_probability=0.5))
    print(algorithms.dynamic_programming())
    
    
    
if __name__ == "__main__":
    main()