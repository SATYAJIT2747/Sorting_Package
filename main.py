import argparse
import sys
from src.controller import Sorter, AlgorithmName
from typing import List

def read_input_file(file_path: str) -> List[int]:
    """Reads a file and returns a list of integers."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            # Split by any whitespace, filter empty strings, and convert to int
            numbers = [int(num) for num in content.split() if num.strip()]
            return numbers
    except FileNotFoundError:
        print(f"Error: Input file '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print(f"Error: Input file '{file_path}' contains non-integer values.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main function to run the sorter from the command line."""

    parser = argparse.ArgumentParser(description="Sort a list of integers using various algorithms.")

    # Add arguments
    parser.add_argument(
        'input_file',
        type=str,
        help="Path to the input file containing space-separated integers."
    )
    parser.add_argument(
        '-a', '--algorithm',
        type=str,
        required=True,
        choices=['bubble', 'selection', 'quick', 'merge'],
        help="The sorting algorithm to use."
    )
    parser.add_argument(
        '-o', '--order',
        type=str,
        default='asc',
        choices=['asc', 'desc'],
        help="Sort order: 'asc' for ascending (default), 'desc' for descending."
    )

    args = parser.parse_args()

    # --- 1. Read Data ---
    input_data = read_input_file(args.input_file)

    # --- 2. Setup Sorter ---
    controller = Sorter()
    is_ascending = (args.order == 'asc')
    algorithm_name = args.algorithm


    print(f"--- Sorter ---")
    print(f"Algorithm:   {algorithm_name}")
    print(f"Order:       {'Ascending' if is_ascending else 'Descending'}")
    print(f"Input List:  {input_data}")

    # --- 3. Run and Print ---
    try:
        sorted_data = controller.sort_list(
            algorithm_name=algorithm_name,
            data=input_data,
            ascending=is_ascending
        )

        # The prompt requires output to be redirected.
        print("\n--- Output ---")
        print(f"Sorted List: {sorted_data}")

    except (ValueError, TypeError) as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)

# Standard Python entry point
if __name__ == "__main__":
    main()
