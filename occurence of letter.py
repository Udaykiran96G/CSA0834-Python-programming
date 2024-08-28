def count_letter_occurrences(input_string, letter):
    # Ensure the letter is a single character
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter should be a single character.")
    
    # Count the occurrences of the letter in the input string
    count = input_string.count(letter)
    return count

# Example usage
input_string = "Hello, world!"
letter = "o"
occurrences = count_letter_occurrences(input_string, letter)

print(f"The letter '{letter}' occurs {occurrences} times in the string.")
