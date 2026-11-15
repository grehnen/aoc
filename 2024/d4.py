from aoc_utils import Grid, fetch_input

file_content: list[str] = fetch_input(__file__)


grid = Grid(file_content)

sumA = grid.get_any_direction_word_count("XMAS")
print(sumA)

pattern = ["M*S", "*A*", "M*S"]
sumB = grid.get_pattern_count(pattern, any_rotation=True)
print(sumB)
