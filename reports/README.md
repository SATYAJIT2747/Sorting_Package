

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
│   ├── controller.py      (The main Sorter "factory" class)
│   └── sorters.py         (All algorithm implementations)
├── test/                 (The Pytest package)
│   ├── __init__.py
│   └── test_sorters.py   (All unit tests)
├── input.txt             (Sample input for main.py)
└── main.py               (Runnable demo script)
```

---

## How to Run

### 1. Running the Tests (Q3.3)

This is the best way to verify that all sorting algorithms are working correctly.

**Setup:**

```
pip install pytest
```

**Run Tests:**
From the `Sorting_Package` root folder, simply run:

```
pytest
```

You should see all 7 tests pass (1 test function that runs 4 algorithms, plus 3 error-case tests).

---

### 2. Running the Demo (`main.py`) 

The `main.py` script is a command-line tool to showcase the sorter. It reads numbers from `input.txt` and prints the sorted list.

**Usage:**

```
python main.py <input_file> -a <algorithm_name> -o <order>
```

* **algorithm_name:** `bubble`, `selection`, `quick`, `merge`
* **order:** `asc` (default) or `desc`

**Examples:**

**Quick Sort (Ascending):**

```
python main.py input.txt -a quick
```

**Merge Sort (Descending):**

```
python main.py input.txt -a merge -o desc
```

**Bubble Sort (Redirecting Output):**
As required by the prompt, the output can be redirected:

```
python main.py input.txt -a bubble > output.txt
```

---

## Assumptions

* **`main.py` Input:**
  The demo script is designed to read a simple, space-separated list of integers from a text file.

---

## Git & Submission (Q3)

This project was developed using Git, as required.
The main branch  contains the complete, working implementation for Q3.

---

