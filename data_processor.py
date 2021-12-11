"""TODO: ADD DOCSTRING

"""
import datetime
from data_handler import create_datasets  # Imported just for testing, can delete later
from data_handler import Dataset
from statistics import mean


def calc_avg_before(data: dict[str, Dataset], crypto: str) -> float:
    """
    Returns a list of floats of the average increase of the highs of a cryptocurrency
    before March 2020.

    Preconditions:
        - crypto == data[crypto].name
        - data[crypto].points[0].date <= datetime.date(2020, 3, 1)

    Sample Usage:
    >>> data = create_datasets('data')
    >>> calc_avg_before(data, 'XRP')
    0.199
    """
    num_days = abs(datetime.date(2020, 3, 1) - data[crypto].points[0].date).days
    return round(sum([data[crypto].points[day].High for day in range(num_days)]) / num_days, 3)


def calc_avg_after(data: dict[str, Dataset], crypto: str) -> float:
    """
    Returns a list of floats of the average increase of the high of a cryptocurrency
    from March 2020 to the most recent data entry.

    Preconditions:
        - crypto == data[crypto].name
        - data[crypto].points[-1].date >= datetime.date(2020, 3, 1)

    Sample Usage:
    >>> data = create_datasets('data')
    >>> calc_avg_after(data, 'XRP')
    0.477
    """
    num_days = abs(data[crypto].points[-1].date - datetime.date(2020, 3, 1)).days
    return round(sum([data[crypto].points[-day].High for day in range(1, num_days + 1)]) / num_days, 3)


def calc_per_before(data: dict[str, Dataset], crypto: str) -> float:
    """
    Returns a list of floats of the percent increase of the low and high of a cryptocurrency
    before March 2020.

    Preconditions:
        - crypto != ''
        - data[crypto].points[0].date <= datetime.date(2020, 3, 1)

    Sample Usage:
    >>> data = create_datasets('data')
    >>> calc_per_before(data, 'XRP')
    0.49
    """
    index = 0

    while data[crypto].points[index].date <= datetime.date(2020, 3, 1):
        index += 1

    return round(mean([(data[crypto].points[i + 1].High - data[crypto].points[i].High)
                       / data[crypto].points[i].High * 100 for i in range(index)]), 2)


def calc_per_after(data: dict[str, Dataset], crypto: str) -> float:
    """
    Returns a list of floats of the percent increase of the high of a cryptocurrency
    after March 2020 to the most recent data entry.

    Preconditions:
        - crypto != ''
        - data[crypto].points[-1].date >= datetime.date(2020, 3, 1)

    Sample Usage:
    >>> data = create_datasets('data')
    >>> calc_per_before(data, 'XRP')
    0.48
    """
    index = -1

    while data[crypto].points[index].date >= datetime.date(2020, 3, 1):
        index -= 1

    return round(mean([(data[crypto].points[i].High - data[crypto].points[i - 1].High)
                       / data[crypto].points[i - 1].High * 100 for i in range(index, 0)]), 2)


# if __name__ == '__main__':
#     import python_ta
#
#     python_ta.check_all(config={
#         'max-line-length': 100,
#         'extra-imports': ['pygame', 'datetime', 'button', 'data_handler'],
#         'disable': ['R1705', 'C0200'],
#         'generated-members': ['pygame.*']
#     })
