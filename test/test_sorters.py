# test/test_sorters.py
import pytest
from src.controller import Sorter, AlgorithmName

# --- 1. Define our Test Data ---

# A list of test cases: (input_list, expected_ascending, expected_descending)
TEST_CASES = [
    (
        [5, 2, 9, 1, 5, 6],    # Input
        [1, 2, 5, 5, 6, 9],    # Expected (ascending)
        [9, 6, 5, 5, 2, 1]     # Expected (descending)
    ),
    (
        [],                    # Empty list
        [],
        []
    ),
    (
        [1],                   # Single element
        [1],
        [1]
    ),
    (
        [1, 2, 3, 4],          # Already sorted
        [1, 2, 3, 4],
        [4, 3, 2, 1]
    ),
    (
        [4, 3, 2, 1],          # Reverse sorted
        [1, 2, 3, 4],
        [4, 3, 2, 1]
    ),
    (
        [2, 2, 2, 2],          # All duplicates
        [2, 2, 2, 2],
        [2, 2, 2, 2]
    )
]

# A list of all algorithm names  need to test
ALGORITHMS_TO_TEST: list[AlgorithmName] = ["bubble", "selection", "quick", "merge"]

# --- 2. Create the Test Functions ---

#  create an instance of our controller
sorter = Sorter()

#  pytest's 'parametrize' to run the same test on all algorithm names
@pytest.mark.parametrize("algo", ALGORITHMS_TO_TEST)
def test_all_algorithms(algo: AlgorithmName):
    """
    This single test function will be run 4 times, once for each algorithm.
    It loops through all test cases and checks both ascending and descending order.
    """
    for test_input, expected_asc, expected_desc in TEST_CASES:
        
        # --- Test Ascending ---
        #  copy the input just in case, though our sorter shouldn't modify it
        original_input = test_input.copy() 
        
        result_asc = sorter.sort_list(
            algorithm_name=algo,
            data=original_input,
            ascending=True
        )
        # The main check: is the result correct?
        assert result_asc == expected_asc, \
            f"[{algo} / Ascending] Failed on {test_input}. Expected {expected_asc}, got {result_asc}"
        # Check that the original list was not modified
        assert original_input == test_input, \
            f"[{algo} / Ascending] Original list was modified! {test_input}"

        # --- Test Descending ---
        result_desc = sorter.sort_list(
            algorithm_name=algo,
            data=original_input,
            ascending=False
        )
        # The main check: is the result correct?
        assert result_desc == expected_desc, \
            f"[{algo} / Descending] Failed on {test_input}. Expected {expected_desc}, got {result_desc}"
        # Check that the original list was not modified
        assert original_input == test_input, \
            f"[{algo} / Descending] Original list was modified! {test_input}"

def test_invalid_algorithm():
    """
    Test that our controller gracefully handles an unknown algorithm name.
    """
    with pytest.raises(ValueError):
        # This code is expected to fail with a ValueError
        sorter.sort_list("timsort", [3, 1, 2]) # type: ignore

def test_invalid_data_type():
    """
    Test that our controller rejects lists with non-integers.
    """
    with pytest.raises(TypeError):
        sorter.sort_list("bubble", [1, "a", 3]) # type: ignore

def test_list_size_limit():
    """
    Test that our controller rejects lists that are too large.
    """
    with pytest.raises(ValueError):
        # Create a list with 200,001 elements
        large_list = [1] * (200001) 
        sorter.sort_list("quick", large_list)