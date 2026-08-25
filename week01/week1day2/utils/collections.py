from os import remove


def frequencies(items):
    # counts the frequency of each item in a list
    # returns a dictionary with the items as keys and their frequencies as values.
    frequency = {}
    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(frequencies(items))


def dedupe(items):
    # remove duplicates from a list while preserving order.
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


items = ["apple", "banana", "cherry", "apple", "banana", "date"]
print(dedupe(items))


def group_by(items, key: str):
    result = {}
    for item in items:
        value = item[key]
        if value not in result:
            result[value] = []
        result[value].append(item)
    return result


items = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
]
print(group_by(items, "age"))
