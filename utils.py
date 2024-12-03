import os
import requests
import re
from datetime import datetime
from typing import List
from dotenv import load_dotenv
from typing import NamedTuple

load_dotenv()


def fetch_input(day: int = datetime.today().day) -> List[str]:
    filename = f"input/d{day}.txt"
    if os.path.exists(filename):
        print(f"{filename} already exists. Skipping fetch.")
        return get_file_content(filename)

    cookie = {"session": os.getenv("SESSION_COOKIE")}

    url = f"https://adventofcode.com/2024/day/{day}/input"

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
    def __init__(self, grid: List[str]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def __getitem__(self, pos: coord):
        x, y = pos
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise IndexError("Out of bounds")
        return self.grid[y][x]

    def __setitem__(self, pos: coord, value):
        x, y = pos
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise IndexError("Out of bounds")
        self.grid[y] = self.grid[y][:x] + value + self.grid[y][x+1:]

    def __str__(self):
        return "\n".join(self.grid)

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

    def neighbors(self, pos: coord, diagonal = True, distance = 1, include_self = False) -> List[coord]:
        x, y = pos
        offsets = [(dx, dy) for dx in range(-distance, distance + 1) for dy in range(-distance, distance + 1) if dx or dy or include_self]
        print(offsets)
        if not diagonal:
            offsets = [(dx, dy) for dx, dy in offsets if dx == 0 or dy == 0]
        return [(x + dx, y + dy) for dx, dy in offsets if 0 <= x + dx < self.width and 0 <= y + dy < self.height]

    def neighbor_values(self, pos: coord, diagonal = True, distance = 1, include_self = False) -> List[str]:
        return [self[coord] for coord in self.neighbors(pos, diagonal, distance, include_self)]


if __name__ == "__main__":
    today = datetime.today().day
    fetch_input(today)
