"""
An example of greedy algorithm.

The task is to cover as much regions as possible with as little stations as possible.

To find an optimal solution would be of O(2**n) complexity.
Instead we could apply a greedy algorithm that will give us solution that is good enough taking O(n**2) time.

1. Pick the station that covers the most states that haven’t been covered yet.
It's OK if the station covers some states that have been covered already.
2. Repeat until all the states are covered.
"""

# Test data.
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
stations = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}


def greedy_approximation(states_to_find, available_stations):
    final_stations = set()

    while states_to_find:
        best_station = None
        states_covered = set()

        for station, station_states in available_stations.items():
            covered = states_to_find & station_states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        final_stations.add(best_station)
        states_to_find = states_to_find - states_covered

    return final_stations


print(greedy_approximation(states_needed, stations))  # {'kfive', 'ktwo', 'kone', 'kthree'}
