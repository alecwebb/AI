# author: Alec Webb
import sys
import os.path

from csp import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def solve_sudoku():
    """This function solves the two given sodoku problems within csp.py and a third of my creation
    called medium, derived by deleting more elements from the given harder1 initial state"""
    
    game_easy = Sudoku( easy1 )
    solution = backtracking_search( game_easy, select_unassigned_variable=mrv, inference=forward_checking )
    print( "Solution to easy sodoku problem: " )
    game_easy.display( solution )
    print( "Number of assignments: ", game_easy.nassigns )
    
#     medium = '.1.36.8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
#     game_medium = Sudoku( medium )
#     solution = backtracking_search( game_medium, select_unassigned_variable=mrv, inference=forward_checking )
#     print( "Solution to medium sodoku problem: " )
#     game_medium.display( solution )
#     print( "Number of assignments: ", game_medium.nassigns )

    game_hard = Sudoku( harder1 )
    solution = backtracking_search( game_hard, select_unassigned_variable=mrv, inference=forward_checking )
    print( "Solution to hard sodoku problem: " )
    game_hard.display( solution )
    print( "Number of assignments: ", game_hard.nassigns )

def solve_n_queens(board_size):
    """This function takes a board size as an argument and solves the n-queens problem
    using the minimum conflicts algorithm"""
    
    nqueens = NQueensCSP( board_size )
    solution = min_conflicts( nqueens )
    solved = sorted( solution.values() ) == list( range( board_size ) )
    print( "N-Queens Solved: ", solved )
    print( "Value of N: ", board_size )
    print( "Solution : " , solution )
    print( "Number of assignments: ", nqueens.nassigns )
    
def solve_zebra_backtrack():
    """solve_zebra provided in csp.py is faulty or unresponsive, here I implemented the solution using 
    backtracking"""
    
    z = Zebra()
    ans = backtracking_search( z, select_unassigned_variable=mrv, inference=forward_checking )
    for h in range( 1, 6 ):
        print( 'House', h, end=' ' )
        for ( var, val ) in ans.items():
            if val == h:
                print( var, end=' ' )
        print()
    print( "Number of assignments: ", z.nassigns )

def solve_ships_backtrack():
    """A similar problem to the zebra problem is the ships problem, here I implemented the solution using 
    backtracking, for more information about ships goto: http://brainden.com/einsteins-riddles.htm , or 
    see the comments in the problem class found in csp.py"""
    
    s = Ships()
    ans = backtracking_search( s, select_unassigned_variable=mrv, inference=forward_checking )
    for r in range( 1, 6 ):
        for ( var, val ) in ans.items():
            if val == r:
                print( var, end=' ' )
        print()
    print( "Number of assignments: ", s.nassigns )
    

def init():
    """ Executes the functions necessary to produce the solutions for the additional game problems """
    
    print( "---------------" )
    print( "Solving Sudoku:" )
    print( "---------------" )
    solve_sudoku()
     
    print( "---------------" )
    print( "Solving N-Queens:" )
    print( "---------------" )
    solve_n_queens( 1001 )  # n > 1000
     
    print( "--------------" )
    print( "Solving Zebra:" )
    print( "--------------" )
    solve_zebra_backtrack()
    
    print( "--------------" )
    print( "Solving Ships:" )
    print( "--------------" )
    solve_ships_backtrack()


init()
