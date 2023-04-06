import random
import json
from app.algorithm_analyzer import Algorithm_Analyzer


class Data_Generator:
    def __init__(self, max_single_weight=80, max_single_value=80):
        self._max_single_weight = max_single_weight
        self._max_single_value = max_single_value
        self._data = None

    def _generate_random_solution(self, max_items):
        solution_item_count = random.randint(1, max_items)
        solution = {"weights": [], "values": [], "max_weight": None, "min_value": None}

        for _ in range(solution_item_count):
            item_weight = random.randint(1, self._max_single_weight)
            item_value = random.randint(1, self._max_single_value)
            if solution["max_weight"] is None and solution["min_value"] is None:
                solution["max_weight"] = item_weight
                solution["min_value"] = item_value
            else:
                solution["max_weight"] = (
                    item_weight
                    if item_weight > solution["max_weight"]
                    else solution["max_weight"]
                )
                solution["min_value"] = (
                    item_value
                    if item_value < solution["min_value"]
                    else solution["min_value"]
                )

            solution["weights"].append(item_weight)
            solution["values"].append(item_value)

        return solution

    def generate_single_data_set(self, max_items=80):
        solution = self._generate_random_solution(max_items)
        other_item_weights = []
        other_item_values = []
        other_item_count = max_items - len(solution["weights"])

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
                "bit": 0,
            }
            info_list.append(info)
        for index in range(len(solution["weights"])):
            info = {
                "weight": solution["weights"][index],
                "value": solution["values"][index],
                "bit": 1,
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
            "solution": {
                "capacity": sum(solution["weights"]),
                "items_used": solution_bitvector,
                "max_value": sum(solution["values"]),
            },
        }
        self._data = single_data
        return single_data

    def generate_multiple_data_set(self, max_items=80):
        data = []
        for problem_set_size in range(2, max_items):
            single_data_set = self.generate_single_data_set(problem_set_size)
            data.append(single_data_set)

        self._data = {"data": data}
        return {"data": data}

    def generate_single_data_set_without_solution(self, max_items=80):
        weights = []
        values = []

        for _ in range(max_items):
            weights.append(random.randint(1, self._max_single_weight))
            values.append(random.randint(1, self._max_single_value))

        max_capacity = sum(weights)
        min_capacity = min(weights)

        capacity = random.randint(min_capacity, max_capacity)

        self._data = {"capacity": capacity, "weights": weights, "values": values}
        return self._data

    def generate_multiple_data_set_without_solution(self, max_items=80):
        multiple_data_sets = {"data": []}
        for single_data_set_size in range(1, max_items + 1):
            single_data_set = self.generate_single_data_set_without_solution(
                max_items=single_data_set_size
            )
            multiple_data_sets["data"].append(single_data_set)

        self._data = multiple_data_sets
        return self._data

    def export_multiple_data_set_with_solution_verify_by_dynamic_programming(
        self, max_items, overall_time_out= None, single_set_time_out= None
    ):
        data = self.generate_multiple_data_set_without_solution(max_items=max_items)
        analyzer = Algorithm_Analyzer()
        total_time = 0
        file_path = "data/dynamic_programming_data_set.json"
        for data_set_index, data_set in enumerate(data["data"]):
            print(f"Current data set: {data_set_index}")
            dynamic_solution = analyzer.run_dynamic_programming_algorithm(data_set)
            
            run_time = dynamic_solution["run_time"]
            total_time += run_time
            if overall_time_out is not None and total_time >= overall_time_out:
                self.export_data_to_json(file_path=file_path)
                return
            if single_set_time_out is not None and run_time >= single_set_time_out:
                self.export_data_to_json(file_path=file_path)
                return
                
            data_set["solution"] = dynamic_solution
        
        self._data = data
        self.export_data_to_json(
            file_path=file_path
        )

    def get_data(self):
        return self._data

    def print_data(self):
        print(json.dumps(self._data, indent=4))

    def export_data_to_json(self, file_path="data/generated_data.json"):
        json_file = json.dumps(self._data, indent=4)

        with open(file_path, "w") as outfile:
            outfile.write(json_file)
