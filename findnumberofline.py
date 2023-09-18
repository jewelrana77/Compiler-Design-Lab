import re

def find_comment_line_numbers(input_code):
    comment_line_numbers = []

    # Regular expression pattern to match comments
    comment_pattern = r'#.*$'

    # Split the code into lines and analyze each line
    lines = input_code.split('\n')
    for line_number, line in enumerate(lines, start=1):
        if re.match(comment_pattern, line):
            comment_line_numbers.append(line_number)

    return comment_line_numbers

if __name__ == "__main__":
    input_code = """
    # This is a comment on line 2.
    print("Hello, world!")  # Another comment on line 4
    # Comment after code on line 6

    '''This is a multi-line
    comment on line 8.'''
    
    \"\"\"
    This is another multi-line
    comment on line 11.
    \"\"\"
    """

    comment_line_numbers = find_comment_line_numbers(input_code)

    print("Line numbers with comments:")
    for line_number in comment_line_numbers:
        print(line_number)
