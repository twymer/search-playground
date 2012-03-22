Search Playground
=================

About
-----

This project exists because I needed a place to test functionality and more importantly performance of my breadth first search and A\* search implementations for the Google AI Challenge.

The code is strange at times largely due to efforts that were made to squeeze maximum performance out of it. For example, to keep track of insert order and still have quick lookups, I used both a Deque and a Dict to store the list of open nodes in both of them while searching. This was vastly faster than any other option (including OrderedDict, actually).

While some of the code is particularly oriented for the AI Challenge, it should be able to be used for other applications with a little adapting.

The method calc_path is the A\* implementation and bfs_path is the breadth first search implementation.

Files
-----

* **searching.py** - This contains all logic about searching and ascii visualizing the results.
* **visualize_paths.py** - Code I used for testing that calls a search and prints the path and search data.
* **searching_tests.py** - Unit tests.
* **little_maze.txt and big_maze.txt** - Two sample maps used for testing.
* **brute_force.py** - Runs search for all start/finish possibilities to test performance.
