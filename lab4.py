import math

import data

# Write your functions for each part in the space below.

# Part 1

def first_element(ins:list[list[int]]) -> list[int]:
    element_list = []
    for sub_list in ins:
        if len(sub_list) > 0:
            element_list.append(sub_list[0])
    return element_list



# Part 2
def x_coordinates(points:list[data.Point]) -> list[float]:
    x_coords = [points.x for points in points]
    print(x_coords)
    return x_coords



# Part 3
def are_in_positive_quadrant(quads:list[data.Point]) -> list[data.Point]:
    pos_points = [coords for coords in quads if coords.x > 0 and coords.y > 0]
    print(pos_points)
    return pos_points

# are_in_positive_quadrant([data.Point(-6,4), data.Point(2,-2049643), data.Point(4,43)])


# Part 4
def distance(point_1:data.Point, point_2:data.Point) -> float:
    width = point_1.x - point_2.x
    length = point_1.y - point_2.y
    euclidean = math.sqrt(width**2+length**2)
    print(euclidean)
    return euclidean

# distance(data.Point(-6,4), data.Point(2,7))

# Part 5
def manhattan_distance(point_1:data.Point, point_2:data.Point) -> float:
    width = point_1.x - point_2.x
    length = point_1.y - point_2.y
    man = math.fabs(width) + math.fabs(length)
    print(man)
    return man

# manhattan_distance(data.Point(-6,4), data.Point(2,7))

# Part 6
def distance_all(corbin:list[data.Point]) -> list[float]:
    origin_distances = []
    for point in corbin:
        p = distance(point, data.Point(0,0))
        origin_distances.append(p)
    print(origin_distances)
    return origin_distances

distance_all([data.Point(-6,4), data.Point(2,-2049643), data.Point(4,43)])


