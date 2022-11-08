"""
Short Exercises #6
"""

from tree import Tree


def harmonic_sequence(N):
    """
    Sum the first N values of the harmonic sequence: 
        1 + 1/2 + 1/3 + ... + 1/N

    Inputs:
        N (int): the number of values to sum

    Returns (float): The sum 1 + 1/2 + 1/3 + ... + 1/N
    """
    
    ### YOUR CODE HERE
    pass


def recursive_len(lst):
    """
    Compute the length of a list recursively

    Input:
       lst (list): a list

    Returns (int): The length of the list
    """
    
    ### YOUR CODE HERE
    pass


def min_depth_leaf(tree):
    """
    Compute the minimum depth of a leaf in the tree (the length of shortest
        path from the root to a leaf)

    Input:
        tree: a Tree instance
    
    Returns (int): The minimum depth of a leaf in the tree
    """

    ### YOUR CODE HERE
    pass


def repeated_value(tree):
    """
    Determine whether there is a node in the input tree that has 
        an ancestor with the same value

    Input:
        tree (Tree): a Tree instance
    
    Returns (boolean): True if there is a node in the tree that has 
        an ancestor with the same value, False otherwise
    """
    
    ### YOUR CODE HERE
    pass


def prune_tree(tree, keys_to_prune):
    """
    Create a new tree that is identical to the original tree, except
        that any node whose key is in keys_to_prune is removed, along with its
        descendants

    Inputs:
        tree (Tree): a Tree instance
        keys_to_prune (set): set of keys
    
    Returns (Tree): The pruned tree
    """
    
    ### YOUR CODE HERE
    pass
