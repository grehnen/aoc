import os
import requests
import re
from datetime import datetime
from typing import List
from dotenv import load_dotenv

load_dotenv()


def fetch_input(
) -> List[str]:
    filename = f"input/d{day}.txt"
    if os.path.exists(filename):
        print(f"{filename} already exists. Skipping fetch.")
        return get_file_content(filename)

    cookie = {"session": os.getenv("SESSION_COOKIE")}

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    response = requests.get(url, cookies=cookie)
    response.raise_for_status()

    with open(filename, "w") as file:
        file.write(response.text)

    print(f"Content fetched and saved to {filename}")
    return get_file_content(filename)


def get_file_content(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return file.read().splitlines()


def ints(string: str) -> List[int]:
    return [int(i) for i in re.findall(r"-?\d+", string)]


type coord = tuple[int, int]


class Grid:
    DIRECTIONS = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    def __init__(self, grid: List[str]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def __getitem__(self, pos: coord):
        x, y = pos
        if not self.is_in_bounds(pos):
            raise IndexError("Out of bounds")
        return self.grid[y][x]

    def __setitem__(self, pos: coord, value):
        x, y = pos
        if not self.is_in_bounds(pos):
            raise IndexError("Out of bounds")
        self.grid[y] = self.grid[y][:x] + value + self.grid[y][x + 1 :]

    def __str__(self):
        return "\n".join(self.grid)

    def is_in_bounds(self, pos: coord) -> bool:
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def count(self, char: str) -> int:
        return sum(row.count(char) for row in self.grid)

    def find(self, string: str) -> coord:
        """
        Returns the first coordinate where the string is found
        """
        for y, row in enumerate(self.grid):
            x = row.find(string)
            if x != -1:
                return x, y
        raise ValueError(f"String '{string}' not found in grid")

    def find_all(self, string: str) -> List[coord]:
        """
        Returns a list of all coordinates where the string is found
        """
        coords = []
        for y, row in enumerate(self.grid):
            x = row.find(string)
            while x != -1:
                coords.append((x, y))
                x = row.find(string, x + 1)
        return coords

    def neighbors(
        self, pos: coord, diagonal=True, distance=1, include_self=False
    ) -> List[coord]:
        x, y = pos
        offsets = [
            (dx, dy)
            for dx in range(-distance, distance + 1)
            for dy in range(-distance, distance + 1)
            if dx or dy or include_self
        ]
        print(offsets)
        if not diagonal:
            offsets = [(dx, dy) for dx, dy in offsets if dx == 0 or dy == 0]
        return [
            (x + dx, y + dy)
            for dx, dy in offsets
            if self.is_in_bounds((x + dx, y + dy))
        ]

    def neighbor_values(
        self, pos: coord, diagonal=True, distance=1, include_self=False
    ) -> List[str]:
        return [
            self[coord]
            for coord in self.neighbors(pos, diagonal, distance, include_self)
        ]

    def get_any_direction_word_count(self, word: str) -> int:
        sum = 0
        first_letter_coords = self.find_all(word[0])
        for coord in first_letter_coords:
            for direction in range(8):
                dx, dy = self.DIRECTIONS[direction]
                valid = True
                for i in range(1, len(word)):
                    x, y = coord
                    if not (
                        self.is_in_bounds((x + i * dx, y + i * dy))
                        and self[x + i * dx, y + i * dy] == word[i]
                    ):
                        valid = False
                        break
                if valid:
                    sum += 1
        return sum

    def get_pattern_count(
        self,
        pattern: List[str],
        wildcard="*",
        any_rotation=False,
        v_mirror=False,
        h_mirror=False,
    ) -> int:
        sum = 0
        if any_rotation:
            for _ in range(4):
                sum += self.get_pattern_count(
                    pattern, wildcard, v_mirror=v_mirror, h_mirror=h_mirror
                )
                pattern = list(zip(*pattern[::-1]))
            return sum

        if v_mirror:
            sum += self.get_pattern_count(pattern, wildcard, h_mirror=h_mirror)
            pattern = pattern[::-1]
            sum += self.get_pattern_count(pattern, wildcard, h_mirror=h_mirror)
            return sum

        if h_mirror:
            sum += self.get_pattern_count(pattern, wildcard)
            pattern = [row[::-1] for row in pattern]
            sum += self.get_pattern_count(pattern, wildcard)
            return sum

        first_letter_coords = self.find_all(pattern[0][0])
        for x, y in first_letter_coords:
            valid = True
            for dy, row in enumerate(pattern):
                for dx, pattern_char in enumerate(row):
                    if pattern_char == wildcard:
                        continue
                    elif not (
                        self.is_in_bounds((x + dx, y + dy))
                        and self[x + dx, y + dy] == pattern_char
                    ):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                sum += 1
        return sum


if __name__ == "__main__":
    fetch_input()
