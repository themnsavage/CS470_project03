from app.data_extractor import Data_Extractor
from app.data_generator import Data_Generator
from app.knapsack_algorithms import Knapsack_Algorithms
from app.algorithm_analyzer import Algorithm_Analyzer


def main():
    extractor = Data_Extractor(json_file_path="data/dynamic_programming_data_set.json")
    extractor._extract_json_file_content()
    data = extractor.get_data()["data"][725]
    
    algorithm = Algorithm_Analyzer()
    genetic_result = algorithm.run_genetic_algorithm(data=data, population_size=4, generations=1500, mutation_probability=0.7)
    dynamic_result = algorithm.run_dynamic_programming_algorithm(data=data)
    
    best_value = dynamic_result["max_value"]
    genetic_value = genetic_result["max_value"]
    print(f"accuracy ratio: {float(genetic_value/best_value)}")
    
    genetic_time = genetic_result["run_time"]
    dynamic_time = dynamic_result["run_time"] 
    
    print(f"is: {float(dynamic_time - genetic_time)}s faster")
    

if __name__ == "__main__":
    main()
