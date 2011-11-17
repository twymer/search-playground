#!/usr/local/bin/python3
import searching
from random import random

e = searching.Environment()
e.load_map("little_maze.txt")
s = searching.Search(e)
start = (int(random() * e.rows), int(random() * e.cols))
end = (int(random() * e.rows), int(random() * e.cols))

start = (13, 7)
end = (9, 23)

# This set demonstrates that start gets explored after we open
# the first real node
# Also that the end node never technically gets expanded which means our
# path distance is one off from correct
start = (9, 19)
end = (14, 19)

# s.visualize_path(start, end)
def goal_method(node):
  return node == (14, 19)
s.visualize_bfs(start, goal_method)
print(start, end)
