def csFindAllPathsFromAToB(graph):
    all_paths = []
    # visited = set()
    
    recurse(graph, all_paths, 0, [])
    
    return all_paths
    
    
def recurse(graph, all_paths, current_node, current_path):
    # add this path to our list of paths 
    current_path.append(current_node)
    
    # base case 1:
    # when we've gone over every graph node in our 
    # adjacency list 
    # how do we know when we've gone through ever node in our list?
    if current_node >= len(graph) - 1: 
        # add this current path to all_paths
        all_paths.append(current_path[:])
        current_path.pop()
        return 
    
    # base case 2:
    # if a node has no neighbors, then we end the 
    # current path we're building up 
    if len(graph[current_node]) == 0:
        # we're done with this route 
        return
    
    # how do we get closer to a base case? 
    # also need to keep track of which nodes we've visited 
    # visited.add(current_node)
    
    # iterate through all of our graph nodes in our adj list
    # recursively build up all branching paths by traversing
    # to each node's neighbors 
    for neighbor in graph[current_node]:
        recurse(graph, all_paths, neighbor, current_path)
        
    # pop off the most recently added node to the current path 
    current_path.pop()
