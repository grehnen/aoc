from typing import List
from utils import fetch_input, Grid, Coord
from datetime import datetime
from concurrent.futures import as_completed, ProcessPoolExecutor
import multiprocessing

ORIENTATIONS: List[Coord] = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def test_position_func(test_position, grid2p, start_position):
    grid2p_copy = grid2p.copy()
    position = start_position
    orientation = ORIENTATIONS[0]
    done_steps = set()

    grid2p_copy[test_position] = "#"
    while grid2p_copy.is_in_bounds(position):
        new_position, new_orientation = move_one_step(
            grid2p_copy, position, orientation
        )
        if str((position, new_position)) in done_steps:
            grid2p_copy[test_position] = "."
            return test_position
        done_steps.add(str((position, new_position)))
        position = new_position
        orientation = new_orientation
    grid2p_copy[test_position] = "."
    return None


def next_orientation(orientation: Coord) -> Coord:
    return Coord(ORIENTATIONS[(ORIENTATIONS.index(orientation) + 1) % 4])


def move_one_step(
    grid: Grid, current: Coord, orientation: Coord
) -> tuple[Coord, Coord]:
    while True:
        forward_position = current + orientation
        if not grid.is_in_bounds(forward_position) or grid[forward_position] != "#":
            return forward_position, orientation
        orientation = next_orientation(orientation)


if __name__ == "__main__":
    file_content: List[str] = fetch_input(__file__)

    grid = Grid(file_content.copy())

    start_time = datetime.now()
    start_position = grid.find("^")
    position = start_position
    orientation = ORIENTATIONS[0]

    done_steps = set()

    while grid.is_in_bounds(position):
        grid[position] = "X"
        new_position, new_orientation = move_one_step(grid, position, orientation)
        done_steps.add(str((position, new_position)))
        position = new_position
        orientation = new_orientation

    print(grid.count("X"))
    print(f"Part 1: {datetime.now() - start_time}")

    # Part 2
    grid2 = grid.copy()
    start_time = datetime.now()
    possible_positions = set()
    grid2[start_position] = "."

    test_positions = grid2.find_all("X")

    for test_position in test_positions:
        position = start_position
        orientation = ORIENTATIONS[0]
        done_steps = set()

        test_position = grid2.find("X")
        grid2[test_position] = "#"
        loop = False
        looper = 0
        while grid2.is_in_bounds(position):
            looper += 1
            new_position, new_orientation = move_one_step(grid2, position, orientation)
            if str((position, new_position)) in done_steps:
                possible_positions.add(test_position)
                break
            done_steps.add(str((position, new_position)))
            if looper > 10000:
                print(str((position, new_position)))
            position = new_position
            orientation = new_orientation

        grid2[test_position] = "."

    print(len(possible_positions))
    print(f"Part 2: {datetime.now() - start_time}")

    # Part 2 (Parallelized)
    start_time = datetime.now()
    possible_positions = set()
    grid2p = grid.copy()
    grid2p[start_position] = "."

    test_positions = grid2p.find_all("X")

    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        futures = [
            executor.submit(test_position_func, pos, grid2p, start_position)
            for pos in test_positions
        ]
        for future in as_completed(futures):
            result = future.result()
            if result:
                possible_positions.add(result)

    print(len(possible_positions))
    print(f"Part 2 (Parallelized): {datetime.now() - start_time}")
