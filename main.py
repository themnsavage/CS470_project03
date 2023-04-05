from app.data_extractor import Data_Extractor
from app.data_generator import Data_Generator
from app.knapsack_algorithms import Knapsack_Algorithms

def main():
    generator = Data_Generator()
    generator.generate_multiple_data_set(max_items=50)
    multi_data_set = generator.get_data()
    algorithms = Knapsack_Algorithms()
    for data_set in multi_data_set["data"]:
        algorithms.set_data(data_set)
        print(algorithms.genetic_algorithm(population_size=3000, generations=10, mutation_probability=0.05))
        print(algorithms.dynamic_programming())
    
    
    
if __name__ == "__main__":
    main()