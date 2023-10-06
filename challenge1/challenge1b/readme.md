### Algorithm Explanation

I made assumptions as to the abstraction of the directed graph and it's nodes. I assumed that nodes keep track of their inbounds and outbounds. I believe this would improve the access time for computations like identifying nodes with most connections. How this is done can be seen in the `read_nodes_into_graphs` function

Using the big O notation, the time complexity for the identify router function written is O(n) —— linear time complexity, where n is the number of nodes.

The function is of linear time complexity since only one iteration of the nodes of the graph is required for computation. Hence the relationship between the number of nodes and the time for computation is linear.
