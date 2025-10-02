from stats import get_word_count, get_char_dict, sorted_char_dict


def main():
    book_path  = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    char_dict = get_char_dict(book_text)
    sorted_dict = sorted_char_dict(char_dict)
    print_report(book_path, num_words, sorted_dict)

def get_book_text(book_path):
    with open(book_path) as ebook:
        return ebook.read()

def print_report(book_path, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_count in sorted_dict:
        if not char_count["char"].isalpha():
            continue
        print(f"{char_count['char']}: {char_count['num']}")

    print("============== END ==============")

    
main()
