film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese"
}

print(film_directors.get("Goodfellas"))
print(film_directors.get("Bad Boys", "Michael Boy"))
print(film_directors)

print(film_directors.get("Bad Boys"))

print(film_directors.setdefault("Bad Boys", "Michael Boy"))
print(film_directors)