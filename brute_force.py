import searching

e = searching.Environment()
# e.load_map("big_maze.txt")
e.load_map("little_maze.txt")
s = searching.Search(e)

for start_row in range(e.rows()):
  for start_col in range(e.cols()):
    for goal_row in range(e.rows()):
      for goal_col in range(e.cols()):
        print(start_row, start_col, " to ", goal_row, goal_col, " dist: ", s.manhattan_distance((start_row, start_col), (goal_row, goal_col)))
