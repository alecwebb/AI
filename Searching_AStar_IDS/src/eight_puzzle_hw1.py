# author: Alec Webb
import random

import sys
import numpy as np
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from search import astar_search, iterative_deepening_search, EightPuzzle

state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
puzzle = EightPuzzle(tuple(state))
solution = None

"""Modified the GUI version of Eight Puzzle provided, stripped the GUI and retained the backend"""

def scramble():
    """ Scrambles the puzzle starting from the goal state """

    global state
    global puzzle
    possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    scramble = []
    for _ in range(60):
        scramble.append(random.choice(possible_actions))

    for move in scramble:
        if move in puzzle.actions(state):
            state = list(puzzle.result(state, move))
            puzzle = EightPuzzle(tuple(state))

def solveAstar():
    """ Solves the puzzle using astar_search with the number of wrong tiles heuristic"""
    return astar_search(puzzle, puzzle.h).solution()

def solveAstarManhattan():
    """ Solves the puzzle using astar_search with the Manhattan distance heuristic"""
    return astar_search(puzzle, puzzle.hManhattan).solution()
    
def solveIterativeDeepeningSearch():
    """Solves the puzzle using iterative_deepening_search"""
    return iterative_deepening_search(puzzle).solution()

def printSolution(solution, state):
    """Prints the sequence of moves for the final solution and the number of nodes expanded,
    can also print the sequence of states as a 3x3 matrix by uncommenting commented code"""
    
    print("Solution:" ,solution)
    print("Nodes Expanded: ", puzzle.numNodes())
    puzzle.clearNodes()
    solution = None
    
#     for move in solution:
#         state = puzzle.result(state, move) 
#         #Below implements the matrix printout       
#         shape = (3,3)
#         grid = np.array(state).flatten()
#         print(grid.reshape(shape))
#         print("---------")

def solve_steps():
    """ Solves the puzzle step by step """

    global puzzle
    global solution
    global state
    
    print("A* with Manhattan Heuristic")
    printSolution(solveAstarManhattan(), state)
    
    print("---------------------------")
    print("A* with # of misplaced tiles Heuristic")
    printSolution(solveAstar(), state)

    print("--------------------------")
    print("Iterative Deepening Search")
    printSolution(solveIterativeDeepeningSearch(), state)

def init():
    """ Calls necessary functions """
    global state
    global solution
    state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    scramble()
    print("Eight Puzzle Run with starting state: ", state)
    print("-------------------------------------")
    solve_steps()

init()