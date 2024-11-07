def divide_five_by_number(n):
    try:
        return 5 / n
    except(ZeroDivisionError, TypeError) as e:
        return f"Hey! na error be this oo {e}"

print(divide_five_by_number("nir"))

