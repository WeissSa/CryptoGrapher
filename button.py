"""CSC110 Fall 2021: Cryptographer - Grapher

Module Description
==================
This module contains functions that

Copyright and Usage Information
===============================
This file is intended exclusively for academic use for the University of Toronto St. George Campus
in the CSC110 class of Fall 2021. Any distribution of this code, with or without changes,
are expressly prohibited.

This file is Copyright (c) 2021 Madeline Ahn, and Samuel Weiss.
"""
import pygame


class Button:
    """A customizable button object that can be placed on pygame screen.

    Instance Attributes:
      - position: top left corner of the default box of dropdown
      - dimensions: width and length of each box
      - color: colour of each box (rgb)
      - hover_color: a lighter version of the colour for when it is being hovered over
      - is_hovered: represents whether the mouse is on the button


    Representation Invariants:
      - 0 <= position[0] <= 800
      - 0 <= position[1] <= 800
      - 0 < dimensions[0]
      - 0 < dimensions[1]

    Example Usage:
    >>> button1 = Button((0, 0), (50, 50), (0,0,0))
    """
    position: tuple[int, int]
    dimensions: tuple[float, float]
    color: tuple[int, int, int]
    is_hovered: bool
    hover_color: tuple[int, int, int]

    def __init__(self, position: tuple[int, int], dimensions: tuple[float, float],
                 color: tuple[int, int, int]) -> None:
        """Initializes a new instance of a button.
        """
        self.position = position
        self.color = color
        self.dimensions = dimensions
        self.is_hovered = False  # Assume it is not hovered by default
        # The hover color is a lighter version of the original color
        self.hover_color = tuple((min(x + 20, 255) for x in color))

    def display(self, screen: pygame.display, font: pygame.font, text: str) -> None:
        """Draws the button on screen.
        """
        self.check_hovered(pygame.mouse.get_pos())
        x, y = self.position
        w, length = self.dimensions
        if self.is_hovered:  # Make a lighter colour if mouse is hovering over it
            rect = pygame.draw.rect(screen, self.hover_color, [x, y, w, length], False)
        else:
            rect = pygame.draw.rect(screen, self.color, [x, y, w, length], False)
        pygame.draw.rect(screen, (0, 0, 0), [x, y, w, length], True)
        text_display = font.render(text, True, (0, 0, 0))
        text_rect = text_display.get_rect(center=rect.center)
        screen.blit(text_display, text_rect)

    def is_clicked(self, mouse: tuple[float, float]) -> bool:
        """Return if mouse is colliding with self.
        """
        x, y = self.position
        w, length = self.dimensions
        temp_rect = pygame.rect.Rect(x, y, w, length)
        if temp_rect.collidepoint(mouse):
            return True
        return False

    def check_hovered(self, mouse: tuple[float, float]) -> None:
        """Check to see if the button is being hovered over.
        """
        x, y = self.position
        w, length = self.dimensions
        temp_rect = pygame.rect.Rect(x, y, w, length)
        if temp_rect.collidepoint(mouse):
            self.is_hovered = True
        else:
            self.is_hovered = False


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['pygame'],
        'disable': ['R1705', 'C0200']
    })

    # No doctests present
