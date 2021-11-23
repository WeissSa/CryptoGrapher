"""TODO: ADD DOCSTRING"""
import data_handler
import data_processor
import menu
import grapher

if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['data_handler', 'data_processor', 'menu', 'grapher'],
        'disable': ['R1705', 'C0200']
    })
