from app.data_extractor import Data_Extractor
from app.data_generator import Data_Generator
from app.knapsack_algorithms import Knapsack_Algorithms
from app.algorithm_analysis import Algorithm_Analysis


def main():
    generator = Data_Generator()
    generator.generate_single_data_set(max_items=1000)
    single_data_set = generator.get_data()

    analyzer = Algorithm_Analysis()
    analyzer.set_test_data(single_data_set)

    analyzer.set_test_data(None)
    print("genetic solution data:")
    print(analyzer.run_genetic_algorithm(data=single_data_set, population_size=900, mutation_probability=0.3, generations=10))

    print("dynamic solution data:")
    print(analyzer.run_dynamic_programming_algorithm(data=single_data_set))


if __name__ == "__main__":
    main()
