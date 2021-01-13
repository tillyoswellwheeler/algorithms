# -------------------------------------------------------------------------
# Grokking Algorithms  -- Dijkstra's Algorithm
# -------------------------------------------------------------------------

#---------------------
# Implementation

# Model the graph with hash tables (three hash tables required: graph, cost and parents)

# ###### GRAPH HASH TABLE MODEL #######

# # ----------------------#
# #       |   a   |   6   #
# # start |---------------#
# #       |   b   |   2   #
# #-----------------------#
# #   a   |  fin  |   1   #
# # ----------------------#
# #       |   a   |   3   #
# #   b   |---------------#
# #       |   fin |   5   #
# #-----------------------#
# #   fin |  ---          #
# # ----------------------#

# graph = {}

# # graph has the keys: 'start', 'a', 'b', 'fin'
# # Those keys have keys and values of their own, eg// start has 'a':6 and 'b':2
# # We need to have a hash table within the main hash table
# graph["start"] = {}
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2

# graph["a"] = {}
# graph["a"]["fin"] = 1

# graph["b"] = {}
# graph["b"]["a"] = 3
# graph["b"]["fin"] = 5

# graph["fin"] = {} #The finish node doesn't have any neighbours

# # Checking the keys and values of the hash tables created in the graph model
# # print(graph["start"].keys()) # returned as an array
# # print(graph["start"].values()) # returned as an array

# ###### COST HASH TABLE MODEL #######

# #---------------#
# #   a   |   6   #
# # --------------#
# #   b   |   2   #
# # --------------#
# #   fin |  inf  #
# # --------------#
# infinity = float("inf")
# costs = {}
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity

# ###### PARENTS HASH TABLE MODEL #######

# #-------------------#
# #   a   |   start   #
# #-------------------#
# #   b   |   start   #
# #-------------------#
# #   fin |   ---     #
# #-------------------#

# parents = {}
# parents["a"] = "start"
# parents["b"] = "start"
# parents["fin"] = None

# ###### LOGIC/CODE #######

# processed = [] # an array to keep track of the processed nodes

# def find_lowest_cost_node(costs): # takes in cost hash table
#     lowest_cost = float("inf")
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node

# node = find_lowest_cost_node(costs) #Find the lowest-cost node that you haven't processed yet
# while node is not None: # If you have processed all the nodes this while loop stops/is done
#     cost = costs[node]
#     neighbours = graph[node]
#     for n in neighbours.keys():
#         new_cost = cost + neighbours[n]
#         if costs[n] > new_cost:
#             costs[n] = new_cost
#             parents[n] = node
#     processed.append(node)
#     node = find_lowest_cost_node(costs)

# print(costs)
# print(parents)
# #---------------------
# # Exercise 1

# ###### GRAPH HASH TABLE MODEL #######

# # ----------------------#
# #       |   a   |   2   #
# # start |---------------#
# #       |   b   |   5   #
# #-----------------------#
# #       |   b   |   8   #
# #   a   |---------------#
# #       |   d   |   7   #
# #-----------------------#
# #       |   c   |   4   #
# #   b   |---------------#
# #       |   d   |   2   #
# #-----------------------#
# #       |   d   |   6   #
# #   c   |---------------#
# #       |   fin |   3   #
# #-----------------------#
# #   d   |  fin  |   1   #
# #-----------------------#
# #   fin |  ---          #
# # ----------------------#

# graph = {}

# graph["start"] = {}
# graph["start"]["a"] = 2 #The neighbours of start
# graph["start"]["b"] = 5 #The neighbours of start

# graph["a"] = {}
# graph["a"]["b"] = 8 #The neighbours of a
# graph["a"]["d"] = 7 #The neighbours of a

# graph["b"] = {}
# graph["b"]["c"] = 4 #The neighbours of b
# graph["b"]["d"] = 2 #The neighbours of b

# graph["c"] = {}
# graph["c"]["d"] = 6 #The neighbours of c
# graph["c"]["fin"] = 3 #The neighbours of c

# graph["d"] = {}
# graph["d"]["fin"] = 1 #The neighbours of d

# graph["fin"] = {} # fin has no neighbours, so no hash tables within hash table to start

# ###### COST HASH TABLE MODEL #######

# #---------------#
# #   a   |   2   #
# # --------------#
# #   b   |   5   #
# # --------------#
# #   c   |  inf  #
# # --------------#
# #   d   |  inf  #
# # --------------#
# #   fin |  inf  #
# # --------------#

# infinity = float("inf")

# costs = {}

# costs["a"] = 2
# costs["b"] = 5
# costs["c"] = infinity
# costs["d"] = infinity
# costs["fin"] = infinity

# ###### PARENTS HASH TABLE MODEL #######

# #-------------------#
# #   a   |   start   #
# #-------------------#
# #   b   |   start   #
# #-------------------#
# #   c   |   ---     #
# #-------------------#
# #   d   |   ---     #
# #-------------------#
# #   fin |   ---     #
# #-------------------#

# parents = {}

# parents["a"] = "start"
# parents["b"] = "start"
# parents["c"] = None
# parents["d"] = None
# parents["fin"] = None

# processed = []

# def find_lowest_cost_node(costs):
#     lowest_cost = float("inf")
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node

# node = find_lowest_cost_node(costs)
# while node is not None:
#     cost = costs[node]
#     neighbours = graph[node]
#     for n in neighbours.keys():
#         new_cost = cost + neighbours[n]
#         if costs[n] > new_cost:
#             costs[n] = new_cost
#             parents[n] = node
#     processed.append(node)
#     node = find_lowest_cost_node(costs)

# print(costs)
# print(parents)
# cheapest_path_value = costs["fin"]
# print(f"Cheapest path calculated using Dijkstra's Algorithm is: {cheapest_path_value}")

#---------------------
# Exercise 2

###### GRAPH HASH TABLE MODEL #######

# ----------------------#
# start |   a   |   10  #
#-----------------------#
#   a   |  b    |   20  #
#-----------------------#
#       |   fin |   30  #
#   b   |---------------#
#       |   c   |   1   #
#-----------------------#
#   c   |  a    |   1   #
#-----------------------#
#   fin |  ---          #
# ----------------------#

graph = {}

graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["b"] = 20

graph["b"] = {}
graph["b"]["fin"] = 30
graph["b"]["c"] = 1

graph["c"] = {}
graph["c"]["a"] = 1

graph["fin"] = {}

###### COST HASH TABLE MODEL #######

#---------------#
#   a   |   10  #
# --------------#
#   b   |  inf  #
# --------------#
#   c   |  inf  #
# --------------#
#   fin |  inf  #
# --------------#

infinity = float("inf")
costs = {}

costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["fin"] = infinity

###### PARENTS HASH TABLE MODEL #######

#-------------------#
#   a   |   start   #
#-------------------#
#   b   |   start   #
#-------------------#
#   c   |   ---     #
#-------------------#
#   d   |   ---     #
#-------------------#
#   fin |   ---     #
#-------------------#

parents = {}

parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)
cheapest_path_value = costs["fin"]
print(f"Cheapest path calculated using Dijkstra's Algorithm is: {cheapest_path_value}")

#---------------------
# Exercise 3

# Can't solve with Dijkstra's Algorithm as it is a negative weighted graph
