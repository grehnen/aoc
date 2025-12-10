from typing import List, NamedTuple
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats, Vector3, Coord3
import heapq
import z3

file_content: List[str] = fetch_input(__file__)
example = [
    "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
]


def press_button_1(lights: tuple[bool, ...], button: tuple[int, ...]) -> List[bool]:
    new_lights = list(lights)
    for index in button:
        new_lights[index] = not lights[index]

    return new_lights


def solve_row_1(line: dict) -> int:
    wanted_lights: tuple[bool, ...] = line["lights"]
    buttons = line["buttons"]

    current_lights = [False] * len(wanted_lights)
    known_states = {}
    to_check = [(0, current_lights)]
    heapq.heapify(to_check)
    for presses, lights in to_check:
        if tuple(lights) == wanted_lights:
            return presses
        for button in buttons:
            new_lights = press_button_1(tuple(lights), button)
            state_tuple = tuple(new_lights)
            if (
                state_tuple not in known_states
                or known_states[state_tuple] > presses + 1
            ):
                known_states[state_tuple] = presses + 1
                heapq.heappush(to_check, (presses + 1, new_lights))

    raise ValueError("No solution found")


def solve_1(lines: List[dict]) -> int:
    count = 0
    for line in lines:
        count += solve_row_1(line)

    return count


def press_button_2(jolts: tuple[int, ...], button: tuple[int, ...]) -> tuple[int, ...]:
    new_jolts = list(jolts)
    for index in button:
        new_jolts[index] += 1
    return tuple(new_jolts)


def solve_row_2(line: dict) -> int:
    wanted_jolt: tuple[int, ...] = line["joltage"]
    buttons: tuple[tuple[int, ...], ...] = line["buttons"]

    optimizer = z3.Optimize()
    # Create variables for each button
    button_vars = [z3.Int(f"b_{i}") for i in range(len(buttons))]
    for var in button_vars:
        optimizer.add(var >= 0)

    jolt_buttons: List[tuple[list[int], int]] = []

    # Map each jolt index to the buttons that affect it
    for jc_i, jolt_goal in enumerate(wanted_jolt):
        button_indexes = []
        for b_i, button in enumerate(buttons):
            if jc_i in button:
                button_indexes.append(b_i)
        jolt_buttons.append((button_indexes, jolt_goal))

    for button_indexes, jolt_goal in jolt_buttons:
        # Create a sum expression that sums the presses of the affecting buttons for this jolt counter
        jolt_sum = z3.Sum([button_vars[b_i] for b_i in button_indexes])
        
        # Add constraint that this sum equals the wanted jolt count
        optimizer.add(jolt_sum == jolt_goal)

    # Create a sum expression for total button presses and minimize it
    total_presses = z3.Sum(button_vars)
    optimizer.minimize(total_presses)

    if optimizer.check() == z3.sat:
        model = optimizer.model()
        return sum(model[var].as_long() for var in button_vars)  # type: ignore

    raise ValueError("No solution found")


def solve_2(lines: List[dict]) -> int:
    count = 0
    for line in lines:
        count += solve_row_2(line)

    return count


if __name__ == "__main__":
    lines: List[dict] = []

    for line in file_content:
        s_line = line.split()
        lines.append(
            {
                "lights": tuple(x == "#" for x in s_line[0] if x in "#."),
                "buttons": tuple(tuple(ints(x)) for x in s_line[1:-1]),
                "joltage": tuple(ints(s_line[-1])),
            }
        )

    print(solve_1(lines))
    print(solve_2(lines))
