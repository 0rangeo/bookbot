from stats import get_num_words,character_count, sorted_dict
import sys

def main():
    # book_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_dict = character_count(text)
    # print(character_dict)
    sorted_characters = sorted_dict(character_dict)
    # print(sorted_characters)
    for i in sorted_characters:
        if i[0].isalpha(): 
            print(f"{i[0]}: {i[1]}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    


main()