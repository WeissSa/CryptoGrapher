"""TODO: ADD DOCSTRING"""
import pygame
from dropdown import Dropdown
from button import Button
from grapher import Grapher
import data_handler


def run_menu(datasets: dict[str, data_handler.Dataset]) -> None:
    """Open the menu for our software and set up interface"""
    pygame.display.init()
    pygame.font.init()

    screen = pygame.display.set_mode((800, 800))  # create an 800 x 800 pixel screen
    dropdown_1, dropdown_2 = create_dropdowns(datasets)
    dependent_variable_dropdown = Dropdown(['High', 'Low', 'Marketcap'],
                                           (400, 100),
                                           (80, 30),
                                           (150, 100, 200))

    continue_button = Button(position=(300, 700), dimensions=(200, 70),
                             color=(100, 200, 100))
    dropdowns = [dropdown_1, dropdown_2, dependent_variable_dropdown]
    # List of dropdowns to draw on screen
    things_to_draw = set(dropdowns)
    things_to_draw.add(continue_button)

    running = 'continue'
    while running == 'continue':
        # This loop handles displaying/updating the menu. Everyting above is setup for this.
        draw_screen(screen, things_to_draw)
        pygame.display.update()
        running = check_events(pygame.event.get(), dropdowns, continue_button)
    if running == 'graph':
        graph = Grapher(datasets[dropdown_1.current_value],
                        datasets[dropdown_2.current_value], screen,
                        str.lower(dependent_variable_dropdown.current_value))
        running = graph.make_graph()
        # if make_graph returns that the user wants to continue the function will call itself
        # and loop recursively

    if running == 'continue':
        run_menu(datasets)

    elif running == 'quit':
        pygame.display.quit()


def check_events(events: list[pygame.event], dropdowns: list[Dropdown], button: Button) -> str:
    """Go through all events and return whether the user wants to quit
    or if they have pressed a button."""
    for event in events:
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONUP:
            check_dropdowns(dropdowns)
            if button.is_clicked(pygame.mouse.get_pos()):
                return 'graph'

    return 'continue'


def draw_screen(screen: pygame.display, objects: set) -> None:
    """Draw objects onto the menu screen."""
    font = pygame.font.SysFont("Arial", 20)
    screen.fill((200, 200, 200))

    # Label the dependent variable dropdown
    text = font.render('Compare: ', True, (0, 0, 0))
    text_rect = text.get_rect(topleft=(320, 105))
    screen.blit(text, text_rect)

    # draw all the buttons
    for obj in objects:
        if isinstance(obj, Dropdown):
            obj.display(screen, font, text=obj.current_value)
        elif isinstance(obj, Button):
            obj.display(screen, font, text='Continue')


def create_dropdowns(datasets: dict[str, object]) -> tuple[Dropdown, Dropdown]:
    """Take a dictionary of datasets and based off the keys return 2 identical dropdowns."""
    options = list(datasets.keys())
    length = 200
    width = 30
    # I am making each box of the dropdown be length x width pixels
    # placing them in arbitrary spots
    dropdown_1 = Dropdown(options, (100, 20), (length, width), (100, 100, 200))
    dropdown_2 = Dropdown(options, (500, 20), (length, width), (200, 100, 100))
    return dropdown_1, dropdown_2


def check_dropdowns(dropdowns: list[Dropdown]) -> None:
    """Check if dropdowns are being clicked on"""
    for drop in dropdowns:
        drop.is_clicked_on()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['pygame', 'dropdown', 'button', 'grapher', 'data_handler'],
        'disable': ['R1705', 'C0200'],
        'generated-members': ['pygame.*']
    })

    run_menu(data_handler.create_datasets('data'))  # runs the code in intended way
