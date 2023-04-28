import json
from app.data_extractor import Data_Extractor
from app.data_generator import Data_Generator
from app.knapsack_algorithms import Knapsack_Algorithms
from app.algorithm_analyzer import Algorithm_Analyzer


def main():
    """
    Description: ask user for input to run algorithms on 0-1 knapsack data
    """
    data = None
    option = input("Enter 0 for generated data or Enter 1 to read data from file: ")
    if option == "0":
        data_size = int(input("Enter data size(e.g. 1500): "))
        data = Data_Generator().generate_single_data_set(max_items=data_size)
    else:
        file_path = input(
            "Enter file path(e.g. data/output_reduction_files/knapsack_data_from_3sat.txt): "
        )
        file_type = file_path.split("/")[-1].split(".")[-1]
        if file_type == "json":
            data = Data_Extractor(json_file_path=file_path).get_data()
        else:
            data = Data_Extractor(file_path=file_path).get_data()
            print(data)

    population_size = int(input("Enter genetic alg. population size(e.g. 10): "))
    mutations_probability = float(
        input("Enter genetic alg. mutation probability(e.g. 0.7): ")
    )
    generation = int(input("Enter genetic alg. numbers of generations(e.g. 1000): "))

    genetic_solution = Algorithm_Analyzer().run_genetic_algorithm(
        data=data,
        population_size=population_size,
        mutation_probability=mutations_probability,
        generations=generation,
    )
    print(f"genetic algorithm solution:\n{json.dumps(genetic_solution, indent=4)}")

    dynamic_solution = Algorithm_Analyzer().run_dynamic_programming_algorithm(data=data)
    print(
        f"dynamic programming algorithm solution:\n{json.dumps(dynamic_solution, indent=4)}"
    )

    print(
        f'genetic algorithm was {dynamic_solution["run_time"] - genetic_solution["run_time"]}s faster, with {genetic_solution["max_value"]/dynamic_solution["max_value"]} accuracy'
    )


if __name__ == "__main__":
    main()
