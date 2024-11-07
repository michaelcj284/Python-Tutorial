def super_sum(strings):
    total = 0
    for string in strings:
        if "s" in string:
            index = string.index("s")
            total += index
    return total

print(super_sum(["mustache"]))