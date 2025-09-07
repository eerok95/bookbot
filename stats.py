def count_words(book):
    word_list = book.split()
    return len(word_list)

def count_chars(book):
    char_counts = {}
    for char in book:
        if char.lower() in char_counts:
            char_counts[char.lower()] += 1
        elif char.lower() not in char_counts:
            char_counts[char.lower()] = 1

    return char_counts

def sort_on(list):
    return list["num"]

def sort_dictionary(dictionary):
    dictionary_list = []
    for key in dictionary:
        dictionary_list.append({"char": key, "num":dictionary[key]})

    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list