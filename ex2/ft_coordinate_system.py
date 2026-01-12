#!/usr/bin/python3

import math


def parse_coordinates(coord_str: str) -> tuple:
    """
    Parse a string like "x,y,z" into a 3D tuple (x, y, z).
    """

    parts = coord_str.split(",")

    if len(parts) != 3:
        print("Coordinates must be 3D")

    try:
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
    except ValueError as e:
        print(e)

    return tuple((x, y, z))


def distance_3d(p1: tuple, p2: tuple) -> float:
    """
    Calculate the Euclidean distance between two 3D points.
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def main() -> None:
    """
    Game Coordinate System: Parses 3D coordinates and calculates distances.

    Demonstrates:
    - Parsing coordinates from strings
    - Calculating distance from the origin
    - Handling invalid input
    - Unpacking coordinate tuples
    """
    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)

    # ---- First coordinate ----
    coord = "10,20,5"
    position = parse_coordinates(coord)

    print(f"Position created: {position}")

    dist = distance_3d(origin, position)
    print(
        f"Distance between {origin} and {position}: {dist:.2f}"
    )

    # ---- Second coordinate ----
    coord = "3,4,0"
    print(f'\nParsing coordinates: "{coord}"')

    position = parse_coordinates(coord)
    print(f"Parsed position: {position}")

    dist = distance_3d(origin, position)
    print(
        f"Distance between {origin} and {position}: {dist}"
    )

    # ---- Invalid coordinate ----
    coord = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{coord}"')

    try:
        parse_coordinates(coord)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(
            f'Error details - Type: ValueError, Args: ("{e}",)'
        )

    # ---- Unpacking demonstration ----
    print("\nUnpacking demonstration:")

    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
