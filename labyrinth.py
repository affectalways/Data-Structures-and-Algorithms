# -*- coding:UTF-8 -*-

# right, down, left, up
direction_keys = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 迷宫， 坐标想成x，y直角坐标系
# 14列，12行
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

path_leave_maze = []


# 标记为已经到达过
def mark(position):
    maze[position[0]][position[1]] = 2


# 检查是否已经到过
def whether_have_been_to(position):
    return maze[position[0]][position[1]] == 2


# 检查是否通行，返回True，Flase
def passage(position):
    return maze[position[0]][position[1]] == 0


# 定义迷宫 起始位置 和 出口 （两个都必须为0）
def maze_solver(start_position, end_position):
    if whether_have_been_to(start_position):
        return False
    
    # append the current_position into path_leave_maze
    path_leave_maze.append(start_position)

    # mark have been to, =2
    mark(position=start_position)

    # whether to reach the exit
    if list(start_position) == end_position:
        print path_leave_maze
        print '已经到达出口'
        return True

    # try four directions
    for direction in direction_keys:
        next_step = start_position[0] + direction[0], start_position[1] + direction[1]
        # whether the passage
        if passage(next_step):
            if maze_solver(next_step, end_position):
                return True
    # remove the needless postion
    path_leave_maze.pop()
    return False


if __name__ == "__main__":
    # x,y format
    maze_solver([1, 1], [10, 12])
