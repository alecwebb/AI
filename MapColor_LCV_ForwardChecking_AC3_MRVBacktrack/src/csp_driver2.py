# author: Alec Webb
import sys
import os.path

from csp import cutset_conditioning, australia, france, usa

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def init():
    """ Executes the functions necessary to produce the solutions for the cutset map problems"""
    
    print("Solving map coloring problem with tree structured csp with cutset conditioning")
    print("------------------------------------------------------------------------------")
    print("Australia")
    print("---------")
    cutset_conditioning(australia)
    print("France")
    print("------")
    cutset_conditioning(france)
    print("USA")
    print("---")
    cutset_conditioning(usa)
    

init()
