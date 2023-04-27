from app.algorithm_analyzer import Algorithm_Analyzer
from app.data_extractor import Data_Extractor


def main():
    Algorithm_Analyzer().analyze_data_sets(max_items=900)

if __name__ == "__main__":
    main()
