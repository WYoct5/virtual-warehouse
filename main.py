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

route = ["I","A","E","C","I"]

for place in route:
    print(place,get_location(place))

total_distance = 0

for i in range(len(route) - 1):
    current = get_location(route[i])
    next_location = get_location(route[i + 1])

    distance_between = distance(current,next_location)

    print(route[i], "→", route[i + 1],":",distance_between)

    total_distance = total_distance + distance_between

print("合計距離:",total_distance)
    



for row in warehouse:
    print("".join(row))