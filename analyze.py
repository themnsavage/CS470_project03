from app.algorithm_analyzer import Algorithm_Analyzer
from app.data_generator import Data_Generator

def main():
    """
    Description: runs analysis on algorithms that run against 0-1 knapsack data
    """
    data = Data_Generator().generate_multiple_data_set(max_items=800)
    analysis_data = Algorithm_Analyzer().analyze_data_sets(data=data)
    Algorithm_Analyzer().graph_data(data=analysis_data["data"], genetic_solution=analysis_data["genetic_solution"], dynamic_solution=analysis_data["dynamic_solution"])


if __name__ == "__main__":
    main()
