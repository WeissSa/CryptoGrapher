"""TODO: ADD DOCSTRING

"""
import datetime
from data_handler import create_datasets  # Imported just for testing, can delete later
from data_handler import Dataset


def low_avg(data: dict[str, Dataset], crypto: str, start_date: datetime.date, end_date: datetime.date) -> float:
    """
    Takes the average change of the low of a cryptocurrency from the inputted starting date
    to end date and returns it as a float.

    Note that end_date of all csv files is July 6, 2021 (2021, 7, 6).

    Preconditions:
        - crypto == data[crypto].name
        - # end_date and start_date in the dataset
        - end_date.days > start_date.days

    Sample Usage:
    >>> data = create_datasets('data')
    >>> low_avg(data, 'XRP', datetime.date(2020, 3, 1), datetime.date(2021, 7, 6)
    0.000  # Fix this value
    """
    list_values = []
    num_days = abs(end_date - start_date).days

    for day in range(num_days - 1):
        temp_diff = round(data[crypto].points[day + 1].Low - data[crypto].points[day].Low, 3)
        list_values.append(temp_diff)

    total_avg = round(sum(list_values) / num_days, 3)
    return list_values  # Change this back to total average later


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['pygame', 'datetime', 'button', 'data_handler'],
        'disable': ['R1705', 'C0200'],
        'generated-members': ['pygame.*']
    })
