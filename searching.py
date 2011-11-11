from collections import namedtuple
from time import time
import logging
import heapq

class Environment:
  def __init__(self):
    self.grid = []
    self.neighbors = {}

  def rows(self):
    return len(self.grid)

  def cols(self):
    return len(self.grid[0])

  # Used in ants library to check if there is an ant already there
  def unoccupied(self, position):
    return True

  # Determine if there is an obstacle blocking the way
  def passable(self, position):
    return self.grid[position[0]][position[1]] != "%"

  def load_map(self, file_name):
    f = open(file_name, 'r')
    for line in f:
      self.grid.append(list(line))

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for r in range(self.rows()):
      for c in range(self.cols()):
        self.neighbors[(r,c)] = [((r + d_row) % self.rows(), (c + d_col) % self.cols())
          for (d_row, d_col) in directions]

  

class Search:
  def find_path(self, start_position, goal_position, environment):
    if not environment.passable(goal_position):
        return False
    Node = namedtuple('Node', 'position f g h parent depth')
    #logging.error("find_path")

    # TODO: This doesn't consider map wrap around
    # Source: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
    def manhattan_distance(start, goal):
      d = 1 # movement cost
      return d * (abs(start[0] - goal[0]) + abs(start[1] - goal[1]))

    #def neighbors(pos):
    #  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    #  return [((pos[0] + d_row) % environment.rows(), (pos[1] + d_col) % environment.cols())
    #      for (d_row, d_col) in directions]

    def trace_path(final_node):
      t = time()
      path = []
      current = final_node
      while current.parent is not None:
        path.append(current.position)
        current = current.parent

      # self.tracing_time += time() - t
      return path

    open_nodes = {}
    open_nodes_heap = []
    closed_nodes = {}
    open_heap = []

    start_h = manhattan_distance(start_position, goal_position)
    current = Node(start_position, start_h, 0, start_h, None, 0)
    open_nodes[current.position] = current
    heapq.heappush(open_nodes_heap, (current.f, current))
    while open_nodes:
      # Grab item with minimum F value
      _, current = heapq.heappop(open_nodes_heap)
      del open_nodes[current.position]
      #current = min(open_nodes.values(), key=lambda x:x.f)
      if current.position == goal_position:
        # logging.error("steps to find path: " + str(current.depth))
        return trace_path(current)
      closed_nodes[current.position] = current
      for neighbor in environment.neighbors[current.position]:
        if (environment.passable(neighbor) and # Add if passable..
            neighbor not in open_nodes and # and not open
            neighbor not in closed_nodes and # or closed
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
          open_nodes[new.position] = new
          heapq.heappush(open_nodes_heap, (new.f, new))
      # If first item has no neighbors, ant is trapped, put a noop on his move list
      if current.depth == 0 and len(open_nodes) == 0:
        return [current.position]

    # Making it through the loop means we explored all points reachable but
    # did not find our goal
    return None

e = Environment()

s = Search()
# e.load_map("little_maze.txt")
# print(s.find_path((20, 21), (6, 21), e))
e.load_map("big_maze.txt")
# for i in range(e.cols()):
#   for j in range(e.rows()):

for i in range(20):
  for j in range(20):
    s.find_path((2,2), (i,j), e)
# print(s.find_path((2, 2), (47, 81), e))
