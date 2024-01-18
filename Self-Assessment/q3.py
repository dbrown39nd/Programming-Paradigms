#!/usr/bin/env python3


def tree_to_text(tree, root_node):
    parents = []
    queue = [root_node]
    text = ""
    while queue: #While there are still nodes to be examined
        node = queue.pop(0) #pop first node
        
        if len(tree[node]): #has kids
            left_child  = tree[node][0]
            right_child = tree[node][1]
            parents.insert(0, node)
            queue.insert(0,left_child)
            queue.insert(1, right_child)
        else:
            text += node[node.index('_')+1:]
            if parents:
                node = parents.pop(0)
                text += node[node.index('_')+1:]
    return text
    
        #check if leaf

def main():
    tree =  {"n1_+": ["n2_*","n3_3"], "n2_*":["n4_2","n5_7"], "n4_2":[],"n5_7":[],"n3_3":[]}
    root_node = "n1_+" 
    output = tree_to_text(tree, root_node)
    print(output)
    tree ={'n1_+': ['n2_3', 'n3_*'], 'n3_*': ['n4_/', "n5_2"], 'n4_/': ["n6_10", "n7_5"], "n6_10": [], "n7_5": [], "n5_2": [], 'n2_3': []}
    root_node = "n1_+" 
    output = tree_to_text(tree, root_node)
    print(output)
    
    
    
if __name__ == '__main__':
    main()