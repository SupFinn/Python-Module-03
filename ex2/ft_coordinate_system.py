#!/usr/bin/python3

import math

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)

    # ---- First coordinate ----
    coord1 = "10,20,5"
    coords1 = coord1.split(",")

    x1 = int(coords1[0])
    y1 = int(coords1[1])
    z1 = int(coords1[2])

    position1 = (x1, y1, z1)

    distance1 = math.sqrt(
        (x1 - origin[0]) ** 2 +
        (y1 - origin[1]) ** 2 +
        (z1 - origin[2]) ** 2
    )

    print(f"Position created: {position1}")
    print(f"Distance between {origin} and {position1}: {distance1:.2f}\n")

    # ---- Second coordinate ----
    coord2 = "3,4,0"
    print(f'Parsing coordinates: "{coord2}"')

    coords2 = coord2.split(",")

    x2 = int(coords2[0])
    y2 = int(coords2[1])
    z2 = int(coords2[2])

    position2 = (x2, y2, z2)

    distance2 = math.sqrt(
        (x2 - origin[0]) ** 2 +
        (y2 - origin[1]) ** 2 +
        (z2 - origin[2]) ** 2
    )

    print(f"Parsed position: {position2}")
    print(f"Distance between {origin} and {position2}: {distance2}\n")

    # ---- Invalid coordinate ----
    invalid = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid}"')

    try:
        invalid_coords = invalid.split(",")

        int(invalid_coords[0])
        int(invalid_coords[1])
        int(invalid_coords[2])

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}",)')
        print()

    # ---- Unpacking demonstration ----
    print("Unpacking demonstration:")
    print(f"Player at x={x2}, y={y2}, z={z2}")
    print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
