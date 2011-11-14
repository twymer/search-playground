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
    self.assertEqual(self.search.manhattan_distance((0,0), (0, self.e.cols() - 1)), 1 * self.d)

  def test_top_overlap(self):
    self.assertEqual(self.search.manhattan_distance((0,0), (self.e.rows() - 1, 0)), 1 * self.d)

  def test_diagonal_overlap(self):
    self.assertEqual(self.search.manhattan_distance((0,0), (self.e.rows() - 1, self.e.cols() - 1)), 2 * self.d)

  def test_edge_to_center(self):
    self.assertEqual(self.search.manhattan_distance((0,22), (4,1)), 25 * self.d)

  def middle_tests(self):
    self.assertEqual(self.search.manhattan_distance((49,0), (51,0)), 2 * self.d)
    self.assertEqual(self.search.manhattan_distance((50,0), (51,0)), 1 * self.d)
    self.assertEqual(self.search.manhattan_distance((0,49), (0,51)), 2 * self.d)
    self.assertEqual(self.search.manhattan_distance((49,49), (51,51)), 4 * self.d)

    self.assertEqual(self.search.manhattan_distance((51,0), (49,0)), 2 * self.d)
    self.assertEqual(self.search.manhattan_distance((51,0), (50,0)), 1 * self.d)
    self.assertEqual(self.search.manhattan_distance((0,51), (0,49)), 3 * self.d)
    self.assertEqual(self.search.manhattan_distance((51,51), (49,49)), 4 * self.d)

if __name__ == '__main__':
  unittest.main()
