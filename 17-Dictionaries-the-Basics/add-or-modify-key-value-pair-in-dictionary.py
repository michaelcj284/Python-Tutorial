words = ["danger", "beware", "danger", "beware", "beware"]

def count_words(words):
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    return counts

print(count_words(words))