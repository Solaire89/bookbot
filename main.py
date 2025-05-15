
from stats import get_num_words, get_sorted_chars, character_count
import sys

def main():
    # With block automatically opens and closes the file
    if len(sys.argv) < 2:
        print("'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(book_path) as f:
        file_contents = f.read()
        num_of_words = get_num_words(file_contents)
        character_num = character_count(file_contents)
        char_list = get_sorted_chars(character_num)
        print(f"--- Begin report of <{book_path}> ---")
        print(f"Found {num_of_words} total words")
        print()  # blank line
        for char_dict in char_list:
            print(f"{char_dict['char']}: {char_dict['num']}")
        print()
        print("--- End report ---")


main() # Calling the function
