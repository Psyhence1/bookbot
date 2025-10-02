def get_word_count(book_text):
    book_words = book_text.split()
    return len(book_words)


def get_char_dict(book_text):
    char_dict = {}
    for char in book_text:
        low_char = char.lower()
        if low_char in char_dict:
            char_dict[low_char] += 1
        else:
            char_dict[low_char] = 1
    return char_dict


def sort_on(cd):
    return cd["num"]


def sorted_char_dict(num_char_dict):
    char_list = []
    for char in num_char_dict:
        char_list.append({"char": char, "num": num_char_dict[char]})
    char_list.sort(key=sort_on, reverse=True)
    return char_list