import searching
from random import random

e = searching.Environment()
e.load_map("little_maze.txt")
s = searching.Search(e)
start = (int(random() * e.rows), int(random() * e.cols))
end = (int(random() * e.rows), int(random() * e.cols))

start = (13, 7)
end = (9, 23)

path = s.find_path(start, end)
if path:
  e.visualize_path(path)
print(start, end)
