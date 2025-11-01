# src/sorters.py
from typing import List
# Import  from the other file in this 'src' package
from .base_sorter import BaseSorter 

# --- 1. Bubble Sort ---

class BubbleSorter(BaseSorter):
    
    def sort(self, data: List[int], ascending: bool = True) -> List[int]:
        # Create a copy to avoid modifying the original list
        new_data = data.copy()
        n = len(new_data)
        
        for i in range(n):
            # Flag to optimize if list is already sorted
            swapped = False
            for j in range(0, n - i - 1):
                # Check if we need to swap
                if (ascending and new_data[j] > new_data[j+1]) or \
                   (not ascending and new_data[j] < new_data[j+1]):
                    
                    new_data[j], new_data[j+1] = new_data[j+1], new_data[j]
                    swapped = True
            
            if not swapped:
                break # List is sorted
                
        return new_data

# --- 2. Selection Sort ---

class SelectionSorter(BaseSorter):
    
    def sort(self, data: List[int], ascending: bool = True) -> List[int]:
        # Create a copy
        new_data = data.copy()
        n = len(new_data)
        
        for i in range(n):
            # Find the index of the min (or max) element
            target_idx = i
            for j in range(i + 1, n):
                if (ascending and new_data[j] < new_data[target_idx]) or \
                   (not ascending and new_data[j] > new_data[target_idx]):
                    target_idx = j
            
            # Swap the found element with the first element
            new_data[i], new_data[target_idx] = new_data[target_idx], new_data[i]
            
        return new_data

# --- 3. Quick Sort ---

class QuickSorter(BaseSorter):
    
    def sort(self, data: List[int], ascending: bool = True) -> List[int]:
        # Create a copy
        new_data = data.copy()
        
        # We sort in-place on the copy
        self._quicksort(new_data, 0, len(new_data) - 1)
        
        # Easiest way to handle order: sort ascending, then reverse if needed.
        if not ascending:
            new_data.reverse()
            
        return new_data

    # Helper method for recursion
    def _quicksort(self, arr: List[int], low: int, high: int):
        if low < high:
            # pi is partitioning index
            pi = self._partition(arr, low, high)
            
            self._quicksort(arr, low, pi - 1)  # Before pi
            self._quicksort(arr, pi + 1, high) # After pi

    # Helper method for partitioning
    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high] # Pivot element
        i = (low - 1)     # Index of smaller element
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

# --- 4. Merge Sort ---

class MergeSorter(BaseSorter):

    def sort(self, data: List[int], ascending: bool = True) -> List[int]:
        # Our helper _mergesort already returns a new list, so no
        # data.copy() is needed here.
        
        sorted_data = self._mergesort(data)
        
        # Easiest way to handle order: sort ascending, then reverse if needed.
        if not ascending:
            sorted_data.reverse()
            
        return sorted_data

    # Helper method for recursion
    def _mergesort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
            
        mid = len(arr) // 2
        left_half = self._mergesort(arr[:mid])
        right_half = self._mergesort(arr[mid:])
        
        return self._merge(left_half, right_half)

    # Helper method to merge two sorted lists
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        # Append remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result