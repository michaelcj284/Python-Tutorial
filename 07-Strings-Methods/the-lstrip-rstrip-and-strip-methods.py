empty_space = "       content       "


print(empty_space.strip())
print(len(empty_space.strip()))

website = "www.python.org"
print(website.lstrip("w"))
print(website.rstrip("org"))
print(website.strip("worg."))