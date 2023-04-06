from app.data_extractor import Data_Extractor
from app.data_generator import Data_Generator
from app.knapsack_algorithms import Knapsack_Algorithms
from app.algorithm_analyzer import Algorithm_Analyzer


def main():
    extractor = Data_Extractor(json_file_path="data/dynamic_programming_data_set.json")
    extractor._extract_json_file_content()
    data = extractor.get_data()["data"][725]
    print(data)
    
    algorithm = Knapsack_Algorithms(data=data)
    genetic_result = algorithm.genetic_algorithm()["max_value"]
    best_value = data["solution"]["max_value"]
    
    print(f"accuracy ratio: {float(genetic_result/best_value)}")

if __name__ == "__main__":
    main()
