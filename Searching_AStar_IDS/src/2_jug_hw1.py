# author: Alec Webb
import random
import math
import sys
import os.path

from random import randint
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from search import iterative_deepening_search, TwoJug

def solveIterativeDeepeningSearch(puzzle):
    """Solves the two jug problem using iterative_deepening_search"""
    return iterative_deepening_search(puzzle).solution()

def printSolution(solution, state, puzzle, goal):
    """Prints the solution found by the previous functions IDS search for a particular goal state"""
    
    print("Solution for the goal:", goal)
    print(solution)
    for move in solution:
        state = puzzle.result(state, move) 
        print(state)
        
def solve_given_jug_sizes(dimensions):
    """Given a pair of jug dimensions n and m, uses IDS to solve for 1...max(n,m) goal states"""
    (n,m) = dimensions
    init = (0,0)
    
    print("-----------------------------------------------------------------------------------------------------")
    print("Find Solutions for the Goals from 1...max(n,m) in Either Jug using IDS for capacities: (", n,",",m,")")
    print("-----------------------------------------------------------------------------------------------------")
    
    for goal in range(1, max(n,m) + 1):
        state = [0,0]
        puzzle = TwoJug(init, goal)
        puzzle.set_capacities((n,m))
        solution = solveIterativeDeepeningSearch(puzzle)
        printSolution(solution, state, puzzle, goal)
        solution = None
        
def generate_coprime_pairs():
    """Returns a list of pairs such that n and m are coprime, 
    determined by whether n and m have a gcd equal to one and
    n and m are not equal and in the range 3 <= n,m <= 15"""
    
    coprimePairList = []
    while coprimePairList.__len__() < 10:
        n = randint(3,15)
        m = randint(3,15)
        if math.gcd(n,m) == 1:
            pair = (n,m)     
            if pair not in coprimePairList:
                coprimePairList.append(pair)
    
    print("List of random coprime jug capacities to be solved:" , coprimePairList)
    return coprimePairList

def solve_steps():
    """ Executes the functions necessary to produce the solutions for the two jug problem """

    coprimePairList = generate_coprime_pairs()
    print("List of random coprime jug capacities to be solved:" , generate_coprime_pairs)
      
    for dimensions in coprimePairList:
        solve_given_jug_sizes(dimensions)


solve_steps()
