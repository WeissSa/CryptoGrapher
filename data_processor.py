"""TODO: ADD DOCSTRING

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

    Sample Usage:
    >>> from data_handler import create_datasets
    >>> data = create_datasets('data')
    >>> calc_avg_before(data['Bitcoin'], 'high')
    2.515
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

    Sample Usage:
    >>> from data_handler import create_datasets
    >>> data = create_datasets('data')
    >>> calc_avg_after(data['Bitcoin'], 'high')
    61.762
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

    Sample Usage:
    >>> from data_handler import create_datasets
    >>> data = create_datasets('data')
    >>> calc_per_before(data['Bitcoin'], 'high')
    '0.223%'
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

    Sample Usage:
    >>> from data_handler import create_datasets
    >>> data = create_datasets('data')
    >>> calc_per_after(data['Bitcoin'], 'high')
    '0.419%'
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
