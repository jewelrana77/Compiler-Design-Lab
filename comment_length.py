def count_letters_in_comments(input_code):
    lines = input_code.split("\n")
    comment_count = 0
    total_comment_letters = 0

    for line in lines:
        
        if line.strip().startswith("#"):
            comment_count += 1
            
            comment_text = line.lstrip("#").strip()
            total_comment_letters += len(comment_text)

    return comment_count, total_comment_letters

if __name__ == "__main__":
    user_input = input("Enter something: ")

    comment_count, total_comment_letters = count_letters_in_comments(user_input)

    print("Number of Comments:", comment_count)
    print("Total Letters in Comments:", total_comment_letters)
