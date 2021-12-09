"""CSC110: Cryptographer

TODO: DOCSTRING, Copyright things
"""

# Import functions
from dataclasses import dataclass
import datetime
import csv
import os
import glob


class Point:
    """A class containing information about one day of a cryptocurrency.

    Instance Attributes:
        - name: Name of the cryptocurrency.
        - date: Date for that day's high/low/marketcap for the cryptocurrency.
        - high: Highest value of the cryptocurrency that day.
        - low: Lowest value of the cryptocurrency that day.
        - marketcap: Total value of all the shares of the cryptocurrency that day.

    Representation Invariants:
        - self.name != ''
    """
    name: str
    date: datetime.date
    high: float
    low: float
    marketcap: float

    def __init__(self, name, date, high, low, marketcap) -> None:
        self.name = name
        self.date = date
        self.high = high
        self.low = low
        self.marketcap = marketcap

    def add_points(self) -> list[Point]:
        """Opens all of the csv files and creates a list of lists for each point.

        Preconditions:
            -

        Sample Usage:
        >>>
        """
        path = os.getcwd()/"path"
        all_files = glob.glob(os.path.join(path, "*.csv"))
        points_so_far = []

        for file in all_files:
            with open(os.path.join(path, file)) as f:
                data = csv.reader(f)
                next(data)

                for row in data:
                    points_so_far.append(Point(row[1], row[3], row[4], row[5], row[9]))
        return points_so_far


@dataclass
class Dataset:
    """Class that brings together objects from Point that have the same cryptocurrency name.

    Instance Attributes:
        - dataset: A dictionary containing the name of the cryptocurrency as the key,
            and a list of the points of that cryptocurrency as the value.

    Representation Invariants:
        - dataset != {}
    """
    dataset: dict[str, list[Point]]

    def make_dicts(self, points_so_far: list[Point]) -> dict[str, list[Point]]:
        """Turns the list of all the points from Point into an organized dictionary.

        Preconditions:
            - points_so_far != []

        Sample Usage:
        >>> TODO

        """
        dict_so_far = dict()
        for point in points_so_far:
            temp_list = [point]
            if point.name in dict_so_far.keys():
                dict_so_far[point.name] += temp_list
            else:
                dict_so_far[point.name] = temp_list
        dict = Dataset(dict_so_far)  # need to fix this function and make it proper
        # (unless you think this is fine, i think there's just better ways of doing this)
        return dict

# if __name__ == '__main__':
#     import python_ta
#
#     python_ta.check_all(config={
#         'max-line-length': 100,
#         'extra-imports': ['python_ta.contracts', 'random', 'tkinter'],
#         'disable': ['R1705', 'C0200'],
#         'max-args': 7
#     })
#
#     import python_ta.contracts
#
#     python_ta.contracts.DEBUG_CONTRACTS = False
#     python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
