states_to_cover = {
    "mt", "wa", "or", "id", "nv", "ut", "ca", "az"
}
radio_stations_by_states = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"}
}
picked_stations = set()

while states_to_cover:
    best_station = None
    covered_states = set()
    
    for station, states in radio_stations_by_states.items():
        covered = states_to_cover & states
        if len(covered) > len(covered_states):
            best_station = station
            covered_states = covered

    states_to_cover -= covered_states
    picked_stations.add(best_station)

print(picked_stations)
