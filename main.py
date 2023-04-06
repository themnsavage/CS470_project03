from app.data_extractor import Data_Extractor
from app.data_generator import Data_Generator
from app.knapsack_algorithms import Knapsack_Algorithms
from app.algorithm_analyzer import Algorithm_Analyzer


def main():
    generator = Data_Generator()
    generator.generate_single_data_set(1500)
    generator.export_multiple_data_set_with_solution_verify_by_dynamic_programming(100)


if __name__ == "__main__":
    main()
