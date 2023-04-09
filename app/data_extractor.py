import copy
import json


class Data_Extractor:
    def __init__(self, file_path="", json_file_path=""):
        self._file_path = file_path
        self._json_file_path = json_file_path
        self._data = {"capacity": None, "weights": [], "values": []}

        if file_path != "":
            self._extract_file_content()
        if json_file_path != "":
            self._extract_json_file_content()

    def _extract_file_content(self):
        with open(self._file_path, "r") as file_data:
            file_lines = file_data.readlines()

        for line in file_lines:
            if self._data["capacity"] == None:
                self._data["capacity"] = int(line)
            elif line != "$":
                weight_and_value = line.split()
                self._data["weights"].append(int(weight_and_value[0]))
                self._data["values"].append(int(weight_and_value[1]))

    def _extract_json_file_content(self):
        with open(self._json_file_path) as json_file_data:
            self._data = json.load(json_file_data)

    def get_data(self):
        return copy.deepcopy(self._data)

    def print_data(self):
        print(json.dumps(self._data, indent=4))

    def convert_json(self, file_path=None):
        self._json_file_path = file_path
        self._extract_json_file_content()
        data = self.get_data()

        capacity = data["capacity"]
        weights = data["weights"]
        values = data["values"]

        with open("data/knapsack_mnsavage.dat", "w") as file:
            file.write(f"{capacity}\n")
            for index in range(len(weights)):
                line = f"{weights[index]} {values[index]}\n"
                file.write(line)
            file.write("$\n")
