def get_longest_words(word_list):
    longest_words = []
    max_length = 0

    # Iterate through the list to find the longest words
    for word in word_list:
        word_length = len(word)
        if word_length > max_length:
            longest_words = [word] # Found a longer word, update the list
            max_length = word_length
        elif word_length == max_length:
            longest_words.append(word) # Found another word of the same length

    return longest_words, max_length

# Get a list of words from the user
words_input = input("Enter a list of words separated by spaces: ")
words = words_input.split()

# Get the longest words and their length
longest_words, max_length = get_longest_words(words)

# Display the results
if longest_words:
    print(f"\nThe longest word(s) with {max_length} characters:")
    for word in longest_words:
        print(f'- {word}')
else:
    print("\nNo words entered.")