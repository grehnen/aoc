import os
import requests
import re
from datetime import datetime
from typing import List
from dotenv import load_dotenv

load_dotenv()


def fetch_input(file_path: str) -> List[str]:
    year, day = get_date(file_path)
    file_dir = os.path.dirname(os.path.abspath(file_path))
    input_dir = os.path.join(file_dir, "input")
    os.makedirs(input_dir, exist_ok=True)
    filename = os.path.join(input_dir, f"d{day}.txt")
    if os.path.exists(filename):
        print(f"{filename} already exists. Skipping fetch.")
        return get_file_content(filename)

    session_cookie = os.getenv("SESSION_COOKIE")
    if not session_cookie:
        raise ValueError("SESSION_COOKIE environment variable is not set")

    cookie = {"session": session_cookie}

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    response = requests.get(url, cookies=cookie)
    response.raise_for_status()

    with open(filename, "w") as file:
        file.write(response.text)

    print(f"Content fetched and saved to {filename}")
    return get_file_content(filename)


def get_date(file: str) -> tuple[int, int]:
    filename = os.path.basename(file)
    day = int(
        "".join(filter(str.isdigit, filename))
        or (datetime.today().day if datetime.today().day <= 25 else 1)
    )

    directory = os.path.basename(os.path.dirname(file))
    year = int(
        "".join(filter(str.isdigit, directory))
        or (
            datetime.today().year
            if datetime.today().month == 12
            else datetime.today().year - 1
        )
    )
    return year, day


def get_file_content(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return file.read().splitlines()


def ints(string: str) -> List[int]:
    return [int(i) for i in re.findall(r"-?\d+", string)]


def floats(string: str) -> List[float]:
    return [float(i) for i in re.findall(r"-?\d+(?:\.\d+)?", string)]


class Coord:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], tuple) and len(args[0]) == 2:
            self.x, self.y = args[0]
        elif len(args) == 2 and all(isinstance(arg, int) for arg in args):
            self.x, self.y = args
        else:
            raise TypeError("Coord() takes either a tuple or two integer arguments")

    def __add__(self, other) -> "Coord":
        if isinstance(other, Coord):
            return Coord(self.x + other.x, self.y + other.y)
        elif (
            isinstance(other, tuple)
            and len(other) == 2
            and all(isinstance(i, int) for i in other)
        ):
            return Coord(self.x + other[0], self.y + other[1])
        elif isinstance(other, int):
            return Coord(self.x + other, self.y + other)
        else:
            raise TypeError("Operand must be Coord or tuple of two integers")

    def __sub__(self, other) -> "Coord":
        if isinstance(other, Coord):
            return Coord(self.x - other.x, self.y - other.y)
        elif (
            isinstance(other, tuple)
            and len(other) == 2
            and all(isinstance(i, int) for i in other)
        ):
            return Coord(self.x - other[0], self.y - other[1])
        else:
            raise TypeError("Operand must be Coord or tuple of two integers")

    def __mul__(self, other: int) -> "Coord":
        return Coord(self.x * other, self.y * other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
        return False

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __getitem__(self, index: int) -> int:
        return (self.x, self.y)[index]

    def __setitem__(self, index: int, value: int):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")

    def __contains__(self, item):
        return item in (self.x, self.y)

    def __iter__(self):
        return iter((self.x, self.y))

    def __hash__(self):
        return hash((self.x, self.y))

    def __mod__(self, other: "Coord") -> "Coord":
        return Coord(self.x % other.x, self.y % other.y)


class Vector(Coord):
    RIGHT: "Vector"
    LEFT: "Vector"
    DOWN: "Vector"
    UP: "Vector"

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Coord):
            self.x, self.y = args[0]
        else:
            super().__init__(*args)

    def manhattan_distance(self) -> int:
        return abs(self.x) + abs(self.y)

    def chebyshev_distance(self) -> int:
        return max(abs(self.x), abs(self.y))

    def euclidean_distance(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def perpendicular(self) -> "Vector":
        return Vector(self.y, -self.x)

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y)

    def __add__(self, other) -> "Vector":
        return Vector(super().__add__(other))

    @staticmethod
    def all_directions(diagonal=True) -> List["Vector"]:
        directions = [Vector(0, 1), Vector(1, 0), Vector(0, -1), Vector(-1, 0)]
        if diagonal:
            directions += [Vector(1, 1), Vector(-1, -1), Vector(1, -1), Vector(-1, 1)]
        return directions


