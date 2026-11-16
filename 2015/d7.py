import re
from collections import defaultdict
from math import prod
from typing import TypedDict

from aoc_utils import (
    Coord2,
    Coord3,
    Grid,
    Vector2,
    Vector3,
    fetch_input,
    floats,
    ints,
)

file_content: list[str] = fetch_input(__file__)


def maybeInt(string: str) -> str | int:
    if string.isnumeric():
        return int(string)
    return string


class IncomingWires(TypedDict):
    operator: str
    terms: list[str | int]


def parse():
    values: dict[str, int] = {}
    outgoing: defaultdict[str, list[str]] = defaultdict(list)
    incoming: dict[str, IncomingWires] = {}
    for line in file_content:
        operator = re.search(r"[A-Z]+", line)
        if operator is None:
            term1, result = re.findall(r"[a-z0-9]+", line)
            if term1.isnumeric():
                values[result] = int(term1)
            else:
                incoming[result] = {
                    "terms": [maybeInt(term1)],
                    "operator": "EQUALS",
                }
                outgoing[term1].append(result)
            continue
        operator = operator.group()

        if operator == "NOT":
            term1, result = re.findall(r"[a-z0-9]+", line)
            incoming[result] = {"terms": [maybeInt(term1)], "operator": operator}
            outgoing[term1].append(result)
        else:
            term1, term2, result = re.findall(r"[a-z0-9]+", line)
            incoming[result] = {
                "terms": [maybeInt(term1), maybeInt(term2)],
                "operator": operator,
            }
            outgoing[term1].append(result)
            outgoing[term2].append(result)

    return values, outgoing, incoming


def calc(input: IncomingWires) -> int:
    terms = tuple(input["terms"])
    assert all(isinstance(x, int) for x in terms)

    match input["operator"]:
        case "NOT":
            return 0b1111_1111_1111_1111 - terms[0]  # type: ignore
        case "AND":
            return terms[0] & terms[1]  # type: ignore
        case "OR":
            return terms[0] | terms[1]  # type: ignore
        case "RSHIFT":
            return terms[0] >> terms[1]  # type: ignore
        case "LSHIFT":
            return terms[0] << terms[1]  # type: ignore
        case "EQUALS":
            return terms[0]  # type: ignore
        case _:
            raise TypeError("Unexpected operator:", input["operator"])


def solve(b_override: int | None = None):
    values, outgoing, incoming = parse()
    to_check = set(values.keys())
    if b_override:
        values["b"] = b_override

    for incoming_wire in incoming:
        if all(isinstance(x, int) for x in incoming[incoming_wire]["terms"]):
            values[incoming_wire] = calc(incoming[incoming_wire])
            to_check.add(incoming_wire)

    while to_check:
        wire_with_value = to_check.pop()
        for potentially_active_wire in outgoing[wire_with_value]:
            incoming[potentially_active_wire]["terms"] = [
                values.get(str(incoming_wire), incoming_wire)
                for incoming_wire in incoming[potentially_active_wire]["terms"]
            ]
            if all(
                isinstance(x, int) for x in incoming[potentially_active_wire]["terms"]
            ):
                values[potentially_active_wire] = calc(
                    incoming[potentially_active_wire]
                )
                to_check.add(potentially_active_wire)

    return values["a"]


print(solve())

print(solve(solve()))
