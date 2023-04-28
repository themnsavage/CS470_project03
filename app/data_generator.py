import random
import json


class Data_Generator:
    def __init__(self, max_single_weight=80, max_single_value=80):
        self._max_single_weight = max_single_weight
        self._max_single_value = max_single_value
        self._data = None

    def generate_single_data_set(self, max_items=80):
        weights = []
        values = []

        for _ in range(max_items):
            weights.append(random.randint(1, self._max_single_weight))
            values.append(random.randint(1, self._max_single_value))

        max_capacity = sum(weights) - 1
        min_capacity = int(min(weights))

        capacity = int(max_capacity / 2)  # random.randint(min_capacity, max_capacity)

        self._data = {"capacity": capacity, "weights": weights, "values": values}
        return self._data

    def generate_multiple_data_set(self, max_items=400):
        multiple_data_sets = {"data": []}
        for single_data_set_size in range(5, max_items + 1, 50):
            single_data_set = self.generate_single_data_set(
                max_items=single_data_set_size
            )
            multiple_data_sets["data"].append(single_data_set)

        self._data = multiple_data_sets
        return self._data

    def get_data(self):
        return self._data

    def print_data(self):
        print(json.dumps(self._data, indent=4))

    def export_data_to_json(self, data=None, file_path="data/exported_data.json"):
        json_file = json.dumps(data, indent=4)

        with open(file_path, "w") as outfile:
            outfile.write(json_file)
