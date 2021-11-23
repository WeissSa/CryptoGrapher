"""TODO: ADD DOCSTRING"""
import pygame
import dropdown


def run_menu(datasets: dict[str, object]) -> None:
    """Open the menu for our software and set up interface"""
    pygame.display.init()
    pygame.font.init()

    screen = pygame.display.set_mode((800, 800))  # create an 800 x 800 pixel screen
    dropdown_1, dropdown_2 = create_dropdowns(datasets)

    dropdowns = [dropdown_1, dropdown_2]  # List of dropdowns to draw on screen
    things_to_draw = [] + dropdowns

    running = True
    while running:
        running = check_events(pygame.event.get(), dropdowns)
        draw_screen(screen, things_to_draw)
        pygame.display.update()
    pygame.display.quit()


def check_events(events: list[pygame.event], dropdowns: list[dropdown.Dropdown]) -> bool:
    """Go through all events and return whether the user wants to quit
    or if they have pressed a button."""
    for event in events:
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONUP:
            check_dropdowns(dropdowns)

    return True


def draw_screen(screen: pygame.display, objects: list) -> None:
    """Draw objects onto the menu screen."""
    font = pygame.font.SysFont("Arial", 20)
    screen.fill((200, 200, 200))

    for obj in objects:
        if isinstance(obj, dropdown.Dropdown):
            x, y = obj.position
            w, length = obj.dimensions
            pygame.draw.rect(screen, obj.color, [x, y, w, length], False)  # draw the box
            pygame.draw.rect(screen, (0, 0, 0), [x, y, w, length], True)  # Draw black outline

            text_display = font.render(obj.current_value, True, (0, 0, 0))
            text_rect = text_display.get_rect(center=(x + w / 2, y + length / 2))
            screen.blit(text_display, text_rect)

            if obj.mode == "expand":
                render_expansions(obj, screen, font)


def render_expansions(dd: dropdown.Dropdown, screen: pygame.display, font: pygame.font) -> None:
    """Draws an expanded dropdown that shows all options."""
    count_so_far = 1  # Initializes to 2 because 1 box has already been created.
    other_values = [val for val in dd.options if val != dd.current_value]
    for box in dd.options:
        if box != dd.current_value:
            x, y = dd.position
            w, length = dd.dimensions
            y += length * count_so_far  # I found dividing by 3 works best for spacing
            pygame.draw.rect(screen, dd.color, [x, y, w, length], False)  # draw the box
            pygame.draw.rect(screen, (0, 0, 0), [x, y, w, length], True)  # Draw black outline

            text_display = font.render(other_values[count_so_far - 1], True, (0, 0, 0))
            text_rect = text_display.get_rect(center=(x + w / 2, y + length / 2))
            screen.blit(text_display, text_rect)
            count_so_far += 1


def create_dropdowns(datasets: dict[str, object]) -> tuple[dropdown.Dropdown, dropdown.Dropdown]:
    """Take a dictionary of datasets and based off the keys return 2 identical dropdowns."""
    options = list(datasets.keys())
    # I am making each box of the dropdown be 80 x 20 pixels and placing them in arbitrary spots
    dropdown_1 = dropdown.Dropdown(options, (20, 20), (80, 30), (100, 100, 200))
    dropdown_2 = dropdown.Dropdown(options, (120, 20), (80, 30), (200, 100, 100))
    return dropdown_1, dropdown_2


def check_dropdowns(dropdowns: list[dropdown.Dropdown]) -> None:
    """Check if dropdowns are being clicked on"""
    for drop in dropdowns:
        drop.is_clicked_on()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['pygame', 'dropdown'],
        'disable': ['R1705', 'C0200']
    })
