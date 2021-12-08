"""TODO: add docstring"""
import pygame
from button import Button


class Dropdown(Button):
    """Create a dropdown menu that displays items according to given parameters. Inherits from
    button.Button.

    Each dropdown also returns the value which is currently selected.

    Instance Attributes:
      - options: a list of all options in the dropdown
      - mode: whether only 1 box or all boxes are showing
      - is_hovered: represents whether the mouse is on the button

    Representation Invariants:
      - 0 < len(self.options)
      - 0 <= position[0] <= 800
      - 0 <= position[1] <= 800
      - 0 < dimensions[0]
      - 0 < dimensions[1]

    Example Usage:
    >>> dropdown1 = Dropdown(['1', '2', '3'], (0, 0), (50, 50), (0,0,0))

    """

    options: list
    current_value: str
    mode: str

    def __init__(self, options: list, pos: tuple[int, int], dimensions: tuple[int, int],
                 color: tuple[int, int, int]) -> None:
        """Initialize a new instance of the Dropdown class.
        pos represents the top left corner of the initial box.
        dimensions represent the dimension of each individual box"""

        self.options = options
        self.current_value = self.options[0]
        self.mode = "normal"
        super().__init__(pos, dimensions, color)

    def expand(self) -> None:
        """Change the mode of the dropdown to expand"""
        self.mode = "expand"

    def contract(self) -> None:
        """Change the mode of the dropdown to normal"""
        self.mode = "normal"

    def is_clicked_on(self) -> None:
        """Mutate the object based on if/where the player clicks on screen"""
        if self.mode == 'normal':
            if self.is_clicked(pygame.mouse.get_pos()):
                self.expand()
        else:
            # Recreate the same order of buttons as the user sees and then if one of them is clicked
            # on, make it the current value and then contract the dropdown
            order_displayed_now = [self.current_value] + [val for val in self.options
                                                          if val != self.current_value]
            x, y, wid, length = self.position + self.dimensions
            buttons = [Button((x, int(y + length * i)), (wid, length), self.color)
                       for i in range(0, len(order_displayed_now))]
            for but in buttons:
                if but.is_clicked(pygame.mouse.get_pos()):
                    self.current_value = order_displayed_now[buttons.index(but)]
                    self.contract()

    def display(self, screen: pygame.display, font: pygame.font, text: str) -> None:
        """Display method but works with dropdown"""
        super().display(screen, font, text)
        if self.mode == 'expand':  # Creates a lit of buttons and values which appear onscreen as a
            # dropdown menu.
            order_displayed_now = [self.current_value] + [val for val in self.options
                                                          if val != self.current_value]
            x, y, wid, length = self.position + self.dimensions
            buttons = [Button((x, int(y + length * i)), (wid, length), self.color)
                       for i in range(0, len(order_displayed_now))]
            for but in buttons:  # Cycle through the dropdown meny and assign each one dataset name
                index = buttons.index(but)
                but.display(screen, font, text=(order_displayed_now[index]))


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['pygame', 'button'],
        'disable': ['R1705', 'C0200']
    })
