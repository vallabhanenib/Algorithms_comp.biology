# -*- coding: utf-8 -*-
"""Recursion Algorithm to count the no.of nodes.ipynb

Automatically generated by Colaboratory.


Function to get Node count
"""

def countNodes(tree):
    root,first,second = tree    
    if first == second == ():
        return 1     
    else:
        return 1 + countNodes(first) + countNodes(second)

def height(tree):
    root,first,second = tree    
    if first == second == ():
        return 0     
    else:
        return 1 + max(height(first), height(second))

def leafList(tree):
    root,first,second = tree    
    if first == second == ():
        return [ root ]       
    else:
        return leafList(first) + leafList(second)

"""Question 1:"""

tree1 = ('A',
     ('B',
          ('C',(),()),
          ('D',(),())
     ),
     ('E',(),())
)

same_tree = ('A', ('B', ('C',(),()), ('D',(),()) ), ('E',(),()) )

print("Number of nodes in tree 1 is: ",countNodes(tree1))
print("Number of nodes in same_tree: ",countNodes(same_tree))
print("Height of the tree 1 is : ", height(tree1))
print("leaf Nodes in the tree 1 are: ", leafList(tree1) )


"""Question 2:"""

tree5 = ('A',('B',(),()),('C',('D',(),()),('E',('F',(),()),('G',(),()))))

print("Tuple representation for Question 5: ", tree5)
print("Number of nodes in tree 5 is: ",countNodes(tree5))
print("Height of the tree 5 is : ", height(tree5))
print("Leaf Nodes in the tree 5 are: ", leafList(tree5) )

