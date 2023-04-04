import copy
import json
class Data_Manager:
    def __init__(self, file_path = '', json_file_path = ''):
        self._file_path = file_path
        self._json_file_path = json_file_path
        self._data = {
            "capacity": None,
            "weights": [],
            "values": []
        }
        
        if file_path != '':
            self._extract_file_content()
        if json_file_path != '':
            self._extract_json_file_content()
            
        
    def _extract_file_content(self):
        with open(self._file_path, "r") as file_data:
            file_lines = file_data.readlines()
        
        for line in file_lines:
            if self._data["capacity"] == None:
                self._data["capacity"] = float(line)
            elif line != "$":
                weight_and_value = line.split()
                self._data["weights"].append(float(weight_and_value[0]))
                self._data["values"].append(float(weight_and_value[1]))
    
    def _extract_json_file_content(self):
        with open(self._json_file_path) as json_file_data:
            self._data = json.load(json_file_data)
        
    def get_data(self):
        return copy.deepcopy(self._data)
    
    def print_data(self):
        path = self._file_path if self._file_path != '' else self._json_file_path
        file_data = f"File Path: {path}\nCapacity: {self._data['capacity']}\nWeights: {self._data['weights']}\nValues: {self._data['values']}"
        print(file_data)