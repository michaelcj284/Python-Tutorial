# with open("cupcakes.txt", "r") as cupcakes_file:
#     print("This file has been opened!")
#     content = cupcakes_file.read()
#     print(content)

# print("This file has been closed! We are outsite the context block")


filename = input("What file would you like to open?" )
with open(filename, "r") as file_object:
    print(file_object.read())