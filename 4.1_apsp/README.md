1.
Question 1

In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem.  Here are data files describing three graphs: 
g1.txt

g2.txt

g3.txt

The first line indicates the number of vertices and edges, respectively.  Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) and its length (the third number).  NOTE: some of the edge lengths are negative.  NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path".  Precisely, you must first identify which, if any, of the three graphs have no negative cycles.  For each such graph, you should compute all-pairs shortest paths and remember the smallest one (i.e., compute min⁡u,v∈Vd(u,v)\min_{u,v \in V} d(u,v)minu,v∈V​d(u,v), where d(u,v)d(u,v)d(u,v) denotes the shortest-path distance from uuu to vvv). 

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below.  If exactly one graph has no negative-cost cycles, then enter the length of its shortest shortest path in the box below.  If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their shortest shortest paths in the box below.

OPTIONAL: You can use whatever algorithm you like to solve this question.  If you have extra time, try comparing the performance of different all-pairs shortest-path algorithms!

OPTIONAL: Here is a bigger data set to play with.
large.txt

For fun, try computing the shortest shortest path of the graph in the file above.