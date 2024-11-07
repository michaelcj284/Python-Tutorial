languages = ["Python", "JavaScript", "Ruby"]

lengths = {language: len(language) for language in languages if "t" in language}

print(lengths)

