import re

def categorize_comments(input_code):
    single_line_comments = []
    multi_line_comments = []

    # Regular expression patterns to match single-line and multi-line comments
    single_line_pattern = r'#.*$'
    multi_line_pattern = r"'''(.*?)'''|\"\"\"(.*?)\"\"\""

    # Find single-line comments
    single_line_comments = re.findall(single_line_pattern, input_code, re.MULTILINE)

    # Find multi-line comments
    multi_line_comments = re.findall(multi_line_pattern, input_code, re.DOTALL)

    return single_line_comments, multi_line_comments

if __name__ == "__main__":
    input_code = """
    # This is a single-line comment.
    print("Hello, world!")  # Another single-line comment
    # Comment after code

    '''This is a multi-line
    comment.'''
    
    \"\"\"
    This is another multi-line
    comment.
    \"\"\"
    """

    single_line_comments, multi_line_comments = categorize_comments(input_code)

    print("Single-line comments:")
    for comment in single_line_comments:
        print(comment)

    print("\nMulti-line comments:")
    for comment in multi_line_comments:
        # Filter out empty matches
        comment = "".join(filter(None, comment))
        print(comment)
