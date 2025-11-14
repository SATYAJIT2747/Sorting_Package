

---

# Sorting_Package (Assignment 3 - Q3)


This project is a Python package created for Q3 of the SSD Assignment 3. It provides a modular and extensible framework for sorting lists of integers using various algorithms.

## Features

* **4 Sorting Algorithms:** Implements Bubble Sort, Selection Sort, Quick Sort, and Merge Sort.
* **Abstract Base Class:** Uses BaseSorter (an ABC) to enforce a common `sort()` interface for all algorithms.
* **Controller Class:** A central Sorter class acts as a factory to dynamically select the correct algorithm based on a string parameter.
* **Order Control:** Sorts in both ascending and descending order.
* **Non-Destructive:** All sorting methods return a new sorted list, leaving the original input list unmodified.
* **Fully Tested:** Includes a pytest suite that verifies the correctness of all 4 algorithms, including edge cases and error handling.

---

## Project Structure

The project follows a standard Python package structure:

```
Sorting_Package/
├── .git/                 (Git repository history)
├── src/                  (The main Python package source)
│   ├── __init__.py
│   ├── base_sorter.py    (The ABC "blueprint")
│   ├── controller.py     (The main Sorter "factory" class)
│   └── sorters.py        (All algorithm implementations)
├── test/                 (The Pytest package)
│   ├── __init__.py
│   └── test_sorters.py   (All unit tests)
├── input.txt             (Sample input for main.py)
└── main.py               (Runnable demo script)
```

---

## Design Rationale

The code was designed using a modular, extensible, and decoupled approach, following modern software design patterns.

### The "Blueprint" 

`src/base_sorter.py` defines an Abstract Base Class (ABC) called `BaseSorter`.

* This class establishes a **contract** by defining an `@abstractmethod` called `sort()`.
* This guarantees that any new algorithm class we create must have a `sort()` method, ensuring a consistent interface.

### The "Implementations" 

`src/sorters.py` holds all the concrete algorithm classes (`BubbleSorter`, `QuickSorter`, etc.).

* Each class inherits from `BaseSorter`.
* Each provides its own implementation of `sort()`, fulfilling the contract.

### The "Controller" 

`src/controller.py` contains the `Sorter` class, which is the main public face of the package.

* It follows a **Factory Pattern**.
* Instead of knowing BubbleSorter vs QuickSorter, the user interacts with `Sorter`.
* `Sorter` holds a dictionary (`self._algorithms`) mapping algorithm names (`"bubble"`) to the classes.
* When the user calls `sort_list(algorithm_name="bubble")`, the controller:

  * Finds `"bubble"` in the dictionary,
  * Instantiates `BubbleSorter`,
  * Calls its `sort()` method.

### Safety and Constraints 

* **Non-Destructive :**
  All sorters (except Merge Sort, which does it naturally) immediately call `data.copy()` to create a `new_data` list.

* **Validation :**
  The controller validates:

  * data is a list
  * all items are integers
  * list length ≤ 200,000

---

## How to Run

### 1. Running the Demo (`main.py`)

The `main.py` script is a command-line tool to showcase the sorter. It reads numbers from `input.txt` and prints the sorted list.

**Usage:**

```
python main.py <input_file> -a <algorithm_name> -o <order>
```

* `algorithm_name`: `bubble`, `selection`, `quick`, `merge`
* `order`: `asc` (default) or `desc`

**Examples:**

```
python main.py input.txt -a quick
python main.py input.txt -a merge -o desc
python main.py input.txt -a bubble > output.txt
```

(Last one redirects output as required.)

---

## Testing Strategy 

A dedicated test package (`test/`) was created to ensure correctness of all algorithms and error handling.

### 1. Test Design

`test/test_sorters.py` uses pytest.

* A single test function `test_all_algorithms` tests all four sorters.
* Achieved using:

```
@pytest.mark.parametrize("algo", ["bubble", "selection", "quick", "merge"])
```

### 2. Test Case Development

Covers standard, edge, and special cases:

* **Standard:**
  `[5, 2, 9, 1, 5, 6]`
* **Edge Cases:**
  `[]`, `[1]`
* **Pre-Sorted:**
  `[1, 2, 3, 4]`, `[4, 3, 2, 1]`
* **Special:**
  `[2, 2, 2, 2]`

### 3. Test Verification

For each algorithm:

1. Ascending sort matches expected.
2. Descending sort matches expected reverse-sorted.
3. Original input list remains unchanged.

### 4. Error Handling Tests

Additional tests:

* `test_invalid_algorithm`
* `test_invalid_data_type`
* `test_list_size_limit`

These verify correct raising of `ValueError` or `TypeError`.

### To Run Tests

```
pip install pytest
pytest
```

You should see all 7 tests pass.

---

## Assumptions

* **`main.py` Input:**
  The demo script reads space-separated integers from a text file.

---

## Git & Submission (Q3)

This project was developed using Git, as required.
The master branch contains the complete, working implementation for Q3.

