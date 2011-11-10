from collections import namedtuple
from time import time
import logging

class Environment:
  grid = []

  def rows(self):
    return len(self.grid)

  def cols(self):
    return len(self.grid[0])

  # Used in ants library to check if there is an ant already there
  def unoccupied(self, position):
    return True

  # Determine if there is an obstacle blocking the way
  def passable(self, position):
    if self.grid[position[0]][position[1]] != "%":
      return True
    else:
      return False

  def load_map(self, file_name):
    f = open(file_name, 'r')
    for line in f:
      self.grid.append(list(line))

class Search:
  def find_path(self, start_position, goal_position, environment):
    Node = namedtuple('Node', 'position f g h parent depth')
    #logging.error("find_path")

    # TODO: This doesn't consider map wrap around
    # Source: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
    def manhattan_distance(start, goal):
      d = 1 # movement cost
      return d * (abs(start[0] - goal[0]) + abs(start[1] - goal[1]))

    def neighbors(pos):
      directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
      return [((pos[0] + d_row) % environment.rows(), (pos[1] + d_col) % environment.cols())
          for (d_row, d_col) in directions]

    def trace_path(final_node):
      print("trace")
      t = time()
      path = []
      current = final_node
      while current.parent is not None:
        path.append(current.position)
        current = current.parent

      # self.tracing_time += time() - t
      return path

    def has_node_with_position(node_list, position):
      for node in node_list:
        if position == node.position:
          return True
      return False

    open_set = set()
    closed_set = set()

    start_h = manhattan_distance(start_position, goal_position)
    current = Node(start_position, start_h, 0, start_h, None, 0)
    open_set.add(current)
    while open_set:
      # Grab item with minimum F value
      current = min(open_set, key=lambda x:x.f)
      if current.position == goal_position:
        logging.error("steps to find path: " + str(current.depth))
        return trace_path(current)
      open_set.remove(current)
      closed_set.add(current)
      for neighbor in neighbors(current.position):
        if (environment.passable(neighbor) and # Add if passable..
            not has_node_with_position(open_set, neighbor) and # and not open
            not has_node_with_position(closed_set, neighbor) and # or closed
            (current.depth > 1 or environment.unoccupied(neighbor))): # if occupied and next to start
          new_g = current.g + 1
          new_h = manhattan_distance(neighbor, goal_position)
          new = Node(
            neighbor,
            new_g,
            new_h,
            new_g + new_h,
            current,
            current.depth + 1)
          open_set.add(new)
      # If first item has no neighbors, ant is trapped, put a noop on his move list
      if current.depth == 0 and len(open_set) == 0:
        return [current.position]

    # Making it through the loop means we explored all points reachable but
    # did not find our goal
    return None

e = Environment()

s = Search()
# e.load_map("little_maze.txt")
# print(s.find_path((20, 21), (6, 21), e))
e.load_map("big_maze.txt")
print(s.find_path((2, 2), (47, 81), e))
