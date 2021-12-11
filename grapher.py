"""TODO: ADD DOCSTRING"""
import pygame
from datetime import datetime
from button import Button
from data_handler import Dataset, Point


class Grapher:
    """Handles the drawing and graphing of 2 Datasets.

    Instance Attributes:
      - dataset1: the first dataset to graph
      - dataset2: the second dataset to graph
      - screen: screen object which other surface objects are drawn onto
      - line_color: color of axis and other neutral lines
      - bg_color: background color
      - normal_font: font of average text
      - title_font: font of titles
      - comparison: the attribute the user chose to compare (i.e. market high)

    Representation Invariants:
      - all(0 <= x <= 255 for x in line_color)
      - all(0 <= x <= 255 for x in bg_color)
      - dataset1 and dataset2 are properly formatted Dataset objects

    Example Usage:
    >>> d1 = Dataset([], (0, 0, 0), 'Bitcoin')
    >>> d2 = Dataset([], (0, 0, 0), 'Dogecoin')
    >>> screen = pygame.display.set_mode((800, 800))
    >>> graph = Grapher(d1, d2, screen)
    """

    dataset1: Dataset
    dataset2: Dataset
    screen: pygame.display
    line_color: tuple[int, int, int]
    bg_color: tuple[int, int, int]
    comparison: str
    normal_font: pygame.font.SysFont

    def __init__(self, dataset1: Dataset, dataset2: Dataset, screen: pygame.display,
                 comparison: str) -> None:
        """Initialize a new Grapher object"""
        self.dataset1 = dataset1
        self.dataset2 = dataset2
        self.comparison = comparison
        self.normal_font = pygame.font.SysFont("Arial", 20)
        self.bg_color = (230, 230, 230)
        self.line_color = (20, 20, 20)
        self.screen = screen

    def make_graph(self) -> str:
        """Handles the making of the final graph"""
        running = 'graph'
        while running == 'graph':
            self.screen.fill(self.bg_color)
            self.create_axis()
            self.create_legend()
            self.graph_points()

            # Create and display new_graph button
            continue_button = Button((10, 10), (100, 40),
                                     (150, 50, 150))
            continue_button.display(self.screen, self.normal_font, 'New Graph')

            pygame.display.update()

            # exit condition:
            running = check_events(pygame.event.get(), continue_button)

        return running

    def create_axis(self) -> None:
        """Creates the axis of the graph"""
        line_width = 3
        y_axis = pygame.draw.line(self.screen, self.line_color, (30, 100), (30, 750), line_width)
        x_axis = pygame.draw.line(self.screen, self.line_color, (30, 750), (750, 750), line_width)
        self.label_axis(x_axis, y_axis)

    def label_axis(self, x: pygame.rect.Rect, y: pygame.rect.Rect) -> None:
        """Label the axis"""

        x_label = self.normal_font.render('DAYS', True, self.line_color)
        x_rect = x_label.get_rect(midtop=x.midbottom)

        y_label = self.normal_font.render(str.upper(self.comparison), True, self.line_color)
        y_label = pygame.transform.rotozoom(y_label, 90, 1)
        y_rect = y_label.get_rect(midright=y.midleft)

        title_string = f'Price vs Time of {self.dataset1.name} and {self.dataset2.name}'
        if self.dataset1 == self.dataset2:
            title_string = f'Price vs Time of {self.dataset1.name}'
        title = self.normal_font.render(title_string, True, self.line_color)
        title_rect = title.get_rect(center=(400, 25))

        self.screen.blit(x_label, x_rect)
        self.screen.blit(y_label, y_rect)
        self.screen.blit(title, title_rect)

    def create_legend(self) -> None:
        """Create a legend which labels the two datasets"""
        # Decide the dimensions/create empty box
        dimensions = 140
        legend = pygame.draw.rect(self.screen, self.line_color,
                                  [650, 10, dimensions, dimensions / 1.5], True)
        radius = dimensions / 6

        # create circles
        circle1 = pygame.draw.circle(self.screen, self.dataset1.color,
                                     [legend.left + radius, legend.top + radius], radius)
        circle2 = pygame.draw.circle(self.screen, self.dataset2.color,
                                     [legend.left + radius, legend.bottom - radius], radius)

        # draw/scale text
        text1 = self.normal_font.render(self.dataset1.name, True, self.line_color)
        if text1.get_rect(midleft=circle1.midright).right > 800:
            text1 = pygame.transform.scale(text1, (int(dimensions - radius * 2), 20))
        text1_rect = text1.get_rect(midleft=circle1.midright)
        # ---------------------------------------------------------------------------
        text2 = self.normal_font.render(self.dataset2.name, True, self.line_color)
        if text2.get_rect(midleft=circle2.midright).right > 800:
            text2 = pygame.transform.scale(text2, (int(dimensions - radius * 2), 20))
        text2_rect = text2.get_rect(midleft=circle2.midright)

        self.screen.blit(text1, text1_rect)
        self.screen.blit(text2, text2_rect)

    def graph_points(self) -> None:
        """Graph all the points in dataset1, dataset2

        Note that the area we can draw on is 720 x 650 pixels
        """
        # Make sure we are working with the larger dataset first
        if self.dataset1 != self.dataset2:
            datasets = [self.dataset1, self.dataset2]
            if len(self.dataset2.points) > len(self.dataset1.points):
                datasets.reverse()

            datasets = even_out_datasets(datasets)

            max_value = max([x.__getattribute__(self.comparison)
                             for x in datasets[0].points] + [x.__getattribute__(self.comparison)
                                                             for x in datasets[1].points])
        else:
            datasets = [self.dataset1]
            max_value = max([x.__getattribute__(self.comparison) for x in datasets[0].points])

        for dataset in datasets:
            points = dataset.points
            color = dataset.color

            # Set up a measurement so that each point has at least a 10 pixel gap between the center
            num_points = len(points)
            days_per_10_pixels = max(int(num_points / 72 + 0.5), 1)
            # the graph has 720 pixels on the x axis and the + 0.5 rounds it up
            for i in range(0, len(points), days_per_10_pixels):
                # Set Y and radius relative to the maximum value on the graph
                centery = 750 - points[i].__getattribute__(self.comparison) / max_value * 650

                # 1 minimum radius so you can hover over any point (it can get a bit precise still)
                radius = max(points[i].__getattribute__(self.comparison) / max_value * 10, 3)

                point_rect = pygame.draw.circle(self.screen, color,
                                                (30 + (i // days_per_10_pixels) * 10, centery),
                                                radius)

                # Draw a line to the next point
                if i < len(points) - days_per_10_pixels:
                    center_y2 = points[i + days_per_10_pixels].__getattribute__(self.comparison)
                    center_y2 = 750 - center_y2 / max_value * 650
                    x_1 = 30 + i // days_per_10_pixels * 10
                    x_2 = 30 + (i // days_per_10_pixels + 1) * 10
                    self.draw_line(dataset, (x_1, centery), (x_2, center_y2), points[i].date)

                # Label point if mouse nearby
                if point_rect.collidepoint(pygame.mouse.get_pos()):
                    self.label_point(point_rect, points[i])

    def label_point(self, point_location: pygame.rect, point: Point) -> None:
        """Helper function for graph_points to help label point."""
        value = str(point.__getattribute__(self.comparison))
        date = str(point.date)

        text_1 = self.normal_font.render(str(date), True, self.line_color)
        text_rect_1 = text_1.get_rect(midbottom=point_location.midtop)
        self.screen.blit(text_1, text_rect_1)

        text_2 = self.normal_font.render('$' + str(value), True, self.line_color)
        text_rect_2 = text_2.get_rect(midbottom=text_rect_1.midtop)
        self.screen.blit(text_2, text_rect_2)

    def draw_line(self, dataset: Dataset, point1: tuple[int, int], point2: tuple[int, int],
                  date: datetime.date) -> None:
        """Draw a line between 2 points. Line is red if date is during March 2020"""
        color = dataset.color
        # just in case a point in March is not caught, we measure the first half of april
        if datetime(2020, 2, 28).date() < date < datetime(2020, 4, 15).date():
            color = (255, 0, 0)
        pygame.draw.line(self.screen, color, point1, point2, 3)
        if color == (255, 0, 0):
            self.draw_covid_rect(point1, point2)

    def draw_covid_rect(self, point1: tuple[int, int], point2: tuple[int, int]) -> None:
        """Draw a semi-transparent red rectangle on the covid parts of the graph.

        Preconditions:
          - 30 < point1[0] < 750
          - 30 < point2[0] < 750
        """
        length = point2[0] - point1[0]
        height = 675
        rect = pygame.Surface((length, height))
        rect.set_alpha(50)  # Make it transparent
        rect.fill((255, 0, 0))
        self.screen.blit(rect, (point1[0], 75))


def check_events(events: list[pygame.event.Event], continue_button: Button) -> str:
    """Return whether the user wants to quit or other events have been activated"""
    for event in events:
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONUP:
            if continue_button.is_clicked(pygame.mouse.get_pos()):
                return 'continue'
    return 'graph'


def even_out_datasets(datasets: list[Dataset]) -> list[Dataset, Dataset]:
    """return the shorter dataset with the same number of points as the larger one.

    All points added will have value of 0 and a location such that the datetime matches the larger
    dataset.
    """
    temp_dataset_1 = Dataset(datasets[0].points, datasets[0].color, datasets[0].name)
    temp_dataset_2 = Dataset(datasets[1].points, datasets[1].color, datasets[1].name)
    i = 0
    while len(temp_dataset_1.points) > len(temp_dataset_2.points):
        equivalent_point = temp_dataset_1.points[i]
        temp_dataset_2.points.insert(i, Point(temp_dataset_2.name, equivalent_point.date, 0, 0, 0))
        i += 1
    return [temp_dataset_1, temp_dataset_2]


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['pygame', 'datetime', 'button', 'data_handler'],
        'disable': ['R1705', 'C0200'],
        'generated-members': ['pygame.*']
    })
