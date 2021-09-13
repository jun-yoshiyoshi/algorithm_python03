def walk(x, y):  # 再帰で迷路を解く
    global goal
    maze[y][x] = 2
    print_maze()
    if x == gx and y == gy:
        goal = True
    if goal == False and maze[y - 1][x] == 0:
        walk(x, y - 1)
    if goal == False and maze[y + 1][x] == 0:
        walk(x, y + 1)
    if goal == False and maze[y][x + 1] == 0:
        walk(x + 1, y)
    if goal == False and maze[y][x - 1] == 0:
        walk(x - 1, y)
    if goal == True:
        print("{},{}".format(x, y))


def print_maze():
    print("----------------")
    for y in range(5):
        for x in range(7):
            if maze[y][x] == 0:
                print(" ", end="")
            if maze[y][x] == 1:
                print("#", end="")
            if maze[y][x] == 2:
                print("*", end="")
        print("")


maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]
gx, gy, goal = 5, 3, False

walk(1, 1)
if goal == False:
    print("ゴールに到達できなかった")
