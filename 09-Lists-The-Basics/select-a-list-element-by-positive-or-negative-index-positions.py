def first_and_last(element):
    return element[0] + element[-1]

print(first_and_last(["a", "b", "c"]))



def split_in_two(values, number):
    if number % 2 == 0:
        return values[2:]
    else:
        return values[:2]