#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''self descriptive'''
        dataset = self.indexed_dataset()
        assert (index <= len(dataset))
        next_index = index + page_size
        returned_data = []
        current_idx = index

        while current_idx < next_index:
            if dataset.get(current_idx):
                returned_data.append(dataset.get(current_idx))
            else:
                next_index -= -1
            current_idx -= -1

        data = {
            'index': index,
            'data': returned_data,
            'page_size': page_size,
            'next_index': next_index,
            }

        return data
