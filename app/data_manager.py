import copy
class Data_Manager:
    def __init__(self, file_path):
        self._file_path = file_path
        self._data = {
            "capacity": None,
            "weights": [],
            "values": []
        }
        self._extract_file_content()
        
    def _extract_file_content(self):
        with open(self._file_path, "r") as data_file:
            file_lines = data_file.readlines()
        
        for line in file_lines:
            if self._data["capacity"] == None:
                self._data["capacity"] = float(line)
            elif line != "$":
                weight_and_value = line.split()
                self._data["weights"].append(float(weight_and_value[0]))
                self._data["values"].append(float(weight_and_value[1]))
    
    def get_data(self):
        return copy.deepcopy(self._data)
    
    def print_file_data(self):
        file_data = f"File Path: {self._file_path}\nCapacity: {self._data['capacity']}\n Weights: {self._data['weights']}\nValues: {self._data['values']}"
        print(file_data)