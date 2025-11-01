# src/controller.py
from typing import List, Literal, Optional
from .sorters import BubbleSorter, SelectionSorter, QuickSorter, MergeSorter
from .base_sorter import BaseSorter

# allowed algorithm names for type hinting
AlgorithmName = Literal["bubble", "selection", "quick", "merge"]

class Sorter:
    """
    The main controller class that selects and runs a sorting algorithm.
    """
    
    def __init__(self):
        # This dictionary maps algorithm names (strings) to the 
        # actual class objects.
        self._algorithms: dict[AlgorithmName, type[BaseSorter]] = {
            "bubble": BubbleSorter,
            "selection": SelectionSorter,
            "quick": QuickSorter,
            "merge": MergeSorter
        }

    def _get_algorithm(self, name: AlgorithmName) -> BaseSorter:
        """
        Factory method to get an instance of a sorter.
        """
        sorter_class = self._algorithms.get(name)
        if sorter_class:
            return sorter_class() # Return an INSTANCE of the class
        else:
            raise ValueError(f"Unknown algorithm: {name}. "
                             f"Available: {list(self._algorithms.keys())}")

    def sort_list(
        self,
        algorithm_name: AlgorithmName,
        data: List[int],
        ascending: bool = True
    ) -> List[int]:
        """
        The main public method to sort a list.
        
        Args:
            algorithm_name: The name of the algorithm to use.
            data: The list of integers to sort.
            ascending: Sort order.
        
        Returns:
            A new, sorted list.
        """
        
        # --- Input Validation (as required by Q3.5, Q3.9) ---
        if not isinstance(data, list):
            raise TypeError("Input 'data' must be a list.")
            
        if len(data) > 200000: # 2x1e5
             raise ValueError("List size exceeds the 200,000 element limit.")
             
        if not all(isinstance(x, int) for x in data):
            raise TypeError("All elements in the list must be integers.")

        # --- Get and run the algorithm ---
        try:
            # 1. Get the correct algorithm instance
            sorter = self._get_algorithm(algorithm_name)
            
            # 2. Run its sort method and return the result
            return sorter.sort(data, ascending)
            
        except ValueError as e:
            # Re-raise the error if algorithm name was bad
            print(f"Error: {e}")
            raise # Re-raises the last exception
        except Exception as e:
            print(f"An unexpected error occurred during sorting: {e}")
            raise