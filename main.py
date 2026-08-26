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

for product in picking_list:
    location = product_locations[product]
    print(product,location)

def distance(point1,point2):
    row_distance = abs(point1[0] - point2[0])
    col_distance = abs(point1[1] - point2[1])
    return row_distance + col_distance

def get_location(place):
    if place == "I":
        return entrance
    else:
        return product_locations[place]

route = ["I","A","C","E","I"]

for place in route:
    print(place,get_location(place))

for i in range(len(route) - 1):
    print(route[i], "→", route[i + 1])

for row in warehouse:
    print("".join(row))