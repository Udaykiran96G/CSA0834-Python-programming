def count_words(input_string):
    # Split the input string into words based on whitespace
    words = input_string.split()
    
    # Count the number of words
    num_words = len(words)
    
    return num_words

# Example usage
input_string = "This is an example string with several words."
word_count = count_words(input_string)

print(f"Number of words: {word_count}")
