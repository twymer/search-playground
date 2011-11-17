#!/usr/local/bin/python3
import unittest
import searching

class TestManhattan(unittest.TestCase):
  def setUp(self):
    self.e = searching.Environment()
    self.e.load_map("big_maze.txt")
    self.search = searching.Search(self.e)
    self.d = 1

  def test_neighbors(self):
    self.assertEqual(self.search.manhattan_distance((0,0), (0,1)), 1 * self.d)

  def test_backwards(self):
    self.assertEqual(self.search.manhattan_distance((5,0), (0,0)), 5 * self.d)

  def test_diagonal(self):
    self.assertEqual(self.search.manhattan_distance((0,0), (3,3)), 6 * self.d)

  def test_left_overlap(self):
    self.assertEqual(self.search.manhattan_distance((0,0), (0, self.e.cols - 1)), 1 * self.d)

  def test_top_overlap(self):
    self.assertEqual(self.search.manhattan_distance((0,0), (self.e.rows - 1, 0)), 1 * self.d)

  def test_diagonal_overlap(self):
    self.assertEqual(self.search.manhattan_distance((0,0), (self.e.rows - 1, self.e.cols - 1)), 2 * self.d)

  def test_edge_to_center(self):
    self.assertEqual(self.search.manhattan_distance((22,0), (4,1)), 19 * self.d)
    self.assertEqual(self.search.manhattan_distance((0,111), (4,1)), 6 * self.d)
    self.assertEqual(self.search.manhattan_distance((111,111), (4,1)), 7 * self.d)

  def middle_tests(self):
    self.assertEqual(self.search.manhattan_distance((49,0), (51,0)), 2 * self.d)
    self.assertEqual(self.search.manhattan_distance((50,0), (51,0)), 1 * self.d)
    self.assertEqual(self.search.manhattan_distance((0,49), (0,51)), 2 * self.d)
    self.assertEqual(self.search.manhattan_distance((49,49), (51,51)), 4 * self.d)

    self.assertEqual(self.search.manhattan_distance((51,0), (49,0)), 2 * self.d)
    self.assertEqual(self.search.manhattan_distance((51,0), (50,0)), 1 * self.d)
    self.assertEqual(self.search.manhattan_distance((0,51), (0,49)), 3 * self.d)
    self.assertEqual(self.search.manhattan_distance((51,51), (49,49)), 4 * self.d)

class TestFindPath(unittest.TestCase):
  def setUp(self):
    self.e = searching.Environment()
    self.e.load_map("little_maze.txt")
    self.search = searching.Search(self.e)
    self.d = 4

  def test_neighbors(self):
    self.assertEqual(len(self.search.find_path((10,10), (11,10))), 1)

  def test_further_apart(self):
    def goal_state(node):
      return node == (19,19)
    path = self.search.find_path((19,8), (19,19))
    self.assertEqual(len(path), 11)
    bfs_path, _, _ = self.search.bfs_path((19,8), goal_state)
    self.assertEqual(len(bfs_path), len(path))

  def test_around_things(self):
    def goal_state(node):
      return node == (14,19)
    path = self.search.find_path((9,19), (14,19))
    bfs_path, _, _ = self.search.bfs_path((9,19), goal_state)
    self.assertEqual(len(path), 13)
    self.assertEqual(len(bfs_path), len(path))

if __name__ == '__main__':
  unittest.main()
