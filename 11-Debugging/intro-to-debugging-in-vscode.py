Value = [1, 2, 3, 4, 5]

def sum_of_product_of_value_and_index(numbers):
    total = 0
    for index, number in enumerate(numbers):
        total += number * (index - 1)

    return total

print(sum_of_product_of_value_and_index(Value))

# 1 * (0 - 1) = -1
# 2 * (1 - 1) = 0
# 3 * (2 - 1) = 3
# 4 * (3 - 1) = 8
# 5 * (4 - 1) = 15
# -----------------------
#                25