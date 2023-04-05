from app.data_extractor import Data_Extractor
from app.data_generator import Data_Generator
from app.knapsack_algorithms import Knapsack_Algorithms

def main():
    file_path = 'data/data01.txt'
    json_file_path = 'data/data01.json'
    multiple_data_path = 'data/multiple_data.json'
    
    txt_extractor = Data_Extractor(file_path=file_path)
    json_extractor = Data_Extractor(json_file_path=json_file_path)
    multiple_data_extractor = Data_Extractor(json_file_path=multiple_data_path)
    
    print("txt manager data:")
    txt_extractor.print_data()
    print("json manager data:")
    json_extractor.print_data()
    print("multiple data manager data:")
    multiple_data_extractor.print_data()
    
    algorithms = Knapsack_Algorithms(json_extractor.get_data())
    print("Genetic Result:")
    print(algorithms.genetic_algorithm(population_size=50, generations=1000))
    
    generator = Data_Generator()
    generator.export_data_to_json()
    
    
    
if __name__ == "__main__":
    main()