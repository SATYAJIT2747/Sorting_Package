# src/base_sorter.py
"""Defines the Abstract Base Class for all sorters."""
from abc import ABC, abstractmethod
from typing import List
# pylint: disable=too-few-public-methods
class BaseSorter(ABC):
    """
    Abstract Base Class for all sorting algorithms.

    This class defines the 'contract' that every sorting algorithm
    must follow.
    """

    @abstractmethod
    def sort(self, data: List[int], ascending: bool = True) -> List[int]:
        """
        Sorts a list of integers.

        Args:
            data (List[int]): The list of integers to be sorted.
            ascending (bool): True for ascending order, False for descending.

        Returns:
            List[int]: The sorted list.
        """
        ...
        ...
        # An abstract method has no code in its body
