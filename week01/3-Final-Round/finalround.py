def nan_expand(times):
    if times == 0:
        return ""
    result = ""

    for i in range(times):
        result += "Not a "

    return result + "Nan"


def iterations_of_nan_expand2(expanded):
    if nan_expand(expanded.count("Not a")) == expanded:
        return expanded.count("Not a")

    return False


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


NUMBERS = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " ",
}


def numbers_to_message(num):
    res = ""
    numbs_groups = group(num)
    up_c = False

    for grp in numbs_groups:
        if grp[0] == 1:
            up_c = True
            continue
        if grp[0] == -1:
            continue

        key_letters = NUMBERS[grp[0]]
        times_pressed = len(grp)
        selected_letter_index = times_pressed % len(key_letters) - 1
        letter = key_letters[selected_letter_index]

        if up_c:
            res += letter.upper()
            up_c = False

        else:
            res += letter

    return res
