import copy
import json


class Data_Extractor:
    """
    Description: manages data from files and data type conversions
    """

    def __init__(self, file_path="", json_file_path=""):
        self._file_path = file_path
        self._json_file_path = json_file_path
        self._data = {"capacity": None, "weights": [], "values": []}

        if file_path != "":
            self._extract_file_content()
        if json_file_path != "":
            self._extract_json_file_content()

    def _extract_file_content(self):
        """
        Description: extract 0-1 knapsack data from other type file
        """
        with open(self._file_path, "r") as file_data:
            file_lines = file_data.readlines()

        for line in file_lines:
            if "$" in line:
                break
            elif self._data["capacity"] == None:
                self._data["capacity"] = int(line)
            elif line != "$":
                weight_and_value = line.split()
                self._data["weights"].append(int(weight_and_value[0]))
                self._data["values"].append(int(weight_and_value[1]))

    def _extract_json_file_content(self):
        """
        Description: extract 0-1 knapsack data from json file
        """
        with open(self._json_file_path) as json_file_data:
            self._data = json.load(json_file_data)

    def get_data(self):
        """
        Description: get data that was converted or extracted
        Returns:
            dictionary: 0-1 knapsack data
        """
        return copy.deepcopy(self._data)

    def print_data(self):
        """
        Description: print 0-1 knapsack data to terminal
        """
        print(json.dumps(self._data, indent=4))

    def convert_json(self, data=None, file_path=None):
        """
        Description: convert 0-1 knapsack data to file path of other type
        Args:
            data (dictionary): 0-1 knapsack data
            file_path (str): file path to write converted data to
        """
        capacity = data["capacity"]
        weights = data["weights"]
        values = data["values"]

        with open(file_path, "w") as file:
            file.write(f"{capacity}\n")
            for index in range(len(weights)):
                line = f"{weights[index]} {values[index]}\n"
                file.write(line)
            file.write("$\n")

    def extract_three_sat_data(
        self, file_name="data/input_reduction_files/reduce_3sat_to_knapsack.txt"
    ):
        """
        Description: extracts 3sat data
        Args:
            file_name (str): file path where to extract 3sat data

        Returns:
            list: three sat data
        """
        three_sat_data = []

        with open(file_name, "r") as three_sat_file:
            lines = three_sat_file.readlines()

        for line in lines:
            if line == "$":
                break
            else:
                clause = [int(literal) for literal in line.split()]
                three_sat_data.append(clause)
        return three_sat_data

    def export_traveling_salesman_data(
        self,
        traveling_salesman_data=None,
        file_path="data/output_reduction_files/traveling_salesman_data_from_knapsack.txt",
    ):
        """
        Description: export traveling salesman data to file
        Args:
            traveling_salesman_data (list): traveling salesman data to export
            file_path (str): file path to export traveling salesman data to
        """
        with open(file_path, "w") as file:
            for connection in traveling_salesman_data:
                line = ""
                for data in connection:
                    if line == "":
                        line += f"{data}"
                    else:
                        line += f" {data}"
                line += "\n"
                file.write(line)
            file.write("$\n")