# Note: These assumes origo at top-left corner, x increases to the right, y increases downwards.
Vector.RIGHT = Vector(1, 0)
Vector.LEFT = Vector(-1, 0)
Vector.DOWN = Vector(0, 1)
Vector.UP = Vector(0, -1)


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

    def __getitem__(self, pos: Coord):
        x, y = pos
        if not self.is_in_bounds(pos):
            raise IndexError("Out of bounds")
        return self.grid[y][x]

    def __setitem__(self, pos: Coord, value):
        x, y = pos
        if not self.is_in_bounds(pos):
            raise IndexError("Out of bounds")
        self.grid[y] = self.grid[y][:x] + value + self.grid[y][x + 1 :]

    def __str__(self):
        return "\n".join(self.grid)

    @staticmethod
    def dots(width: int, height: int) -> "Grid":
        return Grid(["." * width] * height)

    def copy(self):
        return Grid(self.grid.copy())

    def is_in_bounds(self, pos: Coord) -> bool:
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def count(self, char: str) -> int:
        return sum(row.count(char) for row in self.grid)

    def find(self, string: str) -> Coord:
        """
        Returns the first coordinate where the string is found
        """
        for y, row in enumerate(self.grid):
            x = row.find(string)
            if x != -1:
                return Coord(x, y)
        raise ValueError(f"{string} not found")

    def find_all(self, string: str) -> List[Coord]:
        """
        Returns a list of all coordinates where the string is found
        """
        coords = []
        for y, row in enumerate(self.grid):
            x = row.find(string)
            while x != -1:
                coords.append(Coord(x, y))
                x = row.find(string, x + 1)
        return coords

    def get_char_set(self, ignore="") -> set[str]:
        char_set = set(char for row in self.grid for char in row)
        for char in ignore:
            char_set.remove(char)
        return char_set

    def neighbors(
        self,
        pos: Coord,
        diagonal=True,
        distance=1,
        include_self=False,
        include_out_of_bounds=False,
    ) -> List[Coord]:
        x, y = pos
        offsets = [
            (dx, dy)
            for dx in range(-distance, distance + 1)
            for dy in range(-distance, distance + 1)
            if dx or dy or include_self
        ]
        if not diagonal:
            offsets = [(dx, dy) for dx, dy in offsets if dx == 0 or dy == 0]
        return [
            Coord(x + dx, y + dy)
            for dx, dy in offsets
            if self.is_in_bounds(Coord(x + dx, y + dy)) or include_out_of_bounds
        ]

    def neighbor_values(
        self, pos: Coord, diagonal=True, distance=1, include_self=False
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
                        self.is_in_bounds(Coord(x + i * dx, y + i * dy))
                        and self[Coord(x + i * dx, y + i * dy)] == word[i]
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
                pattern = list(zip(*pattern[::-1]))  # type: ignore TODO: fix this
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
                        self.is_in_bounds(Coord(x + dx, y + dy))
                        and self[Coord(x + dx, y + dy)] == pattern_char
                    ):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                sum += 1
        return sum

    def a_star(
        self,
        start_marker: str = "S",
        goal_marker: str = "E",
        start: Coord | None = None,
        goal: Coord | None = None,
        inpassable: str = "#",
    ) -> List[Coord]:
        if start is None:
            start = self.find(start_marker)
        if goal is None:
            goal = self.find(goal_marker)
        assert start is not None and goal is not None

        directions = Vector.all_directions(diagonal=False)
        locations: dict[Coord, int] = {start: 0}
        prev_step: dict[Coord, Coord | None] = {start: None}
        visited: set[Coord] = set()

        current_location = start
        while current_location != goal:
            for direction in directions:
                new_location = current_location + direction
                if (
                    self.is_in_bounds(new_location)
                    and new_location not in visited
                    and self[new_location] != inpassable
                ):
                    locations[new_location] = locations[current_location] + 1
                    prev_step[new_location] = current_location
            visited.add(current_location)
            del locations[current_location]
            if not locations:
                return []
            current_location = min(
                locations,
                key=lambda k: locations[k] + Vector(goal - k).manhattan_distance(),
            )

        path = []
        while current_location:
            path.append(current_location)
            current_location = prev_step[current_location]
        path.reverse()
        return path


if __name__ == "__main__":
    fetch_input(__file__)
