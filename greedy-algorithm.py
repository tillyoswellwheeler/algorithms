# -------------------------------------------------------------------------
# Grokking Algorithms  -- Greedy Algorithm
# -------------------------------------------------------------------------

# Problem (Set-covering problem > NP-Complete Problem):
# -- Calculating the minimum number of radio stations you need to cover all 50 states
# -- It costs to play on a radio station, so you want to maximize coverage of states, but minimize cost
# -- An optimization problem? What are the optimal individual radio stations to play on, to get a globally optimal set of stations

# If you had lots of computation or not many stations you would calculate the powerset for the radio stations set.
# INSTEAD: We use the Greedy Algorithm (approxiamation algorithm)
# 1. Pick the station that covers the most states that haven't been covered yet.
#  It's okay if the station covers some states that have been covered already.
# 2. Repeat until all the states have been covered

#---------------------
# Implementation

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] =set(["ca", "az"])

# the stations are the keys and the states are the values

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
