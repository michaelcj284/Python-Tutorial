class Book():
    def __init__(self, title, author, price = 14.99):
        self.title = title
        self.author = author
        self.price = price

animal_farm = Book("Animal Farm", "George Orwell", 19.99)
# gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")

print(animal_farm.title)
print(animal_farm.author)
print(animal_farm.price)
# print(gatsby.price)

atlas = Book(title = "Animal Farm", author = "George Orwell", price = 19.99)
# jude = Book(author = "Thomas Hardy", price = 24.99, title = "Jude the Obscure")

print(atlas.title)
print(atlas.author)
print(atlas.price)