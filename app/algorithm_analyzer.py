import time
import matplotlib.pyplot as plt
import numpy as np
from app.knapsack_algorithms import Knapsack_Algorithms
from app.data_generator import Data_Generator


class Algorithm_Analyzer:
    def __init__(self):
        self._algorithm = Knapsack_Algorithms()
        self._test_data = None
        self._solution_data = None

    def set_test_data(self, test_data):
        self._test_data = test_data

    def get_test_data(self):
        return self._test_data

    def run_genetic_algorithm(
        self, data=None, population_size=10, mutation_probability=0.2, generations=10
    ):
        if data is not None:
            self._algorithm.set_data(data)

        start_time = time.time()
        genetic_solution = self._algorithm.genetic_algorithm(
            population_size=population_size,
            mutation_probability=mutation_probability,
            generations=generations,
        )
        run_time = time.time() - start_time

        return {
            "run_time": run_time,
            "capacity": genetic_solution["capacity"],
            "items_used": genetic_solution["items_used"],
            "max_value": genetic_solution["max_value"],
        }

    def run_dynamic_programming_algorithm(self, data=None):
        if data is not None:
            self._algorithm.set_data(data)

        start_time = time.time()
        dynamic_solution = self._algorithm.dynamic_programming()
        run_time = time.time() - start_time

        return {
            "run_time": run_time,
            "capacity": dynamic_solution["capacity"],
            "items_used": dynamic_solution["items_used"],
            "max_value": dynamic_solution["max_value"],
        }

    def analyze_data_sets(
        self,
        max_items=1000,
        population_size=5,
        mutation_probability=0.7,
        generations=1200,
    ):
        data = Data_Generator().generate_multiple_data_set(max_items=max_items)
        genetic_solutions = []
        dynamic_solutions = []

        for data_set in data["data"]:
            genetic_solutions.append(
                self.run_genetic_algorithm(
                    data=data_set,
                    population_size=population_size,
                    mutation_probability=mutation_probability,
                    generations=generations,
                )
            )

            dynamic_solutions.append(
                self.run_dynamic_programming_algorithm(data=data_set)
            )

        Data_Generator().export_data_to_json(data=data)

        self._graph_data(
            data=data,
            genetic_solution=genetic_solutions,
            dynamic_solution=dynamic_solutions,
        )

    def _graph_data(self, data=None, genetic_solution=None, dynamic_solution=None):
        # data for plots
        data_set_sizes = []
        genetic_run_times = []
        dynamic_run_times = []
        genetic_max_values = []
        dynamic_max_values = []
        accuracies = []

        for index, data_set in enumerate(data["data"]):
            data_set_sizes.append(len(data_set["weights"]))
            genetic_run_times.append(genetic_solution[index]["run_time"])
            dynamic_run_times.append(dynamic_solution[index]["run_time"])
            genetic_max_values.append(genetic_solution[index]["max_value"])
            dynamic_max_values.append(dynamic_solution[index]["max_value"])
            accuracies.append(
                round(genetic_max_values[index] / dynamic_max_values[index], 2)
            )

        # save data set where genetic alg. had worst accuracy
        min_accuracy = 1.0
        index_min_accuracy = None
        for index, data_set in enumerate(data["data"]):
            if (genetic_max_values[index] / dynamic_max_values[index]) < min_accuracy or index_min_accuracy is None:
                min_accuracy = genetic_max_values[index] / dynamic_max_values[index]
                index_min_accuracy = index

        data["data"][index_min_accuracy]["genetic_max_value"] = genetic_max_values[
            index_min_accuracy
        ]
        data["data"][index_min_accuracy]["dynamic_max_value"] = dynamic_max_values[
            index_min_accuracy
        ]
        data["data"][index_min_accuracy]["genetic_items_used"] = genetic_solution[
            index_min_accuracy
        ]["items_used"]
        data["data"][index_min_accuracy]["dynamic_items_used"] = dynamic_solution[
            index_min_accuracy
        ]["items_used"]

        Data_Generator().export_data_to_json(
            data=data["data"][index_min_accuracy], file_path="data/worst_accuracy.json"
        )

        # graphing plots
        max_x = data_set_sizes[-1]

        x = data_set_sizes
        y = genetic_run_times
        n = accuracies
        # plt.subplot(1,2,1)
        fig, ax = plt.subplots()

        my_model = np.poly1d(np.polyfit(x, y, 3))
        my_line = np.linspace(1, max_x, int(max(y) + 1))
        ax.scatter(x, y, color="green")
        for i, txt in enumerate(n):
            ax.annotate(txt, (x[i], y[i]))
        plt.plot(my_line, my_model(my_line))
        plt.title("Genetic Algorithm")
        plt.xlabel("Data Size")
        plt.ylabel("Run Time")
        plt.show()

        # plt.subplot(1,2,2)
        x = data_set_sizes
        y = dynamic_run_times
        my_model = np.poly1d(np.polyfit(x, y, 3))
        my_line = np.linspace(1, max_x, int(max(y) + 1))
        plt.scatter(x, y, color="red")
        plt.plot(my_line, my_model(my_line))
        plt.title("Genetic Algorithm")
        plt.xlabel("Data Size")
        plt.ylabel("Run Time")

        plt.show()
