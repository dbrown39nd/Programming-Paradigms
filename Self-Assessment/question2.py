#!/usr/bin/env python3
from pprint import pprint

def dfs_traversal(graph, initial_node):
    
    queue = []
    visited = []
    
    queue.append(initial_node)
    while queue:
        node = queue.pop(0)
        if node not in visited: #could be optimized
            visited.append(node)
        for index, val in enumerate(graph[node]): #Insert at the front of the queue, not the back. 
            if val not in visited:
                queue.insert(index, val)    
    return visited 
        
        
def main():
    graph = {"+": ["*",3], "*":[2,7], 2:[],7:[],3:[]}
    initial_node = "+"
    traversal = dfs_traversal(graph, initial_node)
    print(traversal)
    graph = {0: [1,3], 1:[2,3], 2:[3,1], 3:[0,1]}
    initial_node = 0
    traversal = dfs_traversal(graph, initial_node)
    print(traversal)

    
    

    
if __name__ == '__main__':
    main()