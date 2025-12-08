from typing import List, Set
from utils import Coord3, fetch_input, Grid, Coord2, Vector2, ints, floats, Vector3, prod

file_content: List[str] = fetch_input(__file__)
examples = [
    "162,817,812",
    "57,618,57",
    "906,360,560",
    "592,479,940",
    "352,342,300",
    "466,668,158",
    "542,29,236",
    "431,825,988",
    "739,650,466",
    "52,470,668",
    "216,146,977",
    "819,987,18",
    "117,168,530",
    "805,96,715",
    "346,949,466",
    "970,615,88",
    "941,993,340",
    "862,61,35",
    "984,92,344",
    "425,690,689",
]
ITERATIONS = 1_000


def solve(
    all_coords: List[Coord3],
):
    all_distances: List[float] = []
    distance_dict: dict[float, tuple[Coord3, Coord3]] = {}
    for i, coord_a in enumerate(all_coords):
        for coord_b in all_coords[i + 1 :]:
            vector = Vector3(coord_b - coord_a)
            distance = Vector2.euclidean_distance()
            all_distances.append(distance)
            distance_dict[distance] = (coord_a, coord_b)

    all_distances.sort()

    clusters: List[Set[Coord3]] = []
    answer_1 = None
    answer_2 = None
    for j, distance in enumerate(all_distances):
        coord_a, coord_b = distance_dict[distance]
        first_cluster_index = None
        for i, cluster in enumerate(clusters):
            intersection = cluster.intersection({coord_a, coord_b})
            if coord_a in intersection and coord_b in intersection:
                first_cluster_index = i
                break
            if coord_a in intersection or coord_b in intersection:
                if first_cluster_index is None:
                    first_cluster_index = i
                    clusters[i].add(coord_a)
                    clusters[i].add(coord_b)
                else:
                    clusters[first_cluster_index].update(cluster)
                    clusters.pop(i)
                    break
        if first_cluster_index is None:
            clusters.append({coord_a, coord_b})
        
        if j == ITERATIONS - 1:
            clusters.sort(key=len, reverse=True)
            answer_1 = prod(len(cluster) for cluster in clusters[:3])
        
        if len(clusters) == 1 and len(clusters[0]) == len(all_coords):
            answer_2 = coord_a.x * coord_b.x
        
        if answer_1 and answer_2:
            return answer_1, answer_2


if __name__ == "__main__":
    all_coords = [Coord3(tuple(ints(line))) for line in file_content]

    print(solve(all_coords))
