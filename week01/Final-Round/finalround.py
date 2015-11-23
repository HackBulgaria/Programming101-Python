def iterations_of_nan_expand(st):
    if st == "":
        return 0

    if st.count("Not a Nan") == 0:
        return False

    else:
        return st.count("Not a")


def take_same(items):
    first = items[0]
    n = len(items)
    index = 1
    result = [first]

    while index < n and first == items[index]:
        result.append(items[index])
        index += 1

    return result


def group(items):
    result = []

    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)

        items = items[len(current_group):]

    return result


def gas_stations(distance, tank_size, stations):
    result = [0]
    stations.append(distance)

    for i in range(0, len(stations)-1):
        diff = stations[i+1] - stations[i]
        size = tank_size - (stations[i] - result[-1])

        if size < diff:
            result.append(stations[i])
            size = tank_size

    return result[1:]