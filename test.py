def count_sentences(text):
    sentence_endings = ['.', '!', '?']
    sentence_count = 0
    for punct in text:
        if punct in sentence_endings: # Check if current char is a sentence ending
            sentence_count += 1
    # What logic would you use to count sentences?
    return sentence_count

test = "Hello, World! How do you do today? I would like to test this."
print(count_sentences(test))