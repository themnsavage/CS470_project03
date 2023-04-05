import random
import json
class Data_Generator:
    def __init__(self, max_items=80, max_single_weight = 80, max_single_value = 80):
        self._max_items = max_items
        self._max_single_weight = max_single_weight
        self._max_single_value = max_single_value
        self._data = self._generate_random_data()
    
    def _generate_random_solution(self, max_items):
        solution_item_count =random.randint(1, max_items)
        solution = {
            "weights": [],
            "values": [],
            "max_weight": None,
            "min_value": None
        }
        
        for _ in range(solution_item_count):
            item_weight = random.randint(1,self._max_single_weight) 
            item_value = random.randint(1,self._max_single_value)
            if solution["max_weight"] is None and solution["min_value"] is None:
                solution["max_weight"] = item_weight
                solution["min_value"] = item_value
            else:
                solution["max_weight"] = item_weight if item_weight > solution["max_weight"] else solution["max_weight"]
                solution["min_value"] = item_value if item_value < solution["min_value"] else solution["min_value"]
            
            solution["weights"].append(item_weight)
            solution["values"].append(item_value)
        
        return solution
        
        
    def _generate_random_data(self):
        data = []
        for problem_set_size in range(2, self._max_items):
            solution = self._generate_random_solution(problem_set_size)
            other_item_weights = []
            other_item_values = []
            other_item_count = problem_set_size - len(solution["weights"])
            
            for _ in range(other_item_count):
                other_item_weight = random.randint(1, solution["max_weight"])
                other_item_value = random.randint(1, solution["min_value"])
                other_item_weights.append(other_item_weight)
                other_item_values.append(other_item_value)
            
            info_list = []
            for index in range(len(other_item_weights)):
                info = {
                    "weight": other_item_weights[index],
                    "value": other_item_values[index],
                    "bit": 0
                }
                info_list.append(info)
            for index in range(len(solution["weights"])):
                info = {
                    "weight": solution["weights"][index],
                    "value": solution["values"][index], 
                    "bit": 1
                    }
                info_list.append(info)
            random.shuffle(info_list)
            
            weights = []
            values = []
            solution_bitvector = []
            
            for info in info_list:
                weights.append(info["weight"])
                values.append(info["value"])
                solution_bitvector.append(info["bit"])
            
            single_data = {
                "capacity": sum(solution["weights"]),
                "weights": weights,
                "values": values,
                "items_used": solution_bitvector,
                "max_value": sum(solution["values"])
            }
            
            data.append(single_data)
        
        return {"data":data}
    
    def get_data(self):
        return self._data
    
    def print_data(self):
        print(json.dumps(self._data, indent=4))
    
    def export_data_to_json(self, file_path='data/generated_data.json'):
        json_file = json.dumps(self._data, indent=4)
        
        with open(file_path, "w") as outfile:
            outfile.write(json_file)