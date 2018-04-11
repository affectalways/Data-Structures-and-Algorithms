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


# 广度优先搜索
def maze_solver_queue_backtracking(start_position, end_position):
    if list(start_position) == end_position:
        print '到达出口'
        return
    # create queue:队列
    queue = []
    # mark position
    mark(start_position)
    queue.append(start_position)
    # queue is not empty, execute while loop
    while len(queue):
        position = queue.pop()
        for direction in direction_keys:
            next_step = position[0] + direction[0], position[1] + direction[1]
            # check passage
            if passage(next_step):
                mark(next_step)
                if list(next_step) == end_position:
                    print '找到出口！'
                    return
                queue.append(next_step)
    print 'no path, help'


# 深度优先搜索
def maze_solver_stack_backtracking(start_position, end_position):
    if list(start_position) == end_position:
        print '到达出口'
        return

    # create stack 栈
    stack = []
    # mark have to been, =2
    mark(start_position)
    # push start_position into stack
    stack.insert(0, start_position)

    while len(stack):
        # get the top element of stack
        position = stack.pop(0)
        # in proper order examine every direction
        for direction in direction_keys:
            next_step = position[0] + direction[0], position[1] + direction[1]
            # if next_step equals end_position, finish the procedure
            if list(next_step) == end_position:
                print '到达出口'
                return
            # if next_step passage
            if passage(next_step):
                # quondam position push into the stack
                stack.insert(0, position)
                # push into the stack as top element
                stack.insert(0, next_step)
                # mark arrived, =2
                mark(next_step)
                # exit for circulation, do the next iteration
                break
    print 'no path, help'


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
    # remove the needless position
    path_leave_maze.pop()
    return False


if __name__ == "__main__":
    # x,y format
    # maze_solver([1, 1], [10, 12])
    # maze_solver_stack_backtracking([1, 1], [10, 12])
    maze_solver_queue_backtracking([1, 1], [10, 12])
