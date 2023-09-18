def remove_comments(input_code):
    lines = input_code.split("\n")
    code_without_comments = []

    for line in lines:
        # Remove comments by splitting at the first occurrence of '#' and taking the first part
        code_without_comments.append(line.split('/*', 1)[0])

    # Join the lines without comments to reconstruct the code
    code_without_comments = "\n".join(code_without_comments)

    return code_without_comments

if __name__ == "__main__":
    input_code = """
    Enter Program $ for termination:
{
int a[3],t1,t2;
t1=2; a[0]=1; a[1]=2; a[t1]=3;
t2=-(a[2]+t1*6)/(a[2]-t1);
if t2>5 then
print(t2);
else {
int t3;
t3=99;
t2=-25;
print(-t1+t2*t3); /* this is a comment on 2 lines */
} endif
}
$
"""

    code_without_comments = remove_comments(input_code)

    print("Code without comments:")
    print(code_without_comments)
