def cleanup(strings):
	clean_strings = []

	for string in strings:
		if string.isspace() or len(string) == 0:
			countinue
		
		clean_strings.append(string)
	
	return " ".join(clean_strings)

print(cleanup(["cat", "er", "pillar"]))