# author: Alec Webb
import sys
import os.path

from csp import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def lcv_backtracking(country):
    """Function which makes a local copy of the global CSV Map, and prints the results of a backtracking
    call using the LCV Heuristic"""
    
    local_map = copy.deepcopy(country)
    map_with_lcv_backtracking = backtracking_search( local_map, order_domain_values=lcv )
    local_map.display( map_with_lcv_backtracking )                  #display result of backtracking
    print( "Number of Assignments", local_map.numAssignments() )    #display # of assignments
    

def mrv_backtracking(country):
    """Function which makes a local copy of the global CSV Map, and prints the results of a backtracking
    call using the MRV Heuristic"""
    
    local_map = copy.deepcopy(country)
    map_with_mrv_backtracking = backtracking_search( local_map, select_unassigned_variable=mrv )
    local_map.display( map_with_mrv_backtracking )                  #display result of backtracking
    print( "Number of Assignments", local_map.numAssignments() )    #display # of assignments
    
def run_mrv_backtracking():
    print( "---------------------------" )
    print( "Backtracking using MRV for:" )
    print( "---------------------------" )
    print( "[Australia]" )
    print( "-----------" )
    mrv_backtracking( australia )
    print( "--------" )
    print( "[France]" )
    print( "--------" )
    mrv_backtracking( france )
    print( "-----" )
    print( "[USA]" )
    print( "-----" )
    mrv_backtracking( usa )
    
def run_lcv_backtracking():
    print( "---------------------------" )
    print( "Backtracking using LCV for:" )
    print( "---------------------------" )
    print( "[Australia]" )
    print( "-----------" )
    lcv_backtracking( australia )
    print( "--------" )
    print( "[France]" )
    print( "--------" )
    lcv_backtracking( france )
    print( "-----" )
    print( "[USA]" )
    print( "-----" )
    lcv_backtracking( usa )

def ac3_constraint_propagation(country):
    """This function takes a country and runs backtracking using ac3 constraint propagation, the 
    framework refers to this as a mac inference"""
    
    local_map = copy.deepcopy(country)
    map_with_ac3 = backtracking_search( local_map, inference=mac )
    local_map.display( map_with_ac3 )                               #display result of backtracking
    print( "Number of Assignments", local_map.numAssignments() )    #display # of assignments
    
def run_ac3():
    print( "---------------------------" )
    print( "Constraint propagation using AC3 for:" )
    print( "---------------------------" )
    print( "[Australia]" )
    print( "-----------" )
    ac3_constraint_propagation( australia )
    print( "--------" )
    print( "[France]" )
    print( "--------" )
    ac3_constraint_propagation( france )
    print( "-----" )
    print( "[USA]" )
    print( "-----" )
    ac3_constraint_propagation( usa )
    
def forward_checking_with_arc_consistency(country):
    """This function takes a country and runs a backtracking search with the forward checking inference"""
    
    local_map = copy.deepcopy(country)
    map_with_forward_checking = backtracking_search( local_map, inference=forward_checking )
    local_map.display( map_with_forward_checking )                  #display result of backtracking
    print( "Number of Assignments", local_map.numAssignments() )    #display # of assignments
    

def run_forward_checking():
    print( "---------------------------" )
    print( "Forward Checking with Arc Consistency for:" )
    print( "---------------------------" )
    print( "[Australia]" )
    print( "-----------" )
    forward_checking_with_arc_consistency( australia )
    print( "--------" )
    print( "[France]" )
    print( "--------" )
    forward_checking_with_arc_consistency( france )
    print( "-----" )
    print( "[USA]" )
    print( "-----" )
    forward_checking_with_arc_consistency( usa )
    
def init():
    """ Executes the functions necessary to produce the solutions for the map coloring problems """
    
    print( "Solving Map Problems:" )
    run_lcv_backtracking()
    run_mrv_backtracking()
    run_ac3()
    run_forward_checking()


init()
