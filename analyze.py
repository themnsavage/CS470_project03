from app.algorithm_analyzer import Algorithm_Analyzer
from app.data_extractor import Data_Extractor


def main():
    Algorithm_Analyzer().analyze_data_sets(max_items=900)
    # Data_Extractor().convert_json(file_path="data/worst_accuracy02.json") # want to export data generated


if __name__ == "__main__":
    main()
