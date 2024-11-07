def be_nice(fn):
    def inner():
        print("Nice to meet you! I'm honored to execute yuor function for you!")
        fn()
        print("It was my pleasure executing your function! Have a nice day!")

    return inner


@be_nice
def complex_business_logic():
    print("Something complex!")

@be_nice
def another_fancy_function():
    print("Go goo gaga")

# complex_business_logic()
another_fancy_function()
