from itertools import permutations

warehouse = [
    [".",".",".",".","."],
    [".",".",".",".","."],
    [".",".",".",".","."],
    [".",".",".",".","."],
    [".",".",".",".","."],
]

warehouse[0][0] = "A"
warehouse[1][3] = "B"
warehouse[2][2] = "C"
warehouse[3][4] = "D"
warehouse[4][1] = "E"
warehouse[4][4] = "I"

product_locations = {
    "A":(0,0),
    "B":(1,3),
    "C":(2,2),
    "D":(3,4),
    "E":(4,1),
}

entrance = (4,4)

picking_list = ["A","C","E"]

def distance(point1,point2):
    row_distance = abs(point1[0] - point2[0])
    col_distance = abs(point1[1] - point2[1])
    return row_distance + col_distance

def get_location(place):
    if place == "I":
        return entrance
    else:
        return product_locations[place]

shortest_distance = None
shortest_route = None

for order in permutations(picking_list):
    route = ["I"] + list(order) + ["I"]

    total_distance = 0

    for i in range(len(route) - 1):
        current = get_location(route[i])
        next_location = get_location(route[i + 1])

        distance_between = distance(current,next_location)

        total_distance = total_distance + distance_between


    if shortest_distance == None:
        shortest_distance = total_distance
        shortest_route = route

    elif total_distance < shortest_distance:
        shortest_distance = total_distance
        shortest_route = route

print("最短距離:",shortest_distance)
print("最短ルート:",shortest_route)
