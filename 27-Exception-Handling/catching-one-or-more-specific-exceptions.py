def divide_5_by_number(n):
    try:
        calculation = 5 / n
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except TypeError as e:
        return f"No dividing by invalid objects! {e}"

    return calculation

print(divide_5_by_number(10))
print(divide_5_by_number(0))
print(divide_5_by_number("nonsense"))

print("\n")


def divide_5_by_number(n):
    try:
        calculation = 5 / n
    except (ZeroDivisionError, TypeError) as e:
        return f"Somethin went wrong, The error was {e}"

    return calculation

print(divide_5_by_number(10))
print(divide_5_by_number(0))
p