# -------------------------------------------------------------------------
# Grokking Algorithms  -- Graphs, Breadth First Search and Topological Sort
# -------------------------------------------------------------------------

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []

# enqueue almost always same as push
# dequeue almost always same as pop

#---------------------
# Version 1 - Without checked functionality removing duplication in queue

# search_queue = deque() # creates a new queue
# search_queue += graph["you"] # adds all of you's node neighbours to the search queue

# def checks_sellers(search_queue):
#     while search_queue: # while the queue is not empty
#         person = search_queue.popleft() #grab the first person off the queue
#         if person_is_seller(person): # checks whether the person sells mango - calls function
#             print(person + " is a mango seller!") # yes they are a mango seller
#             return True
#         else:
#             search_queue += graph[person] # no they are not, adds their node's neighbours to the queue
#     return False # if you have reached here no-one is a mango seller

# def person_is_seller(name):
#     return name[-1] == 'm'

# checks_sellers(search_queue)

#---------------------
# Version 2 - Added in logic to handle duplicated noteds - Checked

def search(name):
    search_queue = deque() # creates a new queue
    search_queue += graph["you"] # adds all of you's node neighbours to the search queue
    searched = []
    while search_queue: # while the queue is not empty
        person = search_queue.popleft() #grab the first person off the queue
        if not person in searched: #only search person if they are not in searched[]
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person) # mark this person as search eg// add to searched[]
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search("you")


