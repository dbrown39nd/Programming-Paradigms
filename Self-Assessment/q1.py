#!/usr/bin/env python3
from pprint import pprint

def bfs_traversal(graph, initial_node):
    
    queue = []
    visited = []
    
    queue.append(initial_node)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
        for val in graph[node]:
            if val not in visited:
                queue.append(val)    
    print(visited)
        
        
def main():
    graph = {"+": ["*",3], "*":[2,7], 2:[],7:[],3:[]}
    initial_node = "+" 
    bfs_traversal(graph, initial_node)
    
    graph = {0: [1,3], 1:[2,3], 2:[3,1], 3:[0,1]}
    initial_node = 0
    bfs_traversal(graph, initial_node)
    

    
if __name__ == '__main__':
    main()