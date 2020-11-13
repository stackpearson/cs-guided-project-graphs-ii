"""
In a town, there are `N` people labelled from `1` to `N`.  There is a rumor
that one of these people is secretly the town judge.
​
If the town judge exists, then:
​
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
​
You are given `trust`, an array of pairs `trust[i] = [a, b]` representing that
the person labelled a trusts the person labelled `b`.
​
If the town judge exists and can be identified, return the label of the town
judge.  Otherwise, return `-1`.
​
Example 1:
​
```plaintext
Input: N = 2, trust = [[1,2]]
Output: 2
```
​
Example 2:
​
```plaintext
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
```
​
Example 3:
​
```plaintext
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```
​
Example 4:
​
```plaintext
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
```
​
Example 5:
​
```plaintext
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
```
​
Constraints:
​
- `1 <= N <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- `trust[i]` are all different
- `trust[i][0] != trust[i][1]`
- `1 <= trust[i][0], trust[i][1] <= N`
"""
def check_every_other_other_node(graph, candidate):
    for i in range(1, len(graph)):
        if i != candidate and candidate not in graph[i]:
            return False 
​
    return True
​
print(check_every_other_other_node([[], [3, 4], [3, 4], [], [3]], 3))
​
def find_nodes_with_no_neighbors(graph):
    candidates = []
​
    for i in range(1, len(graph)):
        if len(graph[i]) == 0:
            candidates.append(i)
​
    return candidates
​
print(find_nodes_with_no_neighbors([[], [3, 4], [3, 4], [], [3]]))
​
def build_graph_from_trust(N, trust):
    graph = [[] for _ in range(N + 1)] 
​
    for a, b in trust:
        graph[a].append(b)
​
    return graph 
​
print(build_graph_from_trust(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
​
​
def find_judge(N, trust):
    """
    Inputs:
    N -> int
    trust -> List[List[int]]
​
    Output:
    int
    """ 
    # 0. Construct our graph from the `trust` list 
    graph = build_graph_from_trust(N, trust)
    # 1. Find the one node that has no neighbors 
    candidates = find_nodes_with_no_neighbors(graph)
    # note: if there is more than one, return -1 
    if len(candidates) != 1:
        return -1 
    # 2. Check that every other node has this node as a neighbor 
    if check_every_other_other_node(graph, candidates[0]):
        return candidates[0] 
    # if these both aren't satisfied, return -1 
    return -1 
​
print(find_judge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))