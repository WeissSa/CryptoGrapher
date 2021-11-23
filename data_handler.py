"""TODO: ADD DOCSTRING"""

# import functions
from dataclasses import dataclass
import datetime
import csv
import os
import glob
import pandas


def get_all_csv() -> None:
    """Takes all of the .csv files in the folder and concatenates them into one .csv file.

    """
    path = os.getcwd()
    all_files = glob.glob(os.path.join(path, "*.csv"))  # finds the path of the csv files.

    csv_files = []
    for file in all_files:  # puts all the csv files into one list.
        csv = pd.read_csv(filename, index_col=None)
        csv_files.append(csv)

    merged_csv = pd.concat(csv_files, ignore_index=True)  # concatenates the csv files into one .csv file.
    merged_csv.to_csv("all_coin.csv")  # exports the merged .csv file.


class Point:
    """Class that receives information for all of the cryptocurrencies for each day.

    Representation Invariants:
        -
        -
        -
    """
    name: str
    date: datetime.datetime
    high: float
    low: float
    marketcap: float


# Make sure to do representation invariants for the class


@dataclass
class Dataset:
    """Class that brings together objects from Point that have the same cryptocurrency name.
    """


def dictionary(x: Dataset) -> dict:
    """Returns the dictionary of the dataset, with the name of the crypto as the key and
    the dataset as its key.
    """
    x = {'0': 0}

    return x


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'random', 'tkinter'],
        'disable': ['R1705', 'C0200'],
        'max-args': 7
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
