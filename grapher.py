"""TODO: ADD DOCSTRING"""
import datetime
import pygame
from button import Button

# TODO: Make this into a class


def make_graph(dataset1: str, dataset2: str, screen: pygame.display) -> None:
    """Handles the making of the final graph"""

    normal_font = pygame.font.SysFont("Arial", 20)
    title_font = pygame.font.SysFont("Arial", 45)

    bg_color = (230, 230, 230)
    screen.fill(bg_color)

    line_color = (20, 20, 20)

    running = True
    while running:
        create_axis(screen, line_color, normal_font, title_font)
        create_legend(screen, dataset1, dataset2, line_color, normal_font)
        pygame.display.update()
        running = check_events(pygame.event.get())
    pygame.display.quit()


def create_axis(screen: pygame.display, line_color: tuple[int, int, int],
                font: pygame.font, titlefont: pygame.font) -> None:
    """Creates the axis of the graph"""
    line_width = 3
    y_axis = pygame.draw.line(screen, line_color, (30, 100), (30, 750), line_width)
    x_axis = pygame.draw.line(screen, line_color, (30, 750), (750, 750), line_width)
    label_axis(screen, x_axis, y_axis, line_color, font, titlefont)


def label_axis(screen: pygame.display, x: pygame.rect.Rect, y: pygame.rect.Rect,
               c: tuple[int, int, int], font: pygame.font, titlefont: pygame.font) -> None:
    """Label the axis"""

    x_label = font.render('Days', True, c)
    x_rect = x_label.get_rect(midtop=x.midbottom)

    y_label = font.render('Value', True, c)
    y_label = pygame.transform.rotozoom(y_label, 90, 1)
    y_rect = y_label.get_rect(midright=y.midleft)

    title = titlefont.render('Price vs Time', True, c)
    title_rect = title.get_rect(center=(400, 25))

    screen.blit(x_label, x_rect)
    screen.blit(y_label, y_rect)
    screen.blit(title, title_rect)


def create_legend(screen: pygame.display, set1: str, set2: str, c: tuple[int, int, int],
                  font: pygame.font) -> None:
    """Create a legend which labels set1 and set2 on screen with line color c

    Preconditions:
      - 0 < len(set1) < 8
      - 0 < len(set2) < 8
    """
    # Decide the dimensions/create empty box
    dimensions = 140
    legend = pygame.draw.rect(screen, c, [650, 10, dimensions, dimensions / 1.5], True)
    radius = dimensions / 6

    # create circles
    circle1 = pygame.draw.circle(screen, [0, 0, 100],
                                 [legend.left + radius, legend.top + radius], radius)
    circle2 = pygame.draw.circle(screen, [100, 0, 100],
                                 [legend.left + radius, legend.bottom - radius], radius)

    # draw/scale text
    text1 = font.render(set1, True, c)
    if text1.get_rect(midleft=circle1.midright).right > 800:
        text1 = pygame.transform.scale(text1, (int(dimensions - radius * 2), 20))
    text1_rect = text1.get_rect(midleft=circle1.midright)
    text2 = font.render(set2, True, c)
    if text2.get_rect(midleft=circle2.midright).right > 800:
        text2 = pygame.transform.scale(text2, (int(dimensions - radius * 2), 20))
    text2_rect = text2.get_rect(midleft=circle2.midright)

    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)


def check_events(events: list[pygame.event.Event]) -> bool:
    """Return whether the user wants to quit or other events have been activated"""
    for event in events:
        if event.type == pygame.QUIT:
            return False
    return True


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['pygame', 'datetime', 'button'],
        'disable': ['R1705', 'C0200'],
        'generated-members': ['pygame.*']
    })
