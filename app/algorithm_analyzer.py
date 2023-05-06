import time
import matplotlib.pyplot as plt
import numpy as np
from app.knapsack_algorithms import Knapsack_Algorithms
from app.data_generator import Data_Generator


class Algorithm_Analyzer:
    """
    Description: use to analyze algorithms used to solve 0-1 knapsack problem
    """

    def __init__(self):
        self._algorithm = Knapsack_Algorithms()
        self._test_data = None
        self._solution_data = None

    def set_test_data(self, test_data):
        """
        Description: setter function
        Args:
            test_data (dictionary): data used to set private variable _test_data
        """
        self._test_data = test_data

    def get_test_data(self):
        """
        Description: getter function
        Returns:
            dictionary: return private _test_data variable
        """
        return self._test_data

    def run_genetic_algorithm(
        self, data=None, population_size=10, mutation_probability=0.2, generations=10
    ):
        """
        Description: runs genetic algorithm and return solution and analysis data
        Args:
            data (dictionary): knapsack data to run genetic algorithm against
            population_size (int): genetic algorithm population size parameter
            mutation_probability (float): genetic algorithm mutation probability parameter
            generations (int): number of generation the genetic algorithm will run

        Returns:
            dictionary: genetic algorithm run time and solution
        """
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
        """
        Description: runs genetic algorithm and return solution and analysis data
        Args:
            data (dictionary): knapsack data to run dynamic programming algorithm against

        Returns:
            dictionary: dynamic algorithm solution and run time
        """
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
        data=None,
        population_size=5,
        mutation_probability=0.7,
        generations=1200,
    ):
        """
        Description: runs both algorithms(genetic and dynamic programming) and graphs data
        Args:
            max_items (int): genetic algorithm parameter
            population_size (int): genetic algorithm parameter
            mutation_probability (float): genetic algorithm parameter
            generations (int): genetic algorithm parameter
        """
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

        self._graph_data(
            data=data,
            genetic_solution=genetic_solutions,
            dynamic_solution=dynamic_solutions,
        )

    def _graph_data(self, data=None, genetic_solution=None, dynamic_solution=None):
        """
        Description: graphs both algorithms
        Args:
            data (dictionary): 0-1 knapsack data used
            genetic_solution (dictionary): genetic algorithm solution from running data
            dynamic_solution (dictionary): dynamic algorithm solution from running data
        """
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
            if (
                genetic_max_values[index] / dynamic_max_values[index]
            ) < min_accuracy or index_min_accuracy is None:
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

        # graphing plot
        x = data_set_sizes
        y = genetic_run_times
        n = accuracies
        # plt.subplot(1,2,1)
        fig, ax = plt.subplots()

        my_model = np.poly1d(np.polyfit(x, y, 3))
        my_line = np.linspace(1, int(max(x)+1), int(max(y) + 1))
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
        my_line = np.linspace(1, int(max(x)), int(max(y) + 1))
        plt.scatter(x, y, color="red")
        plt.plot(my_line, my_model(my_line))
        plt.title("Dynamic Programming Algorithm")
        plt.xlabel("Data Size")
        plt.ylabel("Run Time")

        plt.show()
