import sys
from stats import get_word_count, get_char_dict, sorted_char_dict

# main function to run the program
def main():
    book_path = get_book_path()    
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    char_dict = get_char_dict(book_text)
    sorted_dict = sorted_char_dict(char_dict)
    print_report(book_path, num_words, sorted_dict)

# retrieves path to book from command line arguments
def get_book_path():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

# reads the book file and returns its text
def get_book_text(book_path):
    with open(book_path) as ebook:
        return ebook.read()
    
# prints the analysis report
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

# prints list of strings passed to python3 via line arguments
    print(sys.argv)
main()
