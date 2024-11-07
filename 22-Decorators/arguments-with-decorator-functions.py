def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute yuor function for you!")
        # print(args)
        # print(kwargs)
        fn(*args, **kwargs)
        print("It was my pleasure executing your function! Have a nice day!")

    return inner
@be_nice
def complex_business_logic(stakeholder, position):
    print(f"Sonthing complex {position} for {stakeholder}")

complex_business_logic( "Michael", position = "CEO")