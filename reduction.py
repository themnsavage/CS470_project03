from app.np_reducer import Np_Reducer

def main():
    three_sat_data = [
        [1, 2, -3],
        [-1, 2, -3]
    ]
    
    reducer = Np_Reducer()
    knapsack_data = reducer.three_sat_to_knapsack(three_sat_data)
    print(knapsack_data)


if __name__ == "__main__":
    main()