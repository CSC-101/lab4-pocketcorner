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
    pos_points = [coords for coords in quads if coords[0]> 0 and coords[1] > 0]
    print(pos_points)
    return pos_points




# Part 4


# Part 5


# Part 6


