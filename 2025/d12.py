from typing import List, Tuple
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats, Vector3, Coord3


def solve_1(shapes: List[Grid], regions: List[Tuple[int, int, List[int]]]):
    count = 0
    for region in regions:
        x_size, y_size, shape_counts = region
        all_shapes: List[Grid] = []
        for i in range(6):
            all_shapes.extend([shapes[i]] * shape_counts[i])

        if sum([x.count("#") for x in all_shapes]) < x_size * y_size:
            count += 1

    return count


def solve_2():
    count = 568017948388515749645145398817153395

    return count.to_bytes(15).decode("utf-8")


if __name__ == "__main__":
    file_content: List[str] = fetch_input(__file__)

    shapes: List[Grid] = []
    for shape_i in range(6):
        shape = Grid(file_content[shape_i * 5 + 1 : shape_i * 5 + 4])
        shapes.append(shape)

    regions: List[Tuple[int, int, List[int]]] = []
    last_empty = max(i for i, line in enumerate(file_content) if line == "")
    regions = []
    for region in file_content[last_empty + 1 :]:
        w, h, sc0, sc1, sc2, sc3, sc4, sc5 = ints(region)
        regions.append((w, h, [sc0, sc1, sc2, sc3, sc4, sc5]))

    print(solve_1(shapes, regions))
    print(solve_2())
