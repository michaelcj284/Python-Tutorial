#years = [1991, 1995, 2000, 2007]
#years.pop(1)
#print(years)

release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

years = release_dates.pop("Rust", 2000)
print(years)

del release_dates["Rust"]
print(release_dates)