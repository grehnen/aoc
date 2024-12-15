import os
from typing import List
from utils import fetch_input, Grid, Coord, Vector, ints, floats
from datetime import datetime

filename = os.path.basename(__file__)
day = int(
    "".join(filter(str.isdigit, filename)) or datetime.today().day
    if datetime.today().day <= 25
    else 1
)

directory = os.path.basename(os.path.dirname(__file__))
year = int(
    "".join(filter(str.isdigit, directory)) or datetime.today().year
    if datetime.today().month == 12
    else datetime.today().year - 1
)

file_content: List[str] = fetch_input(day, year)

robots: List[dict] = []
WIDTH = 101
HEIGHT = 103
SECONDS = 10000

for line in file_content:
    x, y, vx, vy = ints(line)
    robots.append(
        {
            "position": Coord(x, y),
            "velocity": Vector(vx, vy),
        }
    )

quad_1 = 0
quad_2 = 0
quad_3 = 0
quad_4 = 0


def print_grid(robots: List[dict], width: int, height: int, second):
    grid = Grid.dots(width, height)
    for robot in robots:
        grid[robot["position"]] = "#"
    if grid.get_pattern_count(["####", "####", "####", "####"]):
        print(grid)
        print(second)
        # Not my proudest work, but it works


for second in range(1, SECONDS):
    for robot in robots:
        robot["position"] += robot["velocity"]
        robot["position"] = robot["position"] % Coord(WIDTH, HEIGHT)
    print_grid(robots, WIDTH, HEIGHT, second)
    if second == 100:
        for robot in robots:
            if robot["position"].x < WIDTH // 2 and robot["position"].y < HEIGHT // 2:
                quad_1 += 1
            elif robot["position"].x < WIDTH // 2 and robot["position"].y > HEIGHT // 2:
                quad_2 += 1
            elif robot["position"].x > WIDTH // 2 and robot["position"].y < HEIGHT // 2:
                quad_3 += 1
            elif robot["position"].x > WIDTH // 2 and robot["position"].y > HEIGHT // 2:
                quad_4 += 1
        a = quad_1 * quad_2 * quad_3 * quad_4
        print(a)


