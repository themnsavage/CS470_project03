from app.np_reducer import Np_Reducer
from app.data_extractor import Data_Extractor
def main():
    three_sat_data = Data_Extractor().extract_three_sat_data()
    knapsack_data_from_three_sat = Np_Reducer().three_sat_to_knapsack(three_sat_data)
    Data_Extractor().convert_json(data=knapsack_data_from_three_sat, file_path="data/output_reduction_files/knapsack_data_from_3sat.txt")
    
    knapsack_data = Data_Extractor(file_path="data/input_reduction_files/reduce_knapsack_to_traveling_salesman.txt").get_data()
    traveling_salesman_data = Np_Reducer().knapsack_to_traveling_salesman(knapsack_data)
    Data_Extractor().export_traveling_salesman_data(traveling_salesman_data)

if __name__ == "__main__":
    main()