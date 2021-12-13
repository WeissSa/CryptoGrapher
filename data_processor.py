"""
Module Description
==================
This module contains functions that processes the data and does calculations on the average
increases for the datasets.

Copyright and Usage Information
===============================
Any distribution of this code, with or without changes, are expressly prohibited.

This file is Copyright (c) 2021 Madeline Ahn, and Samuel Weiss.
"""
import datetime
from data_handler import Dataset


def calc_avg_before(dataset: Dataset, attr: str) -> float:
    """
    Returns a list of floats of the average increase of the given attr of a cryptocurrency
    before March 2020.

    If no points exist before March 2020 return 0.

    Preconditions:
      - len(dataset.points) > 0

    >>> from data_handler import Point
    >>> date1 = datetime.date(2020, 3, 1)
    >>> date2 = datetime.date(2020, 3, 2)
    >>> points = [Point('p', date1, 5, 3, 1), Point('p', date2, 6, 3, 1)]
    >>> data = Dataset(points, (0, 0, 0), 'point')
    >>> calc_avg_before(data, 'high')
    1.0
    >>> points[0].high = 1
    >>> calc_avg_before(data, 'high')
    5.0
    """
    attr_list_so_far = []
    points = dataset.points
    for i in range(0, len(points) - 1):
        if points[i + 1].date < datetime.date(2020, 4, 1):
            increase = points[i + 1].__getattribute__(attr) - points[i].__getattribute__(attr)
            attr_list_so_far.append(increase)

    if len(attr_list_so_far) == 0:
        return 0

    return round(sum(attr_list_so_far) / (len(attr_list_so_far)), 3)


def calc_avg_after(dataset: Dataset, attr: str) -> float:
    """
    Returns a list of floats of the average increase of the given attr of a cryptocurrency
    from March 2020 to the most recent data entry.

    If no points exist after March 2020 return 0.

    Preconditions:
      - len(dataset.points) > 0

    >>> from data_handler import Point
    >>> date1 = datetime.date(2020, 4, 1)
    >>> date2 = datetime.date(2020, 4, 2)
    >>> points = [Point('p', date1, 5, 3, 1), Point('p', date2, 6, 3, 1)]
    >>> data = Dataset(points, (0, 0, 0), 'point')
    >>> calc_avg_after(data, 'high')
    1.0
    >>> points[0].high = 1
    >>> calc_avg_after(data, 'high')
    5.0
    """
    attr_list_so_far = []
    points = dataset.points
    for i in range(0, len(points) - 1):
        if points[i + 1].date >= datetime.date(2020, 4, 1):
            increase = points[i + 1].__getattribute__(attr) - points[i].__getattribute__(attr)
            attr_list_so_far.append(increase)

    if len(attr_list_so_far) == 0:
        return 0

    return round(sum(attr_list_so_far) / len(attr_list_so_far), 3)


def calc_per_before(dataset: Dataset, attr: str) -> str:
    """
    Returns a list of floats of the percent increase of the given attr of a cryptocurrency
    before March 2020.

    If no points exist before March 2020 return 0%.

    Preconditions:
      - len(dataset.points) > 0

    >>> from data_handler import Point
    >>> date1 = datetime.date(2020, 3, 1)
    >>> date2 = datetime.date(2020, 3, 2)
    >>> points = [Point('p', date1, 5, 3, 1), Point('p', date2, 6, 3, 1)]
    >>> data = Dataset(points, (0, 0, 0), 'point')
    >>> calc_per_before(data, 'high')
    '20.0%'
    >>> points[0].high = 1
    >>> calc_per_before(data, 'high')
    '500.0%'
    """
    attr_list_so_far = []
    points = dataset.points
    for i in range(0, len(points) - 1):
        if points[i + 1].date < datetime.date(2020, 4, 1) and points[i].__getattribute__(attr) != 0:
            increase = points[i + 1].__getattribute__(attr) / points[i].__getattribute__(attr)
            attr_list_so_far.append(increase)

    if len(attr_list_so_far) == 0:
        return '0%'

    string = round((sum(attr_list_so_far) / len(attr_list_so_far) - 1) * 100, 3)
    return str(string) + '%'


def calc_per_after(dataset: Dataset, attr: str) -> str:
    """
    Returns a list of floats of the percent increase of the attr of a cryptocurrency
    after March 2020 to the most recent data entry.

    If no points exist after March 2020 return 0%.

    Preconditions:
      - len(dataset.points) > 0

    >>> from data_handler import Point
    >>> date1 = datetime.date(2020, 4, 1)
    >>> date2 = datetime.date(2020, 4, 2)
    >>> points = [Point('p', date1, 6, 3, 1), Point('p', date2, 5, 3, 1)]
    >>> data = Dataset(points, (0, 0, 0), 'point')
    >>> calc_per_after(data, 'high')
    '-16.667%'
    >>> points[0].high = 1
    >>> calc_per_after(data, 'high')
    '400.0%'
    >>> points[0].high = 0
    >>> calc_per_after(data, 'high')
    '0%'
    """
    attr_list_so_far = []
    points = dataset.points
    for i in range(0, len(points) - 1):
        if points[i + 1].date >= datetime.date(2020, 4, 1) \
                and points[i].__getattribute__(attr) != 0:
            increase = points[i + 1].__getattribute__(attr) / points[i].__getattribute__(attr)
            attr_list_so_far.append(increase)

    if len(attr_list_so_far) == 0:
        return '0%'

    string = round((sum(attr_list_so_far) / len(attr_list_so_far) - 1) * 100, 3)
    return str(string) + '%'


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['pygame', 'datetime', 'data_handler'],
        'disable': ['R1705', 'C0200'],
        'generated-members': ['pygame.*']
    })
    import doctest
    doctest.testmod()
