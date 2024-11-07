def fizzbuzz(final_number):
    current_number = 1
    while current_number <= final_number:
        if current_number % 15 == 0:
            print("FizzBuzz")
        elif current_number % 3 == 0:
            print ("Buzz")
        elif current_number % 5 == 0:
            print("Fizz")
        else:
            print(current_number)
        current_number += 1
print(fizzbuzz(30))


