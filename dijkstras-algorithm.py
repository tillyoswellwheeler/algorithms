# -------------------------------------------------------------------------
# Grokking Algorithms  -- Dijkstra's Algorithm
# -------------------------------------------------------------------------

#---------------------
# Implementation

# Model the graph with hash tables (three hash tables required: graph, cost and parents)

###### GRAPH HASH TABLE MODEL #######

# ----------------------#
#       |   a   |   6   #
# start |---------------#
#       |   b   |   2   #
#-----------------------#
#   a   |  fin  |   1   #
# ----------------------#
#       |   a   |   3   #
#   b   |---------------#
#       |   fin |   5   #
#-----------------------#
#   fin |  ---          #
# ----------------------#

graph = {}

# graph has the keys: 'start', 'a', 'b', 'fin'
# Those keys have keys and values of their own, eg// start has 'a':6 and 'b':2
# We need to have a hash table within the main hash table
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {} #The finish node doesn't have any neighbours

# Checking the keys and values of the hash tables created in the graph model
# print(graph["start"].keys()) # returned as an array
# print(graph["start"].values()) # returned as an array

###### COST HASH TABLE MODEL #######

#---------------#
#   a   |   6   #
# --------------#
#   b   |   2   #
# --------------#
#   fin |  inf  #
# --------------#
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

###### PARENTS HASH TABLE MODEL #######

#-------------------#
#   a   |   start   #
#-------------------#
#   b   |   start   #
#-------------------#
#   fin |   ---     #
#-------------------#

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

###### LOGIC/CODE #######

processed = [] # an array to keep track of the processed nodes

node = find_lowest_cost_node(costs) #Find the lowest-cost node that you haven't processed yet
while node is not None: # If you have processed all the nodes this while loop stops/is done
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

def find_lowest_cost_node(costs): # takes in cost hash table
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = costlowest_cost_node = node
    return lowest_cost_node

#---------------------
# Exercise 1

#---------------------
# Exercise 2

#---------------------
# Exercise 3
