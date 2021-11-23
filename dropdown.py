"""TODO: add docstring"""
import pygame


class Dropdown:
    """Create a dropdown menu that displays items according to given parameters.

    Each dropdown also returns the value which is currently selected.

    Representation Invariants:
      - 0 < len(self.options)
      - 0 <= position[0] <= 800
      - 0 <= position[1] <= 800
      - 0 < dimensions[0]
      - 0 < dimensions[1]
    """

    options: list
    position: tuple[int, int]
    dimensions: tuple[int, int]
    current_value: str
    color: tuple[int, int, int]
    mode: str  # represents whether the dropdown is currently displaying all options.

    def __init__(self, options: list, pos: tuple[int, int], dimensions: tuple[int, int],
                 color: tuple[int, int, int]) -> None:
        """Initialize a new instance of the Dropdown class.
        pos represents the top left corner of the initial box.
        dimensions represent the dimension of each individual box"""

        self.options = options
        self.current_value = self.options[0]
        self.position = pos
        self.dimensions = dimensions
        self.color = color
        self.mode = "normal"

    def expand(self) -> None:
        """Change the mode of the dropdown to expand"""
        self.mode = "expand"

    def contract(self) -> None:
        """Change the mode of the dropdown to normal"""
        self.mode = "normal"

    def is_clicked_on(self) -> None:
        """Mutate the object based on if/where the player clicks on screen"""
        if self.mode == 'normal':
            x, y, wid, length = self.position + self.dimensions
            rect = pygame.rect.Rect(x, y, wid, length)
            if rect.collidepoint(pygame.mouse.get_pos()):
                self.expand()
        else:
            order_displayed_now = [self.current_value] + [val for val in self.options
                                                          if val != self.current_value]
            x, y, wid, length = self.position + self.dimensions
            rects = [pygame.rect.Rect(x, y + i * length, wid, length)
                     for i in range(0, len(order_displayed_now))]
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    self.current_value = order_displayed_now[rects.index(rect)]
                    self.contract()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['pygame'],
        'disable': ['R1705', 'C0200']
    })
