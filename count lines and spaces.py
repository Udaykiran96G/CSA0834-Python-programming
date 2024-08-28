def count_lines_and_spaces(input_string):
    # Count the number of lines (newline characters)
    num_lines = input_string.count('\n') + 1  # Adding 1 to account for the last line which doesn't end with a newline
    
    # Count the number of spaces
    num_spaces = input_string.count(' ')
    
    return num_lines, num_spaces

# Example usage
input_string = """This is a sample string.
It has multiple lines.
And some spaces."""

lines, spaces = count_lines_and_spaces(input_string)

print(f"Number of lines: {lines}")
print(f"Number of spaces: {spaces}")
