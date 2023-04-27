class Np_Reducer:
    def __init__(self):
        self._reduction_table = []
    
    def get_reduction_table(self):
        return self._reduction_table      

    def _is_clause_true(self, literal, clause):
        if literal in clause:
            return 1
        return 0

    def _calculate_row_sum(self, row):
        row.reverse()
        sum = 0
        
        for index, value in enumerate(row):
            sum += 10**index * value
        
        return sum 
            
    def _get_k(self, literal_count, clause_count):
        ones = [1] * literal_count
        threes = [3] * clause_count
        ones.extend(threes)
        return ones
    
    def _get_list_of_literals(self, three_sat_data):
        set_of_literals = set()
        list_of_literals = []
        
        for clause in three_sat_data:
            for literal in clause:
                if literal < 0:
                    set_of_literals.add(literal * -1)
                else:
                    set_of_literals.add(literal)
        
        self._literal_count = len(set_of_literals)
        
        for literal in sorted(set_of_literals):
            list_of_literals.append(literal)
            list_of_literals.append(literal * -1)
        
        return list_of_literals            
    
    def _initialize_reduction_table(self, list_of_literals, three_sat_data):
        row_size = len(list_of_literals) + len(three_sat_data)
        
        for index in range(int(len(list_of_literals)/2)):
            empty_row = [0]*row_size
            empty_row[index] = 1
            self._reduction_table.append(empty_row)
            
            empty_row = [0]*row_size
            empty_row[index] = 1
            self._reduction_table.append(empty_row)
        
        for clause_index, clause in enumerate(three_sat_data):
            empty_row = [0]* row_size
            empty_row[clause_index + len(list_of_literals)] = 1
            self._reduction_table.append(empty_row)
            self._reduction_table.append(empty_row)
            
    
    def _create_reduction_table(self, three_sat_data):
        list_of_literals = self._get_list_of_literals(three_sat_data)
        self._initialize_reduction_table(list_of_literals, three_sat_data)
        
        for row_index, literal in enumerate(list_of_literals):
            for clause_index, clause in enumerate(three_sat_data):
                column_index = clause_index + len(list_of_literals)
                self._reduction_table[row_index][column_index] = self._is_clause_true(literal, clause)

        return self._reduction_table
    
    def three_sat_to_subset_sums(self, three_sat_data):
        subset_sums_data = {
            "subsets":[],
            "k": None
        }
        
        reduction_table = self._create_reduction_table(three_sat_data)
        for row in reduction_table:
            subset_sums_data["subsets"].append(self._calculate_row_sum(row))
        
        k = self._get_k(self._literal_count, len(three_sat_data))
        
        subset_sums_data["k"] = self._calculate_row_sum(k)
        
        return subset_sums_data
    
    def subset_sum_to_knapsack(self, subset_sum_data):
        knapsack_data = {
            "values": [],
            "weights": [],
            "capacity": None
        }
        
        for subset in subset_sum_data["subsets"]:
            knapsack_data["values"].append(subset)
            knapsack_data["weights"].append(subset)
        
        knapsack_data["capacity"] = subset_sum_data["k"]
        
        return knapsack_data
    
    def three_sat_to_knapsack(self, three_sat_data):
        subset_sum_data = self.three_sat_to_subset_sums(three_sat_data)
        knapsack_data = self.subset_sum_to_knapsack(subset_sum_data)
        return knapsack_data
         
    def knapsack_to_traveling_salesman(self, knapsack_data):
        pass