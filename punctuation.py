def main():
    # With block automatically opens and closes the file
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    punct_count = count_punctuation(file_contents)
    sentence_count = count_sentences(file_contents)
    sorted_punct = get_sort_punct(punct_count)
    print()
    print(f"{punct_count} found in the doument")
    print()
    for punct_dict in sorted_punct:
        print(f"There {punct_dict['char']} punctuation was found {punct_dict['num']} times")
    print("--- End Report ---")

def sort_on(dict):
    return dict["num"]

def count_punctuation(text):
    punct_dict = {}
    punct_marks = ['.', ';', ',', ':', '?', '!']
    for char in text:
        if char in punct_marks:
            if char not in punct_dict:
                punct_dict[char] = 1
            else:
                punct_dict[char] += 1
    return punct_dict


def count_sentences(text):
    sentence_endings = ['.', '!', '?']
    sentence_count = 0
    for punct in text:
        if punct in sentence_endings: # Check if current char is a sentence ending
            sentence_count += 1
    # What logic would you use to count sentences?
    return sentence_count

def get_sort_punct(punct_dict):
    punct_list = []
    # Convert dictionary to list of dictionaries
    for char, count in punct_dict.items():
        char_info = {
            "char": char,
            "num": count
        }
        punct_list.append(char_info)
    punct_list.sort(reverse=True, key=sort_on)
    # Now we need to sort it...
    # Remember the sort_on function from the previous exercise?
    return punct_list

print("--- Begin report of books/frankenstein.txt ---")
main() # Calling the function
print("--- End report ---")