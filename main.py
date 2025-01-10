
def main():
    # With block automatically opens and closes the file
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_of_words = get_num_words(file_contents)
        character_num = character_count(file_contents)
        char_list = get_sorted_chars(character_num)
        print(f"{num_of_words} words found in the document")
        print()  # blank line
        for char_dict in char_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(novel):
    char_dictionary = {}
    novel = novel.lower()
    for character in novel:
        if character.isalpha():
            if character not in char_dictionary:
                char_dictionary[character] = 1
            else:
                char_dictionary[character] += 1
    return char_dictionary

def sort_on(dict):
    return dict["num"]

def get_sorted_chars(char_dictionary):
    char_list = []
    for char, count in char_dictionary.items():
            char_dict = {'char': char, 'num': count}
            char_list.append(char_dict)
    # Your code here to convert dictionary to list of dictionaries
    # Then sort the list
    char_list.sort(reverse=True, key=sort_on)
    return char_list

print("--- Begin report of books/frankenstein.txt ---")
main() # Calling the function
print("--- End report ---")