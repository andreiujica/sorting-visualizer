import pygame
import sys
import random
import time
import argparse


def get_input_parameters():
    """Use argparse library to restrict input data, display information about
    input fields and altogether make script more command-line friendly"""

    parser = argparse.ArgumentParser(
        description="This Python script uses pygame to visualise different sorting algos"
    )

    parser.add_argument(
        "-a",
        "--algorithm",
        choices=["bubble_sort", "selection_sort", "insertion_sort", "oracle", "mssql"],
        required=True,
        help="Sorting algo to be used in the visualisation",
    )
    parser.add_argument("-c", "--color", required=True, help="Main color theme to be used in the visualisation")

    args = parser.parse_args()
    return args


class Visualiser:
    """The main class for this program. Contains all methods and sorting algos to be called"""

    def __init__(self, algo, color) -> None:
        """__init__ constructor, usually used to initialise parameters"""
        self.screen = None
        self.width = 800
        self.height = 600
        self.num_bars = 50
        self.bar_width = 10
        self.space = 2
        self.bars = []
        self.text = None
        self.text_rect = None
        self.algo = algo
        self.color = color
        pygame.init()

    def set_initial_font(self):
        """Setting a font family, font size and rendering it with a black font
        on a red background. We fit it in a rectangle to make it easier to center"""

        font = pygame.font.Font("./assets/Product Sans Regular.ttf", 32)
        self.text = font.render(self.algo, True, "black", self.color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.width / 2, 50)

    def set_initial_screen(self):
        """Self explanatory, set display dimensions"""
        pygame.display.set_caption("Sorting Algo Visualiser")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill("white")

    def draw_bar(self, x, height, color) -> None:
        """Helper method to draw a single bar of chosen color, parameters center the bar
        in the window"""
        pygame.draw.rect(
            self.screen, color, (x, (600 - height) / 2, self.bar_width, height), 0
        )
        self.bars.append(height)

    def draw_initial_bars_array(self) -> None:
        """Get values array and draw all the bars of [height] heights"""
        for i in range(self.num_bars):
            height = random.randint(10, 300)
            x = (
                (i * self.bar_width)
                + (i * self.space)
                + (
                    self.width
                    - (self.num_bars * self.bar_width + self.num_bars * self.space)
                )
                / 2
            )
            self.draw_bar(x, height, "black")

    def draw_bar_swaps(self, j):
        """Helper method to declutter sorting functions. Makes the two bars that are being compared
        red when accessed. Also prints the name of the sort on screen"""
        for k in range(self.num_bars):
            x = (
                (k * self.bar_width)
                + (k * self.space)
                + (
                    self.width
                    - (self.num_bars * self.bar_width + self.num_bars * self.space)
                )
                / 2
            )
            height = self.bars[k]

            if self.bars[k] is self.bars[j] or self.bars[k] is self.bars[j + 1]:
                color = self.color
            else:
                color = "black"

            self.screen.blit(self.text, self.text_rect)
            self.draw_bar(x, height, color)

        pygame.display.update()
        time.sleep(0.001)

    def check_open(self):
        """Checks for window close"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def bubble_sort(self):
        """Bubble sorting algorithm"""
        n = len(self.bars)
        for i in range(n):
            for j in range(0, n - i - 1):

                self.draw_bar_swaps(j)

                if self.bars[j] > self.bars[j + 1]:
                    self.bars[j], self.bars[j + 1] = self.bars[j + 1], self.bars[j]
                self.screen.fill("white")

        self.check_open()

    def selection_sort(self):
        """Selection sorting algorithm"""
        n = len(self.bars)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):

                self.draw_bar_swaps(j)

                if self.bars[min_idx] > self.bars[j]:
                    min_idx = j

            self.bars[i], self.bars[min_idx] = self.bars[min_idx], self.bars[i]
            self.screen.fill("white")

        self.check_open()

    def insertion_sort(self):
        """Insertion sorting algorithm"""
        n = len(self.bars)
        for i in range(1, n):
            key = self.bars[i]
            j = i - 1

            while j >= 0 and key < self.bars[j]:
                self.draw_bar_swaps(j)
                self.bars[j + 1] = self.bars[j]
                j -= 1
                self.screen.fill("white")

            self.bars[j + 1] = key

        self.check_open()

    def run_game_loop(self) -> None:
        """This is the main game loop that runs until closed. Eval function takes command line
        parameter and makes it into a function call"""
        while True:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            eval("self." + self.algo + "()")


def main():
    args = get_input_parameters()

    sorter = Visualiser(args.algorithm, args.color)
    sorter.set_initial_screen()
    sorter.set_initial_font()
    sorter.draw_initial_bars_array()
    sorter.run_game_loop()


if __name__ == "__main__":
    main()
